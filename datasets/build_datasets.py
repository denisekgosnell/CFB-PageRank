# CFB-PageRank
# Copyright 2026 Denise Koessler Gosnell
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Turn the raw records for one season into the dataset CSV files.

What it reads
    datasets/_raw/<season>/cfbd_teams_fbs.json        the FBS team list
    datasets/_raw/<season>/cfbd_games_regular.json    every regular-season game
    datasets/_raw/<season>/cfbd_rankings_regular.json every weekly poll
    datasets/_raw/<season>/espn_rankings_week_*.json  the release date of each poll
    datasets/_raw/<season>/manifest.json              when the records were fetched

What it writes
    datasets/<season>/games.csv            one row per game, see the README
    datasets/<season>/teams.csv            one row per team that appears in games.csv
    datasets/<season>/ap_poll.csv          the AP Top 25, one row per poll per team
    datasets/<season>/coaches_poll.csv     the Coaches Poll, same shape
    datasets/<season>/cfp_rankings.csv     the CFP committee rankings, same shape
    datasets/<season>/excluded_games.json  every game left out, with the reason
    datasets/<season>/season_calendar.json the week windows and the data cutoff

It also reads datasets/<season>/resolutions.json when that file exists.
That file holds the handful of values where the first two sources
disagreed and a third source settled it. See the README for the list.

How to run it
    python3 datasets/build_datasets.py --season 2024

The week rule
    Week 1 is the Tuesday-through-Monday window that ends on Labor Day.
    Week 0 is every game before that window. Each later week is the next
    Tuesday-through-Monday window. Rivalry week is the week that holds the
    Saturday after Thanksgiving. Games after rivalry week are left out.
"""

import argparse
import csv
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

DATASETS = Path(__file__).resolve().parent
EASTERN = ZoneInfo("America/New_York")

# The names the College Football Data API uses for the three polls we keep.
POLL_FILES = {
    "AP Top 25": "ap_poll.csv",
    "Coaches Poll": "coaches_poll.csv",
    "Playoff Committee Rankings": "cfp_rankings.csv",
}
# The short names used in the ESPN file names written by collect.py.
POLL_SHORT = {"AP Top 25": "ap", "Coaches Poll": "coaches", "Playoff Committee Rankings": "cfp"}

GAME_COLUMNS = [
    "game_id", "season", "week", "game_date", "home_team", "away_team",
    "home_score", "away_score", "winner", "loser", "margin",
    "neutral_site", "conference_game", "overtime", "source",
]


# ---------------------------------------------------------------------------
# The calendar
# ---------------------------------------------------------------------------

def labor_day(season):
    """Labor Day is the first Monday of September."""
    first = date(season, 9, 1)
    return first + timedelta(days=(7 - first.weekday()) % 7)


def thanksgiving(season):
    """Thanksgiving is the fourth Thursday of November."""
    first = date(season, 11, 1)
    first_thursday = first + timedelta(days=(3 - first.weekday()) % 7)
    return first_thursday + timedelta(weeks=3)


def week_of(game_day, season):
    """Map a date to its week number using the rule in the docstring."""
    week1_tuesday = labor_day(season) - timedelta(days=6)
    if game_day < week1_tuesday:
        return 0
    return 1 + (game_day - week1_tuesday).days // 7


def eastern_date(start_date_utc):
    """Convert the API's UTC timestamp to the calendar date in US Eastern time."""
    moment = datetime.fromisoformat(start_date_utc.replace("Z", "+00:00"))
    return moment.astimezone(EASTERN).date()


# ---------------------------------------------------------------------------
# Teams
# ---------------------------------------------------------------------------

def load_json(raw_dir, name):
    return json.loads((raw_dir / name).read_text())


def build_teams(fbs_teams, kept_games, season):
    """One row per FBS team, plus one row per FCS team that played an FBS team."""
    rows = {}
    for team in fbs_teams:
        rows[team["school"]] = {
            "team": team["school"], "team_id": team["id"],
            "conference": team.get("conference") or "", "division": "FBS", "season": season,
        }
    for game in kept_games:
        for side in ("home", "away"):
            name = game[side + "Team"]
            if name in rows:
                continue
            classification = (game.get(side + "Classification") or "").upper()
            rows[name] = {
                "team": name, "team_id": game[side + "Id"],
                "conference": game.get(side + "Conference") or "", "division": classification, "season": season,
            }
    return sorted(rows.values(), key=lambda row: row["team"])


# ---------------------------------------------------------------------------
# Games
# ---------------------------------------------------------------------------

def involves_fbs(game):
    return "fbs" in (game.get("homeClassification"), game.get("awayClassification"))


