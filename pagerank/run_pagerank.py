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
"""Run PageRank on one season's graph, one week at a time.

The first snapshot is the preseason: no games, every team holding 100
credit points, every team tied for first. Then, for each week w from the
first week in the data through the last, the graph is built from every
edge with week <= w, PageRank runs, and the FBS teams are ranked. That
gives one snapshot per week, which is what the result tables, the
comparison, and the visualizations read. The preseason snapshot is stored
as week -1 and labeled "preseason" everywhere a person reads it.

Two modes:
    unweighted   every edge has weight 1
    weighted     every edge has weight min(margin, cap); cap 0 means no cap

What it reads
    graph_model/<season>/vertices.csv and edges.csv

What it writes
    pagerank/<season>/<mode>_results.csv      the wide table: team, conference,
                                              then rank and score for each week
    pagerank/<season>/<mode>_results.md       the same table, rendered
    pagerank/<season>/snapshots/<mode>_week_<w>.json
                                              one file per week with the full
                                              ranking and the games added

How to run it
    python3 pagerank/run_pagerank.py --season 2024 --mode unweighted
    python3 pagerank/run_pagerank.py --season 2024 --mode weighted --cap 28
"""

import argparse
import csv
import json
from pathlib import Path

from pagerank import START_VALUE, pagerank, rank

REPO = Path(__file__).resolve().parent.parent

DAMPING = 0.85
TOLERANCE = 1e-10
MAX_ITERATIONS = 1000
DEFAULT_CAP = 28
PRESEASON = -1


def week_label(week):
    """How a week is named in the tables: "preseason" for the snapshot before any game."""
    return "preseason" if week == PRESEASON else f"week_{week}"


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def edge_weight(edge, mode, cap):
    """The weight of one loses_to edge in the chosen mode."""
    if mode == "unweighted":
        return 1.0
    margin = int(edge["margin"])
    return float(min(margin, cap)) if cap > 0 else float(margin)


def snapshot(season, mode, cap, week, vertices, edges, eligible, conferences):
    """Run PageRank on the edges through one week and package the result."""
    weighted = [(e["source"], e["target"], edge_weight(e, mode, cap)) for e in edges]
    scores, iterations, converged = pagerank(vertices, weighted, DAMPING, TOLERANCE, MAX_ITERATIONS)
    # Round first, then rank, so the ranks in the snapshot follow from the
    # scores in the snapshot and anyone can rebuild one from the other.
    scores = {team: round(score, 10) for team, score in scores.items()}
    ranked = rank(scores, eligible)
    return {
        "season": season, "mode": mode, "cap": cap if mode == "weighted" else None, "week": week,
        "label": week_label(week),
        "games_in_snapshot": len(edges), "iterations": iterations, "converged": converged,
        "damping": DAMPING, "tolerance": TOLERANCE, "start_value": START_VALUE,
        "rankings": [{"rank": r, "team": team, "conference": conferences[team], "score": score} for r, team, score in ranked],
        "games_added_this_week": [{"game_id": e["game_id"], "game_date": e["game_date"], "loser": e["source"], "winner": e["target"],
                                   "winner_score": int(e["winner_score"]), "loser_score": int(e["loser_score"])}
                                  for e in edges if int(e["week"]) == week],
    }


def wide_table(snapshots, eligible, conferences):
    """One row per FBS team: rank and score in every week, sorted by the final week."""
    weeks = [s["week"] for s in snapshots]
    by_week = {s["week"]: {r["team"]: r for r in s["rankings"]} for s in snapshots}
    final = by_week[weeks[-1]]
    rows = []
    for team in sorted(eligible, key=lambda t: (final[t]["rank"], t)):
        row = {"team": team, "conference": conferences[team]}
        for week in weeks:
            row[f"{week_label(week)}_rank"] = by_week[week][team]["rank"]
            row[f"{week_label(week)}_score"] = f"{by_week[week][team]['score']:.6f}"
        rows.append(row)
    columns = ["team", "conference"] + [f"{week_label(w)}_{kind}" for w in weeks for kind in ("rank", "score")]
    return rows, columns


def markdown_table(rows, columns, heading):
    lines = [heading, "", "| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row[c]) for c in columns) + " |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Run PageRank week by week for one season.")
    parser.add_argument("--season", type=int, required=True)
    parser.add_argument("--mode", choices=["unweighted", "weighted"], required=True)
    parser.add_argument("--cap", type=int, default=DEFAULT_CAP, help="margin cap for the weighted mode; 0 means no cap")
    args = parser.parse_args()

    graph_dir = REPO / "graph_model" / str(args.season)
    out_dir = REPO / "pagerank" / str(args.season)
    (out_dir / "snapshots").mkdir(parents=True, exist_ok=True)

    vertex_rows = read_csv(graph_dir / "vertices.csv")
    edges = read_csv(graph_dir / "edges.csv")
    vertices = [v["team"] for v in vertex_rows]
    conferences = {v["team"]: v["conference"] for v in vertex_rows}
    eligible = [v["team"] for v in vertex_rows if v["division"] == "FBS"]

    weeks = sorted({int(e["week"]) for e in edges})
    snapshots = []
    # The preseason snapshot first: no edges, so every team holds the start value.
    for week in [PRESEASON] + list(range(weeks[0], weeks[-1] + 1)):
        through = [e for e in edges if int(e["week"]) <= week]
        snap = snapshot(args.season, args.mode, args.cap, week, vertices, through, eligible, conferences)
        snapshots.append(snap)
        (out_dir / "snapshots" / f"{args.mode}_{week_label(week)}.json").write_text(json.dumps(snap, indent=1) + "\n")

    rows, columns = wide_table(snapshots, eligible, conferences)
    with (out_dir / f"{args.mode}_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    last = snapshots[-1]
    cap_note = f", margin capped at {args.cap}" if args.mode == "weighted" and args.cap else (", raw margin" if args.mode == "weighted" else "")
    heading = (f"# {args.season} PageRank, {args.mode}{cap_note}\n\n"
               f"Season {args.season}, {args.mode} mode. Data through week {last['week']} ({last['games_in_snapshot']} games). "
               f"Every team starts the preseason with {START_VALUE:.0f} credit points and is tied for first; the pool stays at "
               f"{START_VALUE:.0f} points per vertex all season, FCS opponents included, so 100 means average. "
               f"Damping {DAMPING}, tolerance {TOLERANCE}, at most {MAX_ITERATIONS} iterations; "
               f"the final week converged in {last['iterations']} iterations. "
               f"Ranks are competition ranks (tied teams share a rank).")
    (out_dir / f"{args.mode}_results.md").write_text(markdown_table(rows, columns, heading))

    print(f"season {args.season} {args.mode}: {len(snapshots)} snapshots (preseason plus weeks {weeks[0]}..{weeks[-1]}), "
          f"{last['games_in_snapshot']} games in the last one, {len(eligible)} ranked teams")
    first = snapshots[0]["rankings"]
    print(f"  preseason: every team at {first[0]['score']:.0f} points, {sum(1 for r in first if r['rank'] == 1)} of {len(first)} tied for first")
    print("  top 5 at the end: " + ", ".join(f"{r['rank']}. {r['team']} ({r['score']:.2f})" for r in last["rankings"][:5]))


if __name__ == "__main__":
    main()
