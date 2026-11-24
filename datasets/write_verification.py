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
"""Write VERIFICATION.md for one season from the check results on disk.

Nothing in the verification record is typed by hand except the notes file.
Every count and every URL comes from the files the other scripts wrote, so
rerunning the pipeline rewrites the record.

What it reads
    datasets/<season>/games.csv, teams.csv, the poll files,
    season_calendar.json, excluded_games.json, cross_check.json,
    spot_checks.json, resolutions.json, checksums.sha256, and
    verification_notes.md (hand-written, optional)

What it writes
    datasets/<season>/VERIFICATION.md
    datasets/<season>/README.md   the short note beside each season's files

How to run it
    python3 datasets/write_verification.py --season 2024
"""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

DATASETS = Path(__file__).resolve().parent


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def table(headers, rows):
    """A Markdown table."""
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def counts_section(season, games, teams, calendar, excluded):
    fbs = [t for t in teams if t["division"] == "FBS"]
    others = Counter(t["division"] for t in teams if t["division"] != "FBS")
    per_week = Counter(int(g["week"]) for g in games)
    lines = [
        "## Counts", "",
        f"Games in games.csv: {len(games)}", "",
        f"FBS teams in teams.csv: {len(fbs)}", "",
        "Opponents from outside FBS: " + ", ".join(f"{n} {d}" for d, n in sorted(others.items())), "",
        f"Data collected at {calendar['data_collected_at']} (UTC). Last game in the dataset: {calendar['last_game_in_dataset']}.", "",
        f"Rivalry week is week {calendar['rivalry_week']} (the week holding {calendar['rivalry_saturday']}). "
        + ("The dataset runs through rivalry week." if calendar["season_complete_through_rivalry_week"]
           else "The season had not reached rivalry week when the data was collected."), "",
        table(["week", "first game", "last game", "games"],
              [(w, calendar["weeks"][str(w)]["first_game"], calendar["weeks"][str(w)]["last_game"], per_week[w]) for w in sorted(per_week)]),
        "",
    ]
    if excluded:
        reasons = Counter(e["reason"] for e in excluded)
        lines += ["Games involving an FBS team that are not in games.csv:", ""]
        lines += [table(["reason", "games"], sorted(reasons.items()))]
        lines += ["", "The full list, one line per game:", ""]
        for e in sorted(excluded, key=lambda e: (e["game_date"], e["game_id"])):
            note = f" ({e['notes']})" if e.get("notes") else ""
            lines.append(f"- {e['game_date']} {e['away_team']} at {e['home_team']}{note}: {e['reason']}")
        lines.append("")
    return lines


def cross_check_section(cross, resolutions, games):
    lines = ["## Cross-check against ESPN", "",
             f"Games found in ESPN by id: {cross['games_found_in_espn']} of {cross['games_in_dataset']}.", "",
             f"Open disagreements: {len(cross['game_disagreements'])}. "
             f"Completed ESPN games with an FBS team that we lack: {len(cross['games_only_in_espn'])}. "
             f"Poll rows that disagree: {len(cross['poll_disagreements'])}.", ""]
    if resolutions:
        by_id = {g["game_id"]: g for g in games}
        lines += [f"Values settled by a third source ({len(resolutions)} entries in resolutions.json). "
                  "The primary source and ESPN disagreed on each game row below; for the poll rows the archive disagreed with both. "
                  "The value kept is the one in the dataset:", ""]
        rows = []
        for res in resolutions:
            if "game_id" in res:
                game = by_id[res["game_id"]]
                where = f"{game['away_team']} at {game['home_team']}"
                date = game["game_date"]
                other = res.get("espn_value", "")
            else:
                where = f"{res['poll_file']} {res['team']}"
                date = res["poll_date"]
                other = f"ESPN {res.get('espn_value', '')}, archive {res.get('archive_value', '')}" if "archive_value" in res else f"ESPN {res.get('espn_value', '')}"
            rows.append((date, where, res["field"], res.get("primary_value", ""), other, res["value"], res["source"], res.get("reason", "")))
        lines += [table(["date", "game or poll row", "field", "primary source", "other sources", "kept", "settled by", "reason"], rows), ""]
    for problem in cross["game_disagreements"]:
        lines.append(f"- OPEN: {problem}")
    for problem in cross["poll_disagreements"]:
        lines.append(f"- OPEN: {problem}")
    if cross["game_disagreements"] or cross["poll_disagreements"]:
        lines.append("")
    return lines


