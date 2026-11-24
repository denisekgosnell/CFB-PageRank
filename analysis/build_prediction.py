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
"""Write the PageRank top 25 for the season in progress, as of the data cutoff.

This is the PageRank-only ranking for the current season, checked against
each human poll in the dataset: for every team in the PageRank top 25, the
table says where the AP Poll, the Coaches Poll, and the CFP committee put
that team and whether the rank is an exact match. The PageRank columns are
computed from games alone.

What it reads
    datasets/<season>/season_calendar.json, ap_poll.csv, coaches_poll.csv, cfp_rankings.csv
    pagerank/<season>/snapshots/<mode>_week_<last>.json

What it writes
    analysis/<season>_prediction/prediction.csv
    analysis/<season>_prediction/prediction.md

How to run it
    python3 analysis/build_prediction.py --season 2026
"""

import argparse
import csv
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MODES = ["unweighted", "weighted"]
POLLS = [("ap", "ap_poll.csv", "AP Poll"), ("coaches", "coaches_poll.csv", "Coaches Poll"), ("cfp", "cfp_rankings.csv", "CFP rankings")]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def latest_poll(rows):
    """The most recent release in a poll file: (date, {team: rank}). Empty if the file is empty."""
    if not rows:
        return "", {}
    release = max(row["poll_date"] for row in rows)
    return release, {row["team"]: int(row["rank"]) for row in rows if row["poll_date"] == release}


def columns_for(mode):
    out = [f"{mode}_team", f"{mode}_score"]
    for short, _, _ in POLLS:
        out += [f"{mode}_{short}_rank", f"{mode}_{short}_match"]
    return out


def main():
    parser = argparse.ArgumentParser(description="Write the PageRank top 25 for the season in progress.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    season = args.season
    data_dir = REPO / "datasets" / str(season)
    snapshot_dir = REPO / "pagerank" / str(season) / "snapshots"
    out_dir = REPO / "analysis" / f"{season}_prediction"
    out_dir.mkdir(parents=True, exist_ok=True)

    calendar = json.loads((data_dir / "season_calendar.json").read_text())
    last_week = max(int(path.stem.split("_")[-1]) for path in snapshot_dir.glob("unweighted_week_*.json"))
    snapshots = {mode: json.loads((snapshot_dir / f"{mode}_week_{last_week}.json").read_text()) for mode in MODES}
    polls = {short: latest_poll(read_csv(data_dir / file_name)) for short, file_name, _ in POLLS}

    rows = []
    for i in range(25):
        row = {"rank": i + 1}
        for mode in MODES:
            team = snapshots[mode]["rankings"][i]
            row[f"{mode}_team"] = team["team"]
            row[f"{mode}_score"] = f"{team['score']:.2f}"
            for short, _, _ in POLLS:
                _, ranks = polls[short]
                poll_rank = ranks.get(team["team"])
                row[f"{mode}_{short}_rank"] = poll_rank if poll_rank is not None else ("unranked" if ranks else "")
                row[f"{mode}_{short}_match"] = ("yes" if poll_rank == team["rank"] else "no") if ranks else ""
        for short, _, _ in POLLS:
            _, ranks = polls[short]
            by_rank = {r: t for t, r in ranks.items()}
            row[f"{short}_team"] = by_rank.get(i + 1, "")
        rows.append(row)
    columns = ["rank"] + [c for mode in MODES for c in columns_for(mode)] + [f"{short}_team" for short, _, _ in POLLS]
    with (out_dir / "prediction.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    games = snapshots["unweighted"]["games_in_snapshot"]
    poll_notes = ", ".join(f"the {title} released {polls[short][0]}" for short, _, title in POLLS if polls[short][0])
    missing = [title for short, _, title in POLLS if not polls[short][0]]
    lines = [f"# {season} PageRank top 25 as of the data cutoff", "",
             f"Data cutoff: the records were collected at {calendar['data_collected_at']} (UTC). "
             f"The last game in the dataset was played on {calendar['last_game_in_dataset']}, which is week {last_week}. "
             f"The snapshot holds {games} games. Rivalry week (week {calendar['rivalry_week']}) had not been played.", "",
             "The PageRank columns come from games alone: the unweighted graph, and the weighted graph with the margin capped at 28. "
             "Every team started the preseason with 100 credit points, and the pool stays at 100 points per vertex, so a score of 100 is average. "
             "Ranks are competition ranks, so tied teams share a number.", "",
             f"Each PageRank top 25 is checked against the most recent human rankings in the dataset: {poll_notes}. "
             "A match is an exact match of rank. A team the poll did not rank is marked unranked."
             + (f" No {' or '.join(missing)} had been released." if missing else "")
             + " No ranking released after the data cutoff is included.", ""]
    for mode in MODES:
        lines += [f"## PageRank, {mode}", "",
                  "| rank | team | score | AP rank | AP match | Coaches rank | Coaches match | CFP rank | CFP match |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for row in rows:
            cells = [row["rank"], row[f"{mode}_team"], row[f"{mode}_score"]]
            for short, _, _ in POLLS:
                cells += [row[f"{mode}_{short}_rank"], row[f"{mode}_{short}_match"]]
            lines.append("| " + " | ".join(str(c) for c in cells) + " |")
        lines.append("")
    lines += ["## How many did PageRank get right", "",
              "| poll | release | unweighted: exact rank matches | unweighted: teams in the poll's top 25 | weighted: exact rank matches | weighted: teams in the poll's top 25 |",
              "| --- | --- | --- | --- | --- | --- |"]
    for short, _, title in POLLS:
        release, ranks = polls[short]
        if not ranks:
            lines.append(f"| {title} | not released | | | | |")
            continue
        cells = [title, release]
        for mode in MODES:
            cells.append(sum(1 for row in rows if row[f"{mode}_{short}_match"] == "yes"))
            cells.append(sum(1 for row in rows if row[f"{mode}_{short}_rank"] not in ("unranked", "")))
        lines.append("| " + " | ".join(str(c) for c in cells) + " |")
    lines += ["", "## The human rankings, for reference", "",
              "| rank | " + " | ".join(f"{title} {polls[short][0] or '(none)'}" for short, _, title in POLLS) + " |",
              "| --- | --- | --- | --- |"]
    for row in rows:
        lines.append("| " + " | ".join([str(row["rank"])] + [row[f"{short}_team"] for short, _, _ in POLLS]) + " |")
    lines.append("")
    (out_dir / "prediction.md").write_text("\n".join(lines))
    print(f"season {season}: wrote the top 25 as of week {last_week} ({games} games) checked against "
          + ", ".join(f"{short} {polls[short][0] or 'none'}" for short, _, _ in POLLS))


if __name__ == "__main__":
    main()
