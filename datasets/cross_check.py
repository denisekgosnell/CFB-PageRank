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
"""Compare one season's dataset against ESPN, the independent second source.

The primary source and ESPN share game ids and team ids, so every game in
games.csv can be looked up directly in ESPN's scoreboard. For each game we
compare the date, both teams, both scores, the neutral-site flag, the
conference-game flag, and the overtime flag. We also walk the other way:
every completed ESPN game with an FBS team, played on or before rivalry
week, has to be in games.csv. Then we do the same for the polls.

What it reads
    datasets/<season>/games.csv, teams.csv, ap_poll.csv, coaches_poll.csv,
    cfp_rankings.csv, season_calendar.json
    datasets/_raw/<season>/espn_scoreboard_week_*.json
    datasets/_raw/<season>/espn_rankings_week_*_{ap,coaches,cfp}.json

What it writes
    datasets/<season>/espn_games.csv   ESPN's view of every game, kept so the
                                       test suite can rerun the comparison
                                       without the raw cache
    datasets/<season>/espn_polls.csv   ESPN's view of every poll
    datasets/<season>/cross_check.json every disagreement, with both values
    datasets/aliases.csv               every ESPN team name seen, mapped to
                                       the canonical name in teams.csv

How to run it
    python3 datasets/cross_check.py --season 2024
It exits with status 1 if any game or poll row disagrees.
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

DATASETS = Path(__file__).resolve().parent
EASTERN = ZoneInfo("America/New_York")
POLLS = {"ap": "ap_poll.csv", "coaches": "coaches_poll.csv", "cfp": "cfp_rankings.csv"}


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, columns):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def eastern_date(stamp):
    """ESPN gives times like 2023-09-02T22:00Z. Return the Eastern calendar date."""
    moment = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    return moment.astimezone(EASTERN).date().isoformat()


# ---------------------------------------------------------------------------
# Games
# ---------------------------------------------------------------------------

def load_espn_games(raw_dir):
    """Read every ESPN scoreboard file and return {game_id: row}."""
    games = {}
    for path in sorted(raw_dir.glob("espn_scoreboard_*.json")):
        for event in json.loads(path.read_text()).get("events", []):
            competition = event["competitions"][0]
            sides = {c["homeAway"]: c for c in competition["competitors"]}
            home, away = sides["home"], sides["away"]
            games[event["id"]] = {
                "game_id": event["id"],
                "espn_week": event.get("week", {}).get("number", ""),
                "game_date": eastern_date(event["date"]),
                "home_team_id": home["team"]["id"],
                "home_team_name": home["team"]["location"],
                "away_team_id": away["team"]["id"],
                "away_team_name": away["team"]["location"],
                "home_score": home.get("score", ""),
                "away_score": away.get("score", ""),
                "neutral_site": "true" if competition.get("neutralSite") else "false",
                "conference_game": "true" if competition.get("conferenceCompetition") else "false",
                "overtime": "true" if (event["status"].get("period") or 0) > 4 else "false",
                "completed": "true" if event["status"]["type"].get("completed") else "false",
                "status": event["status"]["type"].get("name", ""),
            }
    return games


def compare_games(ours, theirs, team_ids):
    """Return a list of disagreements between games.csv and ESPN."""
    problems = []
    fields = ["game_date", "home_score", "away_score", "neutral_site", "conference_game", "overtime"]
    for row in ours:
        other = theirs.get(row["game_id"])
        if other is None:
            problems.append({"game_id": row["game_id"], "field": "presence", "ours": "in games.csv", "espn": "not found"})
            continue
        checks = {field: (row[field], other[field]) for field in fields}
        checks["home_team"] = (team_ids[row["home_team"]], other["home_team_id"])
        checks["away_team"] = (team_ids[row["away_team"]], other["away_team_id"])
        for field, (mine, yours) in checks.items():
            if str(mine) != str(yours):
                problems.append({"game_id": row["game_id"], "game_date": row["game_date"],
                                 "matchup": f"{row['away_team']} at {row['home_team']}",
                                 "field": field, "ours": str(mine), "espn": str(yours)})
    return problems


def split_settled(problems, out_dir):
    """Separate the disagreements that resolutions.json already settles.

    A settled disagreement is one where a third source decided the value,
    so it is reported for the record but does not fail the check.
    """
    path = out_dir / "resolutions.json"
    resolutions = json.loads(path.read_text()) if path.exists() else []
    settled_keys = {(r.get("game_id"), r["field"]) for r in resolutions}
    open_problems, settled = [], []
    for problem in problems:
        if (problem["game_id"], problem["field"]) in settled_keys:
            settled.append(problem)
        else:
            open_problems.append(problem)
    return open_problems, settled


def games_only_in_espn(ours, theirs, fbs_ids, calendar):
    """ESPN games with an FBS team, completed, inside the season window, that we lack."""
    have = {row["game_id"] for row in ours}
    last_week_date = calendar["weeks"][str(calendar["rivalry_week"])]["last_game"] if str(calendar["rivalry_week"]) in calendar["weeks"] else calendar["last_game_in_dataset"]
    missing = []
    for game_id, row in theirs.items():
        if game_id in have or row["completed"] != "true":
            continue
        if row["home_team_id"] not in fbs_ids and row["away_team_id"] not in fbs_ids:
            continue
        if row["game_date"] > last_week_date:
            continue
        missing.append(row)
    return missing


# ---------------------------------------------------------------------------
# Polls
# ---------------------------------------------------------------------------

def load_espn_polls(raw_dir, id_to_team):
    """Read every ESPN poll file into rows keyed by (poll, release date)."""
    polls = {}
    for path in sorted(raw_dir.glob("espn_rankings_week_*_*.json")):
        if path.name.endswith("_list.json"):
            continue
        short = path.name.split("_")[4].split(".")[0]
        data = json.loads(path.read_text())
        released = data["date"][:10]
        if (short, released) in polls:
            continue
        rows = []
        for rank in data["ranks"]:
            team_id = rank["team"]["$ref"].split("/teams/")[1].split("?")[0]
            rows.append({
                "poll": short, "poll_date": released, "rank": rank["current"],
                "team_id": team_id, "team": id_to_team.get(team_id, ""),
                "points": int(rank["points"]) if rank.get("points") is not None else "",
                "first_place_votes": rank.get("firstPlaceVotes", ""),
            })
        polls[(short, released)] = rows
    return polls


def compare_polls(out_dir, espn_polls):
    """Compare each of our poll tables against ESPN's rows for the same release date."""
    problems = []
    for short, file_name in POLLS.items():
        ours = read_csv(out_dir / file_name)
        by_date = {}
        for row in ours:
            by_date.setdefault(row["poll_date"], []).append(row)
        for released, rows in by_date.items():
            theirs = espn_polls.get((short, released))
            if theirs is None:
                problems.append({"poll": short, "poll_date": released, "field": "presence", "ours": f"{len(rows)} rows", "espn": "no poll on this date"})
                continue
            mine = {(r["team"], int(r["rank"])) for r in rows}
            yours = {(r["team"], int(r["rank"])) for r in theirs}
            for team, rank in sorted(mine - yours):
                problems.append({"poll": short, "poll_date": released, "field": "rank", "ours": f"{team} {rank}", "espn": "not this rank"})
            for team, rank in sorted(yours - mine):
                problems.append({"poll": short, "poll_date": released, "field": "rank", "ours": "not this rank", "espn": f"{team} {rank}"})
            if short != "cfp":
                theirs_by_team = {r["team"]: r for r in theirs}
                for row in rows:
                    other = theirs_by_team.get(row["team"])
                    if other is None:
                        continue
                    for field in ("points", "first_place_votes"):
                        if str(row[field]) != str(other[field]):
                            problems.append({"poll": short, "poll_date": released, "field": f"{row['team']} {field}", "ours": str(row[field]), "espn": str(other[field])})
    return problems