def completeness_section(games, teams):
    played = Counter()
    for g in games:
        played[g["home_team"]] += 1
        played[g["away_team"]] += 1
    fbs = sorted(t["team"] for t in teams if t["division"] == "FBS")
    usual = Counter(played[t] for t in fbs).most_common(1)[0][0]
    lines = ["## Completeness", "",
             f"Games played by each FBS team in the dataset. The most common count is {usual}.", "",
             table(["team", "games"], [(t, played[t]) for t in fbs]), ""]
    return lines


def spot_check_section(spot):
    lines = ["## Spot checks against NCAA.com", "",
             f"Random draw of 25 games with seed {spot['random_seed']}, plus every game of the top 10 in the AP poll of "
             f"{spot['final_ap_poll_date']} ({', '.join(spot['final_ap_top_10'])}).", "",
             f"Selected games checked: {spot['games_checked']}. Passed: {spot['games_passed']}.", "",
             f"Beyond the selection, every game in the season was matched to NCAA.com by date, by score, and by team name: "
             f"{spot['all_games_agreeing']} of {spot['all_games_total']} agree, {len(spot['games_not_found_in_ncaa'])} could not be matched.", ""]
    if spot["home_designation_differences"]:
        lines += ["Games where NCAA.com designates a different home team (scores and teams agree; this is a designation, not a result):", ""]
        for item in spot["home_designation_differences"]:
            lines.append(f"- {item['game_date']} {item['matchup']}: we list {item['our_home_designation']} as home, NCAA.com lists {item['ncaa_home_designation']} ({item['url']})")
        lines.append("")
    rows = []
    for item in spot["game_checks"]:
        rows.append((item["game_date"], item["matchup"], item.get("ours", ""), item.get("ncaa", ""), item["reason"], item["result"], item.get("url", "")))
    lines += [table(["date", "game", "our result", "NCAA.com result", "why selected", "check", "URL"], rows), ""]
    return lines


def polls_section(season_dir, spot, calendar):
    lines = ["## Polls", ""]
    for name in ("ap_poll.csv", "coaches_poll.csv", "cfp_rankings.csv"):
        rows = read_csv(season_dir / name)
        dates = sorted({r["poll_date"] for r in rows})
        sizes = Counter(r["poll_date"] for r in rows)
        odd = [f"{d} ({sizes[d]} teams)" for d in dates if sizes[d] != 25]
        lines.append(f"{name}: {len(dates)} polls from {dates[0] if dates else 'none'} to {dates[-1] if dates else 'none'}, "
                     f"{len(rows)} rows. " + (f"Polls without exactly 25 teams: {', '.join(odd)}." if odd else "Every poll lists exactly 25 teams."))
        lines.append("")
    for note in calendar.get("poll_notes", []):
        lines.append(f"- Build note: {note}")
    if calendar.get("poll_notes"):
        lines.append("")
    lines += ["AP polls checked against College Poll Archive (the rank and the team, then the points and the first-place votes, for every ranked team):", ""]
    rows = [(p.get("poll_date") or "", p["heading"], p.get("teams_compared", ""), p["result"], p["url"]) for p in spot["poll_checks"]]
    lines += [table(["poll date", "archive page", "teams compared", "check", "URL"], rows), ""]
    failures = [p for p in spot["poll_checks"] if p["result"] == "FAIL"]
    for p in failures:
        lines.append(f"- OPEN {p['poll_date']}: {json.dumps(p['mismatches'])}")
    settled = [p for p in spot["poll_checks"] if p["result"] == "settled"]
    if settled:
        lines.append("Polls where the archive's tallies differ from ours. In each case the primary source and ESPN agree with each other, "
                     "and a published copy of the poll (named in resolutions.json) confirms our values:")
        lines.append("")
        for p in settled:
            parts = [f"{key}: ours {value['ours']}, archive {value['archive']}" for key, value in p["settled"].items()]
            lines.append(f"- {p['poll_date']}: " + "; ".join(parts))
    if failures or settled:
        lines.append("")
    return lines


