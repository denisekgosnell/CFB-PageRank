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
"""Prove that one season's graph is a complete and exact translation of its games.

Eight checks, each printed as pass or fail. The script exits with status 1
if any check fails, so it can gate the rest of the pipeline.

What it reads
    datasets/<season>/games.csv and teams.csv
    graph_model/<season>/vertices.csv and edges.csv

What it writes
    graph_model/<season>/verify_graph_output.txt   the same lines it prints

How to run it
    python3 graph_model/verify_graph.py --season 2024
"""

import argparse
import csv
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rebuild_game(edge, games_by_id):
    """Turn an edge back into the games.csv row it came from, for the round trip.

    The edge does not say which team was at home, so the home and away
    columns are taken from the original row and the rest is rebuilt from
    the edge alone.
    """
    original = games_by_id[edge["game_id"]]
    winner_at_home = original["home_team"] == edge["target"]
    return {
        "game_id": edge["game_id"],
        "season": original["season"],
        "week": edge["week"],
        "game_date": edge["game_date"],
        "home_team": edge["target"] if winner_at_home else edge["source"],
        "away_team": edge["source"] if winner_at_home else edge["target"],
        "home_score": edge["winner_score"] if winner_at_home else edge["loser_score"],
        "away_score": edge["loser_score"] if winner_at_home else edge["winner_score"],
        "winner": edge["target"],
        "loser": edge["source"],
        "margin": edge["margin"],
        "neutral_site": edge["neutral_site"],
        "conference_game": original["conference_game"],
        "overtime": original["overtime"],
        "source": original["source"],
    }


def run_checks(games, teams, vertices, edges):
    """Return a list of (name, passed, detail) for the eight checks."""
    games_by_id = {g["game_id"]: g for g in games}
    edge_ids = [e["game_id"] for e in edges]
    vertex_names = {v["team"] for v in vertices}
    team_names = {t["team"] for t in teams}
    results = []

    results.append(("1. edge count equals game count", len(edges) == len(games), f"{len(edges)} edges, {len(games)} games"))

    missing = set(games_by_id) - set(edge_ids)
    extra = set(edge_ids) - set(games_by_id)
    once = len(edge_ids) == len(set(edge_ids))
    results.append(("2. every game id appears exactly once in the edges, and vice versa",
                    not missing and not extra and once, f"missing {len(missing)}, extra {len(extra)}, duplicates {len(edge_ids) - len(set(edge_ids))}"))

    bad_direction = [e["game_id"] for e in edges if e["game_id"] in games_by_id and (
        e["source"] != games_by_id[e["game_id"]]["loser"] or e["target"] != games_by_id[e["game_id"]]["winner"]
        or int(e["winner_score"]) <= int(e["loser_score"]))]
    results.append(("3. every edge runs from the loser to the winner with winner_score > loser_score", not bad_direction, f"{len(bad_direction)} wrong"))

    bad_property = []
    for e in edges:
        g = games_by_id.get(e["game_id"])
        if g is None:
            continue
        expected = {"game_date": g["game_date"], "week": g["week"], "margin": g["margin"], "neutral_site": g["neutral_site"],
                    "winner_score": str(max(int(g["home_score"]), int(g["away_score"]))),
                    "loser_score": str(min(int(g["home_score"]), int(g["away_score"])))}
        for key, value in expected.items():
            if str(e[key]) != value:
                bad_property.append((e["game_id"], key))
    results.append(("4. every edge property equals the matching column in games.csv", not bad_property, f"{len(bad_property)} wrong"))

    results.append(("5. the vertex set equals the team set", vertex_names == team_names,
                    f"{len(vertex_names - team_names)} vertices not in teams.csv, {len(team_names - vertex_names)} teams without a vertex"))

    endpoints = {e["source"] for e in edges} | {e["target"] for e in edges}
    results.append(("6. every edge endpoint is a vertex", endpoints <= vertex_names, f"{len(endpoints - vertex_names)} unknown endpoints"))

    loops = [e["game_id"] for e in edges if e["source"] == e["target"]]
    results.append(("7. no self-loops", not loops, f"{len(loops)} self-loops"))

    columns = list(games[0].keys()) if games else []
    rebuilt = {e["game_id"]: rebuild_game(e, games_by_id) for e in edges if e["game_id"] in games_by_id}
    differences = sum(1 for gid, g in games_by_id.items() if gid not in rebuilt or any(str(rebuilt[gid][c]) != str(g[c]) for c in columns))
    results.append(("8. rebuilding games.csv from the edges reproduces every row", differences == 0 and len(rebuilt) == len(games), f"{differences} rows differ"))
    return results


def main():
    parser = argparse.ArgumentParser(description="Verify the graph for one season.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    data_dir = REPO / "datasets" / str(args.season)
    graph_dir = REPO / "graph_model" / str(args.season)

    results = run_checks(read_csv(data_dir / "games.csv"), read_csv(data_dir / "teams.csv"),
                         read_csv(graph_dir / "vertices.csv"), read_csv(graph_dir / "edges.csv"))
    lines = [f"season {args.season}"]
    for name, passed, detail in results:
        lines.append(f"  {'pass' if passed else 'FAIL'}  {name} ({detail})")
    text = "\n".join(lines)
    print(text)
    (graph_dir / "verify_graph_output.txt").write_text(text + "\n")
    if not all(passed for _, passed, _ in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