def game_row(game, season):
    """Translate one raw game into one games.csv row."""
    home, away = game["homePoints"], game["awayPoints"]
    home_won = home > away
    return {
        "game_id": str(game["id"]),
        "season": season,
        "week": week_of(eastern_date(game["startDate"]), season),
        "game_date": eastern_date(game["startDate"]).isoformat(),
        "home_team": game["homeTeam"],
        "away_team": game["awayTeam"],
        "home_score": home,
        "away_score": away,
        "winner": game["homeTeam"] if home_won else game["awayTeam"],
        "loser": game["awayTeam"] if home_won else game["homeTeam"],
        "margin": abs(home - away),
        "neutral_site": "true" if game.get("neutralSite") else "false",
        "conference_game": "true" if game.get("conferenceGame") else "false",
        # A game with more than four scoring periods went to overtime.
        "overtime": "true" if len(game.get("homeLineScores") or []) > 4 else "false",
        "source": "cfbd",
    }


def split_games(all_games, season, rivalry_week):
    """Decide which raw games belong in games.csv and why the rest do not."""
    kept, excluded = [], []
    for game in all_games:
        if not involves_fbs(game):
            continue
        played = game.get("completed") and game.get("homePoints") is not None and game.get("awayPoints") is not None
        week = week_of(eastern_date(game["startDate"]), season)
        reason = None
        if not played:
            reason = "not played: no final score in the source"
        elif week > rivalry_week:
            reason = "after rivalry week"
        elif game["homePoints"] == game["awayPoints"]:
            reason = "tie score in the source, which cannot happen in a completed game"
        if reason:
            excluded.append({
                "game_id": str(game["id"]), "game_date": eastern_date(game["startDate"]).isoformat(),
                "week": week, "home_team": game["homeTeam"], "away_team": game["awayTeam"],
                "notes": game.get("notes"), "reason": reason,
            })
        else:
            kept.append(game)
    return kept, excluded


# ---------------------------------------------------------------------------
# Polls
# ---------------------------------------------------------------------------

def espn_polls(raw_dir):
    """Read every ESPN poll file: {(label, short): (release date, set of team ids)}."""
    polls = {}
    for path in sorted(raw_dir.glob("espn_rankings_week_*_*.json")):
        if path.name.endswith("_list.json"):
            continue
        label = path.name.split("_")[3]
        short = path.name.split("_")[4].split(".")[0]
        data = json.loads(path.read_text())
        ids = {rank["team"]["$ref"].split("/teams/")[1].split("?")[0] for rank in data["ranks"]}
        polls[(label, short)] = (data["date"][:10], ids)
    return polls


def release_date(cfbd_week, short, team_ids, polls, notes):
    """Find the ESPN poll with the same 25 teams and return its release date.

    The ESPN file for the same week number is tried first, then the
    preseason file, then every other file. The date is accepted only when
    the two sources list the same teams, so a week-numbering difference
    between the sources cannot attach the wrong date to a poll.
    """
    order = [(f"{cfbd_week:02d}", short), ("preseason", short)]
    order += [key for key in polls if key[1] == short and key not in order]
    for key in order:
        if key in polls and polls[key][1] == team_ids:
            return polls[key][0]
    notes.append(f"no ESPN poll lists the same teams as the primary source's {short} poll for week {cfbd_week}")
    return None


def build_polls(rankings, polls, games_rows, teams_rows, poll_cutoff):
    """Build the three poll tables. Returns {file name: rows} and a list of notes."""
    fbs_names = {row["team"] for row in teams_rows if row["division"] == "FBS"}
    ids_by_name = {row["team"]: str(row["team_id"]) for row in teams_rows}
    game_dates_by_week = {}
    for row in games_rows:
        game_dates_by_week.setdefault(row["week"], []).append(row["game_date"])

    tables = {name: [] for name in POLL_FILES.values()}
    notes = []
    for entry in sorted(rankings, key=lambda e: e["week"]):
        for poll in entry["polls"]:
            if poll["poll"] not in POLL_FILES:
                continue
            team_ids = {ids_by_name.get(rank["school"], "?") for rank in poll["ranks"]}
            released = release_date(entry["week"], POLL_SHORT[poll["poll"]], team_ids, polls, notes)
            if released is None:
                continue
            if released > poll_cutoff:
                continue
            # The poll week is the number of game weeks played before the release.
            weeks_before = [week for week, days in game_dates_by_week.items() if min(days) < released]
            poll_week = max(weeks_before) if weeks_before else 0
            ranks = sorted(poll["ranks"], key=lambda r: (r["rank"], r["school"]))
            if len(ranks) != 25:
                notes.append(f"{poll['poll']} released {released} lists {len(ranks)} teams")
            for rank in ranks:
                if rank["school"] not in fbs_names:
                    raise SystemExit(f"poll team {rank['school']!r} is not an FBS team in teams.csv")
                row = {
                    "season": entry["season"], "poll_week": poll_week, "source_week": entry["week"],
                    "poll_date": released, "rank": rank["rank"], "team": rank["school"],
                }
                if poll["poll"] != "Playoff Committee Rankings":
                    row["points"] = rank.get("points") if rank.get("points") is not None else ""
                    row["first_place_votes"] = rank.get("firstPlaceVotes") if rank.get("firstPlaceVotes") is not None else ""
                tables[POLL_FILES[poll["poll"]]].append(row)
    return tables, notes