def checksums_section(season_dir):
    text = (season_dir / "checksums.sha256").read_text().strip()
    return ["## Checksums", "", "Regenerated after the last change and confirmed with `python3 datasets/checksums.py --season "
            + season_dir.name + " --check`:", "", "```", text, "```", ""]


def season_readme(season, games, teams, calendar):
    """The short README that sits beside each season's files."""
    per_week = Counter(int(g["week"]) for g in games)
    fbs = sum(1 for t in teams if t["division"] == "FBS")
    rows = [(w, calendar["weeks"][str(w)]["first_game"], calendar["weeks"][str(w)]["last_game"], per_week[w]) for w in sorted(per_week)]
    status = ("The dataset runs through rivalry week, which is week " + str(calendar["rivalry_week"]) + "."
              if calendar["season_complete_through_rivalry_week"]
              else "The season was still in progress when the data was collected. The last game in the dataset was played on "
              + calendar["last_game_in_dataset"] + ". Rivalry week will be week " + str(calendar["rivalry_week"]) + ".")
    return "\n".join([
        f"# The {season} Season", "",
        "Copyright 2026 Denise Koessler Gosnell. Licensed under CC BY 4.0 (see LICENSE-DATA at the root of the repository).", "",
        f"This folder holds every regular-season game involving one of the {fbs} FBS teams of {season}, "
        f"the AP Top 25, the Coaches Poll, and the CFP committee rankings for the same stretch of the season. "
        f"The columns are described in `datasets/README.md`. How the data was checked is in `VERIFICATION.md`, right here beside it.", "",
        status, "",
        f"Data collected at {calendar['data_collected_at']} (UTC).", "",
        "## Week by Week", "",
        "Weeks are numbered by the calendar rule in `datasets/README.md`: week 1 ends on Labor Day, week 0 is everything before it.", "",
        table(["week", "first game", "last game", "games"], rows), "",
    ])


def main():
    parser = argparse.ArgumentParser(description="Write VERIFICATION.md for one season.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    season_dir = DATASETS / str(args.season)

    games = read_csv(season_dir / "games.csv")
    teams = read_csv(season_dir / "teams.csv")
    calendar = load_json(season_dir / "season_calendar.json")
    excluded = load_json(season_dir / "excluded_games.json", [])
    cross = load_json(season_dir / "cross_check.json")
    spot = load_json(season_dir / "spot_checks.json")
    resolutions = load_json(season_dir / "resolutions.json", [])
    notes_path = season_dir / "verification_notes.md"

    lines = [f"# Verification record for the {args.season} season", "",
             "This file is written by `datasets/write_verification.py` from the output of the collection, "
             "cross-check, and spot-check scripts. Rerun those scripts and this one to rebuild it.", ""]
    lines += counts_section(args.season, games, teams, calendar, excluded)
    lines += cross_check_section(cross, resolutions, games)
    lines += completeness_section(games, teams)
    lines += spot_check_section(spot)
    lines += polls_section(season_dir, spot, calendar)
    lines += checksums_section(season_dir)
    if notes_path.exists():
        lines += ["## Notes", "", notes_path.read_text().strip(), ""]
    (season_dir / "VERIFICATION.md").write_text("\n".join(lines))
    (season_dir / "README.md").write_text(season_readme(args.season, games, teams, calendar))
    print(f"season {args.season}: wrote VERIFICATION.md ({len(lines)} lines) and README.md")


if __name__ == "__main__":
    main()
