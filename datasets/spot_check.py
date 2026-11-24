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
"""Spot check one season against a third source that shares no ids with the first two.

Games are checked against NCAA.com's weekly scoreboard pages. Polls are
checked against College Poll Archive. Neither site uses the primary
source's ids, so every match is made on the date, the scores, and the
team names. That makes this check independent of the id-based check in
cross_check.py.

Which games get checked
    1. Twenty-five games drawn at random with a fixed seed, so the draw is
       the same every time this script runs.
    2. Every game played by a team ranked in the top 10 of the last AP poll
       in the dataset.
    3. As a bonus, every other game in the season is matched too, and the
       totals are reported, but the formal record is the list above.

What it reads
    datasets/<season>/games.csv, teams.csv, ap_poll.csv
    datasets/_raw/<season>/ncaa_scoreboard_week_*.html
    datasets/_raw/<season>/cpa_poll_*.html

What it writes
    datasets/<season>/spot_checks.json   one record per checked game and poll,
                                         with the URL that was checked
    datasets/aliases.csv                 every NCAA.com and College Poll
                                         Archive team name seen, mapped to
                                         the canonical name

How to run it
    python3 datasets/spot_check.py --season 2024
It exits with status 1 if any checked game or poll row disagrees.
"""

import argparse
import csv
import html
import json
import random
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

DATASETS = Path(__file__).resolve().parent
EASTERN = ZoneInfo("America/New_York")
RANDOM_SEED = 20261124
RANDOM_GAMES = 25

# Abbreviations the NCAA uses in short team names, expanded for matching.
ABBREVIATIONS = {
    "st.": "state", "ky.": "kentucky", "mich.": "michigan", "fla.": "florida", "ga.": "georgia",
    "tenn.": "tennessee", "miss.": "mississippi", "ariz.": "arizona", "colo.": "colorado",
    "wash.": "washington", "ill.": "illinois", "conn.": "connecticut", "ark.": "arkansas",
    "la.": "louisiana", "ala.": "alabama", "mo.": "missouri", "caro.": "carolina", "so.": "southern",
    "n.c.": "north carolina", "okla.": "oklahoma", "ind.": "indiana", "minn.": "minnesota",
    "wis.": "wisconsin", "neb.": "nebraska", "ore.": "oregon", "va.": "virginia", "pa.": "pennsylvania",
    "md.": "maryland", "n.m.": "new mexico", "s.c.": "south carolina", "cal.": "california",
}

# Names that abbreviation expansion alone cannot resolve. Keys are the names
# as the third-party sources print them; values are the canonical names.
MANUAL_ALIASES = {
    "army west point": "army", "fiu": "florida international", "hawaii": "hawai'i",
    "miami (fl)": "miami", "niu": "northern illinois", "san jose state": "san josé state",
    "southern california": "usc", "ulm": "ul monroe", "south florida": "south florida",
    "southern mississippi": "southern miss", "uiw": "incarnate word", "uni": "northern iowa",
    "sfa": "stephen f. austin", "etsu": "east tennessee state", "lamar university": "lamar",
    "central connecticut state": "central connecticut", "liu": "long island university",
    "prairie view": "prairie view a&m", "southeast missouri state": "southeast missouri state",
    "umass": "massachusetts", "ole miss": "ole miss", "pitt": "pittsburgh", "app state": "app state",
    "louisiana-monroe": "ul monroe", "louisiana-lafayette": "louisiana", "north carolina state": "nc state",
    "n.c. state": "nc state", "texas-san antonio": "utsa", "texas-el paso": "utep",
    "alabama-birmingham": "uab", "nevada-las vegas": "unlv", "brigham young": "byu",
    "central florida": "ucf", "connecticut": "uconn", "southern methodist": "smu",
    "texas christian": "tcu", "louisiana state": "lsu", "miami (oh)": "miami (oh)",
    "mississippi": "ole miss", "san josé state": "san josé state",
    "ark.-pine bluff": "arkansas-pine bluff", "southeastern louisiana": "se louisiana",
    "alcorn": "alcorn state", "ualbany": "albany", "albany (ny)": "albany",
    "southern u.": "southern", "utrgv": "ut rio grande valley", "mississippi val.": "mississippi valley state",
}


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, columns):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalize(name):
    """Lower-case a team name and expand the abbreviations the sources use."""
    words = []
    for word in name.lower().replace("&amp;", "&").split():
        words.append(ABBREVIATIONS.get(word, word))
    text = " ".join(words)
    return MANUAL_ALIASES.get(text, text)