# ---------------------------------------------------------------------------
# Resolutions
# ---------------------------------------------------------------------------

def apply_resolutions(out_dir, games_rows, tables):
    """Apply the values settled by a third source when the first two disagreed.

    datasets/<season>/resolutions.json is written by hand. Each entry names
    a game (or a poll row), the field, the value we keep, the source that
    settled it, and the reason. Entries whose value already matches the
    primary source change nothing but still document the decision.
    """
    path = out_dir / "resolutions.json"
    if not path.exists():
        return []
    resolutions = json.loads(path.read_text())
    games_by_id = {row["game_id"]: row for row in games_rows}
    for item in resolutions:
        if "game_id" in item:
            row = games_by_id[item["game_id"]]
            row[item["field"]] = item["value"]
        else:
            for row in tables[item["poll_file"]]:
                if row["poll_date"] == item["poll_date"] and row["team"] == item["team"]:
                    row[item["field"]] = item["value"]
    return resolutions


# ---------------------------------------------------------------------------
# Writing
# ---------------------------------------------------------------------------

def write_csv(path, rows, columns):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Build the dataset CSV files for one season.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    season = args.season

    raw_dir = DATASETS / "_raw" / str(season)
    out_dir = DATASETS / str(season)
    out_dir.mkdir(parents=True, exist_ok=True)

    fbs_teams = load_json(raw_dir, "cfbd_teams_fbs.json")
    all_games = load_json(raw_dir, "cfbd_games_regular.json")
    rankings = load_json(raw_dir, "cfbd_rankings_regular.json")
    manifest = load_json(raw_dir, "manifest.json")

    rivalry_saturday = thanksgiving(season) + timedelta(days=2)
    rivalry_week = week_of(rivalry_saturday, season)
    poll_cutoff = (rivalry_saturday + timedelta(days=3)).isoformat()

    kept, excluded = split_games(all_games, season, rivalry_week)
    games_rows = sorted((game_row(g, season) for g in kept), key=lambda r: (r["game_date"], r["game_id"]))
    teams_rows = build_teams(fbs_teams, kept, season)

    # Every team named in a game has to be in teams.csv, and every FBS team in
    # games.csv has to be in the FBS team list.
    fbs_names = {t["school"] for t in fbs_teams}
    for game in kept:
        for side in ("home", "away"):
            if game.get(side + "Classification") == "fbs" and game[side + "Team"] not in fbs_names:
                raise SystemExit(f"{game[side + 'Team']!r} is marked FBS in a game but is not in the FBS team list")

    tables, notes = build_polls(rankings, espn_polls(raw_dir), games_rows, teams_rows, poll_cutoff)

    resolutions = apply_resolutions(out_dir, games_rows, tables)

    write_csv(out_dir / "games.csv", games_rows, GAME_COLUMNS)
    write_csv(out_dir / "teams.csv", teams_rows, ["team", "team_id", "conference", "division", "season"])
    for name, rows in tables.items():
        columns = ["season", "poll_week", "source_week", "poll_date", "rank", "team"]
        if name != "cfp_rankings.csv":
            columns += ["points", "first_place_votes"]
        write_csv(out_dir / name, rows, columns)

    last_game = max(row["game_date"] for row in games_rows)
    weeks = sorted({row["week"] for row in games_rows})
    windows = {}
    for week in weeks:
        days = [row["game_date"] for row in games_rows if row["week"] == week]
        windows[str(week)] = {"first_game": min(days), "last_game": max(days),
                              "games": sum(1 for row in games_rows if row["week"] == week)}
    calendar = {
        "season": season,
        "labor_day": labor_day(season).isoformat(),
        "week_1_starts": (labor_day(season) - timedelta(days=6)).isoformat(),
        "thanksgiving": thanksgiving(season).isoformat(),
        "rivalry_saturday": rivalry_saturday.isoformat(),
        "rivalry_week": rivalry_week,
        "poll_cutoff": poll_cutoff,
        "weeks": windows,
        "last_game_in_dataset": last_game,
        "season_complete_through_rivalry_week": max(weeks) >= rivalry_week,
        "data_collected_at": manifest["cfbd_games_regular.json"]["fetched_at"],
        "poll_notes": notes,
        "resolutions_applied": len(resolutions),
    }
    (out_dir / "season_calendar.json").write_text(json.dumps(calendar, indent=2) + "\n")
    (out_dir / "excluded_games.json").write_text(json.dumps(excluded, indent=2) + "\n")

    print(f"season {season}: read {len(all_games)} raw games, kept {len(games_rows)}, excluded {len(excluded)}")
    print(f"  teams: {len(teams_rows)} ({sum(1 for t in teams_rows if t['division'] == 'FBS')} FBS)")
    print(f"  weeks 0..{max(weeks)}, rivalry week {rivalry_week}, last game {last_game}")
    for name, rows in tables.items():
        print(f"  {name}: {len(rows)} rows, {len({r['poll_date'] for r in rows})} polls")
    for note in notes:
        print("  note:", note)


if __name__ == "__main__":
    main()
