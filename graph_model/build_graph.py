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
"""Translate one season's games into the graph: a team that loses points to the team that won.

The whole model is one sentence: Team loses_to Team. Every row in games.csv
becomes one loses_to edge from the loser to the winner, and every team in
teams.csv becomes one Team vertex, whether or not it has lost yet.

What it reads
    datasets/<season>/games.csv
    datasets/<season>/teams.csv

What it writes
    graph_model/<season>/vertices.csv   one row per Team vertex
    graph_model/<season>/edges.csv      one row per loses_to edge
    graph_model/<season>/graph.graphml  the same graph for tools such as Gephi

How to run it
    python3 graph_model/build_graph.py --season 2024

Nothing is filtered here. If a game should not be in the graph, it should
not be in games.csv.
"""

import argparse
import csv
from pathlib import Path
from xml.sax.saxutils import escape

REPO = Path(__file__).resolve().parent.parent

VERTEX_COLUMNS = ["team", "conference", "division"]
EDGE_COLUMNS = ["source", "target", "game_id", "game_date", "week", "winner_score", "loser_score", "margin", "neutral_site"]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, columns):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def vertex_rows(teams):
    """One Team vertex per row of teams.csv, in name order."""
    return [{"team": t["team"], "conference": t["conference"], "division": t["division"]}
            for t in sorted(teams, key=lambda t: t["team"])]


def edge_row(game):
    """One loses_to edge for one game. The source is the loser, the target is the winner."""
    winner_score = max(int(game["home_score"]), int(game["away_score"]))
    loser_score = min(int(game["home_score"]), int(game["away_score"]))
    return {
        "source": game["loser"],
        "target": game["winner"],
        "game_id": game["game_id"],
        "game_date": game["game_date"],
        "week": game["week"],
        "winner_score": winner_score,
        "loser_score": loser_score,
        "margin": game["margin"],
        "neutral_site": game["neutral_site"],
    }


def graphml(vertices, edges):
    """Write the graph as GraphML by hand so the script stays standard-library only."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">',
             '  <key id="conference" for="node" attr.name="conference" attr.type="string"/>',
             '  <key id="division" for="node" attr.name="division" attr.type="string"/>']
    for column in EDGE_COLUMNS[2:]:
        kind = "int" if column in ("week", "winner_score", "loser_score", "margin") else "string"
        lines.append(f'  <key id="{column}" for="edge" attr.name="{column}" attr.type="{kind}"/>')
    lines.append('  <graph id="loses_to" edgedefault="directed">')
    for vertex in vertices:
        lines.append(f'    <node id="{escape(vertex["team"], {chr(34): "&quot;"})}">')
        lines.append(f'      <data key="conference">{escape(vertex["conference"])}</data>')
        lines.append(f'      <data key="division">{escape(vertex["division"])}</data>')
        lines.append("    </node>")
    for edge in edges:
        lines.append(f'    <edge id="{edge["game_id"]}" source="{escape(edge["source"], {chr(34): "&quot;"})}" '
                     f'target="{escape(edge["target"], {chr(34): "&quot;"})}">')
        for column in EDGE_COLUMNS[2:]:
            lines.append(f'      <data key="{column}">{escape(str(edge[column]))}</data>')
        lines.append("    </edge>")
    lines += ["  </graph>", "</graphml>", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Build the loses_to graph for one season.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()

    games = read_csv(REPO / "datasets" / str(args.season) / "games.csv")
    teams = read_csv(REPO / "datasets" / str(args.season) / "teams.csv")
    out_dir = REPO / "graph_model" / str(args.season)
    out_dir.mkdir(parents=True, exist_ok=True)

    vertices = vertex_rows(teams)
    edges = [edge_row(game) for game in sorted(games, key=lambda g: (g["game_date"], g["game_id"]))]

    write_csv(out_dir / "vertices.csv", vertices, VERTEX_COLUMNS)
    write_csv(out_dir / "edges.csv", edges, EDGE_COLUMNS)
    (out_dir / "graph.graphml").write_text(graphml(vertices, edges), encoding="utf-8")

    dangling = sum(1 for v in vertices if v["team"] not in {e["source"] for e in edges})
    print(f"season {args.season}: read {len(games)} games and {len(teams)} teams")
    print(f"  wrote {len(vertices)} vertices and {len(edges)} edges to {out_dir}")
    print(f"  {dangling} vertices have no outgoing edge (no loss yet)")


if __name__ == "__main__":
    main()