def canonical_lookup(teams):
    """Map normalized spellings of every canonical team name back to the name."""
    lookup = {}
    for team in teams:
        name = team["team"]
        lookup[normalize(name)] = name
        lookup[name.lower()] = name
    return lookup


# ---------------------------------------------------------------------------
# NCAA.com games
# ---------------------------------------------------------------------------

def load_ncaa_contests(raw_dir):
    """Pull the embedded game list out of every weekly NCAA.com page."""
    decoder = json.JSONDecoder()
    contests = {}
    for path in sorted(raw_dir.glob("ncaa_scoreboard_week_*.html")):
        text = path.read_text(encoding="utf-8", errors="replace")
        marker = '"initialGames":'
        start = text.find(marker)
        if start < 0:
            continue
        games, _ = decoder.raw_decode(text, start + len(marker))
        for game in games:
            if game.get("gameState") != "F":
                continue
            sides = {"home" if t["isHome"] else "away": t for t in game["teams"]}
            if len(sides) != 2:
                continue
            moment = datetime.fromtimestamp(game["startTimeEpoch"], tz=EASTERN)
            contests[str(game["contestId"])] = {
                "contest_id": str(game["contestId"]),
                "url": "https://www.ncaa.com" + game["url"],
                "game_date": moment.date().isoformat(),
                "home_name": sides["home"]["nameShort"], "away_name": sides["away"]["nameShort"],
                "home_score": int(sides["home"]["score"]), "away_score": int(sides["away"]["score"]),
            }
    return contests


def match_contest(row, contests, lookup):
    """Find the NCAA.com game that is the same game as a games.csv row.

    A match has the same Eastern date and the same pair of scores, and the
    names of the winner and loser resolve to the same canonical teams. A
    late kickoff in Hawaii can land on the next calendar day in one source
    and not the other, so a one-day difference is allowed and recorded.
    """
    ours = {row["home_score"], row["away_score"]}
    same_day = row["game_date"]
    next_day = (date.fromisoformat(same_day) + timedelta(days=1)).isoformat()
    candidates = []
    for contest in contests.values():
        if contest["game_date"] not in (same_day, next_day):
            continue
        if {str(contest["home_score"]), str(contest["away_score"])} != ours:
            continue
        candidates.append(contest)
    for contest in candidates:
        home = lookup.get(normalize(contest["home_name"]))
        away = lookup.get(normalize(contest["away_name"]))
        if {home, away} == {row["home_team"], row["away_team"]}:
            return contest, home, away
    return None, None, None


def check_game(row, contest, home, away):
    """Compare one games.csv row with its NCAA.com match and return the record."""
    winner = home if contest["home_score"] > contest["away_score"] else away
    loser = away if winner == home else home
    winner_score = max(contest["home_score"], contest["away_score"])
    loser_score = min(contest["home_score"], contest["away_score"])
    checks = {
        "game_date": (row["game_date"], contest["game_date"]),
        "winner": (row["winner"], winner),
        "loser": (row["loser"], loser),
        "winner_score": (max(int(row["home_score"]), int(row["away_score"])), winner_score),
        "loser_score": (min(int(row["home_score"]), int(row["away_score"])), loser_score),
    }
    mismatches = {field: {"ours": str(a), "ncaa": str(b)} for field, (a, b) in checks.items() if str(a) != str(b)}
    date_note = ""
    if "game_date" in mismatches:
        # The scores and teams matched on the next calendar day: a late
        # kickoff that one source files under the next day. Keep it as a note.
        date_note = f"NCAA.com files this game under {contest['game_date']}"
        del mismatches["game_date"]
    return {
        "date_note": date_note,
        "game_id": row["game_id"], "game_date": row["game_date"],
        "matchup": f"{row['away_team']} at {row['home_team']}",
        "ours": f"{row['winner']} {max(int(row['home_score']), int(row['away_score']))}, {row['loser']} {min(int(row['home_score']), int(row['away_score']))}",
        "ncaa": f"{winner} {winner_score}, {loser} {loser_score}",
        "ncaa_home_designation": home, "our_home_designation": row["home_team"],
        "url": contest["url"], "result": "pass" if not mismatches else "FAIL", "mismatches": mismatches,
    }


