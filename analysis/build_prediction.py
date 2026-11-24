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

This is the PageRank-only ranking for the current season, placed beside the
most recent human polls in the dataset for reference. The PageRank columns
are computed from games alone.

What it reads
    datasets/<season>/season_calendar.json, ap_poll.csv, cfp_rankings.csv
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
COLUMNS = ["rank", "unweighted_team", "unweighted_score", "weighted_team", "weighted_score", "ap_team", "cfp_team"]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def latest_poll(rows):
    """The rows of the most recent release in a poll file, sorted by rank. Empty if the file is empty."""
    if not rows:
        return "", []
    release = max(row["poll_date"] for row in rows)
    return release, sorted((row for row in rows if row["poll_date"] == release), key=lambda r: int(r["rank"]))


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
    snapshots = {mode: json.loads((snapshot_dir / f"{mode}_week_{last_week}.json").read_text()) for mode in ("unweighted", "weighted")}
    ap_date, ap_rows = latest_poll(read_csv(data_dir / "ap_poll.csv"))
    cfp_date, cfp_rows = latest_poll(read_csv(data_dir / "cfp_rankings.csv"))

    rows = []
    for i in range(25):
        un = snapshots["unweighted"]["rankings"][i]
        we = snapshots["weighted"]["rankings"][i]
        rows.append({
            "rank": i + 1,
            "unweighted_team": f"{un['rank']}. {un['team']}", "unweighted_score": f"{un['score']:.8f}",
            "weighted_team": f"{we['rank']}. {we['team']}", "weighted_score": f"{we['score']:.8f}",
            "ap_team": ap_rows[i]["team"] if i < len(ap_rows) else "",
            "cfp_team": cfp_rows[i]["team"] if i < len(cfp_rows) else "",
        })
    with (out_dir / "prediction.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    games = snapshots["unweighted"]["games_in_snapshot"]
    lines = [f"# {season} PageRank top 25 as of the data cutoff", "",
             f"Data cutoff: the records were collected at {calendar['data_collected_at']} (UTC). "
             f"The last game in the dataset was played on {calendar['last_game_in_dataset']}, which is week {last_week}. "
             f"The snapshot holds {games} games. Rivalry week (week {calendar['rivalry_week']}) had not been played.", "",
             "The two PageRank columns come from games alone: the unweighted graph, and the weighted graph with the margin capped at 28. "
             "Ranks are competition ranks, so tied teams share a number. Scores add up to 1 across every vertex in the graph.", "",
             f"For reference, the two right-hand columns show the most recent human rankings in the dataset: the AP poll released {ap_date} "
             + (f"and the CFP committee rankings released {cfp_date}." if cfp_date else "and no CFP committee rankings, because none had been released.") + " "
             "No CFP committee ranking released after the data cutoff is included.", "",
             "| rank | PageRank, unweighted | score | PageRank, weighted | score | AP poll " + ap_date + " | CFP rankings " + cfp_date + " |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row[c]) for c in COLUMNS) + " |")
    lines.append("")
    (out_dir / "prediction.md").write_text("\n".join(lines))
    print(f"season {season}: wrote the top 25 as of week {last_week} ({games} games); AP {ap_date}, CFP {cfp_date or 'none'}")


if __name__ == "__main__":
    main()
