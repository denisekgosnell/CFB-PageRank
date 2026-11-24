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
"""Build the interactive page for one season: visualization/<season>/index.html.

The page is one self-contained HTML file. The weekly PageRank snapshots,
the vertices, and the edges are written into the page itself, so it works
when opened straight from disk. D3 is loaded from visualization/lib, which
is vendored in the repository.

What it reads
    graph_model/<season>/vertices.csv and edges.csv
    pagerank/<season>/snapshots/<mode>_week_<w>.json
    datasets/<season>/season_calendar.json

What it writes
    visualization/<season>/index.html

How to run it
    python3 visualization/build_pages.py --season 2024
"""

import argparse
import csv
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "page_template.html"

# Stroke colors by conference. The first four are sampled from the figures in
# The Practitioner's Guide to Graph Data; the rest are darker or lighter
# steps of the same four, plus the book's green and a gray for FCS teams.
PALETTE = ["#1F4ADE", "#FE7D2B", "#51DDBD", "#54E1FB", "#0B2A8C", "#B85A10", "#1F8F7A", "#2A8FB5", "#009D77", "#7A4DBF", "#C9A227", "#E05B5B"]
FCS_COLOR = "#B7B7B7"


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def page_data(season):
    """Everything the page needs, as one JSON-ready dict."""
    graph_dir = REPO / "graph_model" / str(season)
    snapshot_dir = REPO / "pagerank" / str(season) / "snapshots"
    calendar = json.loads((REPO / "datasets" / str(season) / "season_calendar.json").read_text())

    vertices = read_csv(graph_dir / "vertices.csv")
    edges = read_csv(graph_dir / "edges.csv")
    conferences = sorted({v["conference"] for v in vertices if v["division"] == "FBS"})
    colors = {conference: PALETTE[i % len(PALETTE)] for i, conference in enumerate(conferences)}

    snapshots = {"unweighted": {}, "weighted": {}}
    weeks = sorted({int(path.stem.split("_")[-1]) for path in snapshot_dir.glob("unweighted_week_*.json")})
    for mode in snapshots:
        for week in weeks:
            snap = json.loads((snapshot_dir / f"{mode}_week_{week}.json").read_text())
            snapshots[mode][str(week)] = {r["team"]: [r["rank"], round(r["score"], 8)] for r in snap["rankings"]}

    return {
        "season": season,
        "weeks": weeks,
        "week_windows": calendar["weeks"],
        "last_game": calendar["last_game_in_dataset"],
        "season_complete": calendar["season_complete_through_rivalry_week"],
        "collected_at": calendar["data_collected_at"],
        "vertices": [{"id": v["team"], "conference": v["conference"], "division": v["division"]} for v in vertices],
        "edges": [{"source": e["source"], "target": e["target"], "week": int(e["week"]), "date": e["game_date"],
                   "ws": int(e["winner_score"]), "ls": int(e["loser_score"])} for e in edges],
        "colors": colors,
        "fcs_color": FCS_COLOR,
        "snapshots": snapshots,
    }


def main():
    parser = argparse.ArgumentParser(description="Build the interactive page for one season.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    data = page_data(args.season)
    out_dir = REPO / "visualization" / str(args.season)
    out_dir.mkdir(parents=True, exist_ok=True)
    html = TEMPLATE.read_text(encoding="utf-8").replace("__SEASON__", str(args.season)).replace("__DATA__", json.dumps(data, separators=(",", ":")))
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"season {args.season}: wrote {out_dir / 'index.html'} with {len(data['vertices'])} vertices, {len(data['edges'])} edges, weeks {data['weeks'][0]}..{data['weeks'][-1]}")


if __name__ == "__main__":
    main()