def select_games(games, ap_rows):
    """The random draw plus every game of the last AP top 10."""
    ordered = sorted(games, key=lambda r: r["game_id"])
    drawn = random.Random(RANDOM_SEED).sample(ordered, RANDOM_GAMES)
    last_poll = max(r["poll_date"] for r in ap_rows)
    top10 = {r["team"] for r in ap_rows if r["poll_date"] == last_poll and int(r["rank"]) <= 10}
    selected = {r["game_id"]: ("random draw", r) for r in drawn}
    for row in ordered:
        if row["home_team"] in top10 or row["away_team"] in top10:
            selected.setdefault(row["game_id"], ("final AP top 10", row))
    return selected, sorted(top10), last_poll


# ---------------------------------------------------------------------------
# College Poll Archive polls
# ---------------------------------------------------------------------------

def parse_cpa_poll(path):
    """Read one College Poll Archive page into (heading, rows)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    heading = re.search(r"<h2>(.*?)</h2>", text, re.S)
    heading = html.unescape(re.sub("<[^>]+>", "", heading.group(1))).strip() if heading else ""
    rows = []
    for raw_row in re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S):
        cells = [html.unescape(re.sub("<[^>]+>", "", c)).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", raw_row, re.S)]
        if not cells or not cells[0].isdigit():
            continue
        record_index = next((i for i, c in enumerate(cells) if re.fullmatch(r"\d+-\d+(-\d+)?", c)), None)
        if record_index is None or record_index < 3:
            continue
        team_cell = cells[record_index - 2]
        votes = re.search(r"\((\d+)\)\s*$", team_cell)
        rows.append({
            "rank": int(cells[0]),
            "team": re.sub(r"\s*\(\d+\)\s*$", "", team_cell).strip(),
            "first_place_votes": int(votes.group(1)) if votes else 0,
            "points": int(cells[record_index + 1].replace(",", "")),
        })
    return heading, rows


def cpa_poll_date(heading, season, our_dates):
    """Turn 'November 26, 2023 AP Football Poll' into 2023-11-26.

    The preseason page has no date in its heading, so it maps to the first
    poll date in our table.
    """
    found = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4})", heading)
    if found:
        return datetime.strptime(found.group(1), "%B %d, %Y").date().isoformat()
    if "Preseason" in heading:
        return min(our_dates)
    return None


def settled_poll_keys(out_dir):
    """Poll values that resolutions.json already settles: {(poll date, team, field)}."""
    path = out_dir / "resolutions.json"
    if not path.exists():
        return set()
    return {(r["poll_date"], r["team"], r["field"]) for r in json.loads(path.read_text()) if "poll_file" in r}


def check_polls(raw_dir, ap_rows, lookup, aliases, settled):
    """Compare every archived AP poll page with our ap_poll.csv rows.

    A difference that resolutions.json already settles (because a published
    copy of the poll confirmed our value) is reported as settled rather
    than as a failure.
    """
    ours_by_date = {}
    for row in ap_rows:
        ours_by_date.setdefault(row["poll_date"], []).append(row)
    records = []
    for path in sorted(raw_dir.glob("cpa_poll_*.html")):
        heading, rows = parse_cpa_poll(path)
        released = cpa_poll_date(heading, None, ours_by_date)
        url = "https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=" + path.stem.split("_")[-1]
        if released is None or released not in ours_by_date:
            records.append({"poll_date": released, "heading": heading, "url": url, "result": "not in dataset", "mismatches": {}})
            continue
        theirs = {}
        for row in rows:
            canonical = lookup.get(normalize(row["team"]))
            if canonical:
                aliases.append(("college_poll_archive", row["team"], canonical))
            theirs[canonical or row["team"]] = row
        mismatches = {}
        for row in ours_by_date[released]:
            other = theirs.get(row["team"])
            if other is None:
                mismatches[row["team"]] = {"ours": f"rank {row['rank']}", "archive": "not listed"}
                continue
            for field in ("rank", "points", "first_place_votes"):
                mine, yours = str(row[field]), str(other[field])
                if mine != yours:
                    mismatches[f"{row['team']} {field}"] = {"ours": mine, "archive": yours}
        extra = set(theirs) - {row["team"] for row in ours_by_date[released]}
        for team in sorted(extra):
            mismatches[team] = {"ours": "not listed", "archive": f"rank {theirs[team]['rank']}"}
        settled_here = {key: value for key, value in mismatches.items()
                        if (released, key.rsplit(" ", 1)[0], key.rsplit(" ", 1)[1]) in settled}
        open_here = {key: value for key, value in mismatches.items() if key not in settled_here}
        result = "pass" if not mismatches else ("settled" if not open_here else "FAIL")
        records.append({"poll_date": released, "heading": heading, "url": url,
                        "teams_compared": len(ours_by_date[released]),
                        "result": result, "mismatches": open_here, "settled": settled_here})
    return records


def update_aliases(pairs):
    path = DATASETS / "aliases.csv"
    rows = {(r["source"], r["alias"]): r["canonical_team"] for r in read_csv(path)} if path.exists() else {}
    for source, alias, canonical in pairs:
        rows[(source, alias)] = canonical
    out = [{"source": s, "alias": a, "canonical_team": c} for (s, a), c in sorted(rows.items())]
    write_csv(path, out, ["source", "alias", "canonical_team"])


def main():
    parser = argparse.ArgumentParser(description="Spot check one season against NCAA.com and College Poll Archive.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    out_dir = DATASETS / str(args.season)
    raw_dir = DATASETS / "_raw" / str(args.season)

    games = read_csv(out_dir / "games.csv")
    teams = read_csv(out_dir / "teams.csv")
    ap_rows = read_csv(out_dir / "ap_poll.csv")
    lookup = canonical_lookup(teams)
    contests = load_ncaa_contests(raw_dir)

    # Match every game so the alias table is complete and the totals are known.
    aliases, matched, unmatched = [], {}, []
    for row in games:
        contest, home, away = match_contest(row, contests, lookup)
        if contest is None:
            unmatched.append(row)
            continue
        matched[row["game_id"]] = (contest, home, away)
        aliases.append(("ncaa", contest["home_name"], home))
        aliases.append(("ncaa", contest["away_name"], away))

    selected, top10, last_poll = select_games(games, ap_rows)
    game_records = []
    for game_id, (why, row) in sorted(selected.items(), key=lambda kv: (kv[1][1]["game_date"], kv[0])):
        if game_id not in matched:
            game_records.append({"game_id": game_id, "game_date": row["game_date"], "reason": why,
                                 "matchup": f"{row['away_team']} at {row['home_team']}",
                                 "result": "FAIL", "mismatches": {"presence": {"ours": "in games.csv", "ncaa": "no matching game found"}}})
            continue
        record = check_game(row, *matched[game_id])
        record["reason"] = why
        game_records.append(record)

    all_records = [check_game(row, *matched[row["game_id"]]) for row in games if row["game_id"] in matched]
    poll_records = check_polls(raw_dir, ap_rows, lookup, aliases, settled_poll_keys(out_dir))
    update_aliases(aliases)

    report = {
        "season": args.season,
        "random_seed": RANDOM_SEED,
        "final_ap_poll_date": last_poll,
        "final_ap_top_10": top10,
        "games_checked": len(game_records),
        "games_passed": sum(1 for r in game_records if r["result"] == "pass"),
        "all_games_matched_in_ncaa": len(matched),
        "all_games_total": len(games),
        "all_games_agreeing": sum(1 for r in all_records if r["result"] == "pass"),
        "games_not_found_in_ncaa": [{"game_id": r["game_id"], "game_date": r["game_date"], "matchup": f"{r['away_team']} at {r['home_team']}"} for r in unmatched],
        "home_designation_differences": [r for r in all_records if r["ncaa_home_designation"] != r["our_home_designation"]],
        "game_checks": game_records,
        "poll_checks": poll_records,
    }
    (out_dir / "spot_checks.json").write_text(json.dumps(report, indent=2) + "\n")

    failed_games = [r for r in game_records if r["result"] != "pass"]
    failed_polls = [r for r in poll_records if r["result"] == "FAIL"]
    print(f"season {args.season}: {report['games_passed']} of {len(game_records)} selected games agree with NCAA.com")
    print(f"  all games: {report['all_games_agreeing']} of {len(games)} agree, {len(unmatched)} not found")
    print(f"  home designation differs for {len(report['home_designation_differences'])} games")
    print(f"  polls: {sum(1 for r in poll_records if r['result'] == 'pass')} pass, "
          f"{sum(1 for r in poll_records if r['result'] == 'settled')} settled by a published copy, {len(failed_polls)} fail, "
          f"{sum(1 for r in poll_records if r['result'] == 'not in dataset')} archived polls outside the dataset")
    for row in unmatched[:20]:
        print("   not found:", row["game_date"], row["away_team"], "at", row["home_team"], row["away_score"], row["home_score"])
    for record in (failed_games + failed_polls)[:20]:
        print("   FAIL:", json.dumps(record)[:400])
    if failed_games or failed_polls:
        sys.exit(1)


if __name__ == "__main__":
    main()
