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
"""Point check ten edges per season against NCAA.com, and write the graph's verification record.

verify_graph.py proves that edges.csv matches games.csv. This script asks a
different question: does the edge match the world? Ten edges are drawn at
random with a fixed seed and compared with the box score on NCAA.com, which
shares no ids with our primary source. An error that made it into
games.csv and the graph together would show up here.

What it reads
    graph_model/<season>/edges.csv and verify_graph_output.txt
    datasets/<season>/teams.csv
    datasets/_raw/<season>/ncaa_scoreboard_week_*.html   (the cached pages)

What it writes
    graph_model/<season>/point_checks.json
    graph_model/<season>/VERIFICATION.md

How to run it
    python3 graph_model/point_check.py --season 2024
"""

import argparse
import csv
import importlib.util
import json
import random
import sys
from datetime import date, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RANDOM_SEED = 20261124
EDGES_TO_CHECK = 10


def load_spot_check_module():
    """Borrow the NCAA.com page parser and the name matching from datasets/spot_check.py."""
    spec = importlib.util.spec_from_file_location("spot_check", REPO / "datasets" / "spot_check.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def match(edge, contests, lookup, spot):
    """Find the NCAA.com game with the same date, scores, and teams as this edge."""
    scores = {edge["winner_score"], edge["loser_score"]}
    days = {edge["game_date"], (date.fromisoformat(edge["game_date"]) + timedelta(days=1)).isoformat()}
    for contest in contests.values():
        if contest["game_date"] not in days or {str(contest["home_score"]), str(contest["away_score"])} != scores:
            continue
        home = lookup.get(spot.normalize(contest["home_name"]))
        away = lookup.get(spot.normalize(contest["away_name"]))
        if {home, away} == {edge["source"], edge["target"]}:
            winner = home if contest["home_score"] > contest["away_score"] else away
            return contest, winner
    return None, None


def main():
    parser = argparse.ArgumentParser(description="Point check ten edges against NCAA.com.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    graph_dir = REPO / "graph_model" / str(args.season)
    raw_dir = REPO / "datasets" / "_raw" / str(args.season)
    if not raw_dir.exists():
        sys.exit("the raw cache is missing; run datasets/collect.py first")

    spot = load_spot_check_module()
    edges = read_csv(graph_dir / "edges.csv")
    lookup = spot.canonical_lookup(read_csv(REPO / "datasets" / str(args.season) / "teams.csv"))
    contests = spot.load_ncaa_contests(raw_dir)

    drawn = random.Random(RANDOM_SEED).sample(sorted(edges, key=lambda e: e["game_id"]), EDGES_TO_CHECK)
    records = []
    for edge in sorted(drawn, key=lambda e: (e["game_date"], e["game_id"])):
        contest, winner = match(edge, contests, lookup, spot)
        record = {"game_id": edge["game_id"], "edge": f"{edge['source']} loses_to {edge['target']}",
                  "edge_properties": {k: edge[k] for k in ("game_date", "week", "winner_score", "loser_score", "margin")}}
        if contest is None:
            record.update({"result": "FAIL", "ncaa": "no matching game found", "url": ""})
        else:
            loser = edge["source"] if winner == edge["target"] else edge["target"]
            ncaa_winner_score = max(contest["home_score"], contest["away_score"])
            ncaa_loser_score = min(contest["home_score"], contest["away_score"])
            ok = (winner == edge["target"] and loser == edge["source"]
                  and str(ncaa_winner_score) == edge["winner_score"] and str(ncaa_loser_score) == edge["loser_score"])
            record.update({"result": "pass" if ok else "FAIL",
                           "ncaa": f"{winner} {ncaa_winner_score}, {loser} {ncaa_loser_score} on {contest['game_date']}",
                           "url": contest["url"]})
        records.append(record)

    (graph_dir / "point_checks.json").write_text(json.dumps({"season": args.season, "random_seed": RANDOM_SEED, "checks": records}, indent=2) + "\n")

    passed = sum(1 for r in records if r["result"] == "pass")
    lines = [f"# Verification record for the {args.season} graph", "",
             "## Translation checks", "",
             "Output of `python3 graph_model/verify_graph.py --season " + str(args.season) + "`:", "", "```",
             (graph_dir / "verify_graph_output.txt").read_text().rstrip(), "```", "",
             "## Point checks against NCAA.com", "",
             f"Ten edges drawn at random with seed {RANDOM_SEED} and compared with the box score on NCAA.com, "
             "which shares no ids with the primary source. The match is made on the date, the two scores, and the two team names. "
             f"Passed: {passed} of {len(records)}.", "",
             "| edge | edge properties | NCAA.com | check | URL |", "| --- | --- | --- | --- | --- |"]
    for r in records:
        props = ", ".join(f"{k} {v}" for k, v in r["edge_properties"].items())
        lines.append(f"| {r['edge']} | {props} | {r['ncaa']} | {r['result']} | {r['url']} |")
    lines.append("")
    (graph_dir / "VERIFICATION.md").write_text("\n".join(lines))
    print(f"season {args.season}: {passed} of {len(records)} edges agree with NCAA.com")
    for r in records:
        if r["result"] != "pass":
            print("   FAIL:", r)
    if passed != len(records):
        sys.exit(1)


if __name__ == "__main__":
    main()