# ---------------------------------------------------------------------------
# Aliases
# ---------------------------------------------------------------------------

def update_aliases(pairs):
    """Merge (source, alias, canonical) triples into datasets/aliases.csv."""
    path = DATASETS / "aliases.csv"
    rows = {(r["source"], r["alias"]): r["canonical_team"] for r in read_csv(path)} if path.exists() else {}
    for source, alias, canonical in pairs:
        rows[(source, alias)] = canonical
    out = [{"source": s, "alias": a, "canonical_team": c} for (s, a), c in sorted(rows.items())]
    write_csv(path, out, ["source", "alias", "canonical_team"])


def main():
    parser = argparse.ArgumentParser(description="Cross-check one season against ESPN.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()

    out_dir = DATASETS / str(args.season)
    raw_dir = DATASETS / "_raw" / str(args.season)
    games = read_csv(out_dir / "games.csv")
    teams = read_csv(out_dir / "teams.csv")
    calendar = json.loads((out_dir / "season_calendar.json").read_text())
    team_ids = {t["team"]: t["team_id"] for t in teams}
    id_to_team = {t["team_id"]: t["team"] for t in teams}
    fbs_ids = {t["team_id"] for t in teams if t["division"] == "FBS"}

    espn_games = load_espn_games(raw_dir)
    game_problems = compare_games(games, espn_games, team_ids)
    game_problems, settled = split_settled(game_problems, out_dir)
    only_espn = games_only_in_espn(games, espn_games, fbs_ids, calendar)
    espn_polls = load_espn_polls(raw_dir, id_to_team)
    poll_problems = compare_polls(out_dir, espn_polls)

    espn_columns = ["game_id", "espn_week", "game_date", "home_team_id", "home_team_name", "away_team_id",
                    "away_team_name", "home_score", "away_score", "neutral_site", "conference_game",
                    "overtime", "completed", "status"]
    write_csv(out_dir / "espn_games.csv", sorted(espn_games.values(), key=lambda r: (r["game_date"], r["game_id"])), espn_columns)
    poll_rows = [row for key in sorted(espn_polls) for row in espn_polls[key]]
    write_csv(out_dir / "espn_polls.csv", poll_rows, ["poll", "poll_date", "rank", "team_id", "team", "points", "first_place_votes"])

    pairs = []
    for row in espn_games.values():
        for side in ("home", "away"):
            canonical = id_to_team.get(row[side + "_team_id"])
            if canonical:
                pairs.append(("espn", row[side + "_team_name"], canonical))
    update_aliases(pairs)

    report = {
        "season": args.season,
        "games_in_dataset": len(games),
        "games_found_in_espn": sum(1 for g in games if g["game_id"] in espn_games),
        "game_disagreements": game_problems,
        "settled_by_third_source": settled,
        "games_only_in_espn": only_espn,
        "poll_disagreements": poll_problems,
    }
    (out_dir / "cross_check.json").write_text(json.dumps(report, indent=2) + "\n")

    print(f"season {args.season}: {report['games_found_in_espn']} of {len(games)} games found in ESPN")
    print(f"  game disagreements: {len(game_problems)} open, {len(settled)} settled by a third source")
    print(f"  completed ESPN games with an FBS team that we lack: {len(only_espn)}")
    print(f"  poll disagreements: {len(poll_problems)}")
    for problem in (game_problems + poll_problems)[:40]:
        print("  ", problem)
    for row in only_espn[:20]:
        print("   only in ESPN:", row["game_date"], row["away_team_name"], "at", row["home_team_name"], row["status"])
    if game_problems or poll_problems or only_espn:
        sys.exit(1)


if __name__ == "__main__":
    main()
