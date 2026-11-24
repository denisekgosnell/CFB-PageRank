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
"""Compare the PageRank rankings with the human polls, one poll release at a time.

A poll comes out after a week's games. The honest comparison uses the
PageRank snapshot built from every game played before the poll's release
date, so for each poll row with release date D this script runs PageRank
on every edge with game_date < D and compares the result with the poll.
The preseason poll has no games before it and is reported with no metrics.

Every number here is a measurement. There is no interpretation in this
file or in the tables it writes.

What it reads
    datasets/<season>/ap_poll.csv, coaches_poll.csv, cfp_rankings.csv
    graph_model/<season>/vertices.csv and edges.csv

What it writes
    analysis/<season>/comparison_<mode>.csv            against the AP poll
    analysis/<season>/comparison_<mode>_coaches.csv    against the Coaches Poll
    analysis/<season>/comparison_<mode>_cfp.csv        against the CFP rankings
    analysis/<season>/comparison.md                    every table, rendered
    analysis/<season>/top25_side_by_side_week_<N>.md   one per AP poll

How to run it
    python3 analysis/compare_to_polls.py --season 2024
"""

import argparse
import csv
import importlib.util
import math
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

MODES = ["unweighted", "weighted"]
CAP = 28
POLLS = [("ap", "ap_poll.csv", "AP Top 25"), ("coaches", "coaches_poll.csv", "Coaches Poll"), ("cfp", "cfp_rankings.csv", "CFP committee rankings")]
METRIC_COLUMNS = ["poll_date", "poll_week", "snapshot_week", "games_in_snapshot", "top25_overlap", "top10_overlap", "top5_overlap",
                  "number_one_match", "spearman_top25", "kendall_top25", "mean_abs_rank_diff_top25", "max_pagerank_rank_of_ap_top25"]


def load_pagerank_module():
    spec = importlib.util.spec_from_file_location("pagerank", REPO / "pagerank" / "pagerank.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pr = load_pagerank_module()


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, columns):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------------
# Rank correlations, in plain Python. tests/test_analysis.py checks them
# against scipy.
# ---------------------------------------------------------------------------

def average_ranks(values):
    """Rank a list of numbers from 1, giving tied values the average of their positions."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        average = (i + j + 2) / 2.0
        for k in range(i, j + 1):
            ranks[order[k]] = average
        i = j + 1
    return ranks


def pearson(xs, ys):
    n = len(xs)
    mean_x, mean_y = sum(xs) / n, sum(ys) / n
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    var_x = sum((x - mean_x) ** 2 for x in xs)
    var_y = sum((y - mean_y) ** 2 for y in ys)
    if var_x == 0 or var_y == 0:
        return float("nan")
    return cov / math.sqrt(var_x * var_y)


def spearman(xs, ys):
    """Spearman's rank correlation: Pearson on the average ranks."""
    return pearson(average_ranks(xs), average_ranks(ys))


def kendall_tau_b(xs, ys):
    """Kendall's tau-b, which accounts for ties in either list."""
    n = len(xs)
    concordant = discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            dx = xs[i] - xs[j]
            dy = ys[i] - ys[j]
            product = dx * dy
            if product > 0:
                concordant += 1
            elif product < 0:
                discordant += 1
    pairs = n * (n - 1) / 2
    ties_x = sum(c * (c - 1) / 2 for c in count_values(xs).values())
    ties_y = sum(c * (c - 1) / 2 for c in count_values(ys).values())
    denominator = math.sqrt((pairs - ties_x) * (pairs - ties_y))
    if denominator == 0:
        return float("nan")
    return (concordant - discordant) / denominator


def count_values(values):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


# ---------------------------------------------------------------------------
# Snapshots and metrics
# ---------------------------------------------------------------------------

def snapshot_before(release_date, mode, vertices, edges, eligible):
    """PageRank on every edge played before the release date. Returns (ranked rows, edge count, last week)."""
    before = [e for e in edges if e["game_date"] < release_date]
    weighted = []
    for e in before:
        weight = 1.0 if mode == "unweighted" else float(min(int(e["margin"]), CAP))
        weighted.append((e["source"], e["target"], weight))
    scores, _, converged = pr.pagerank(vertices, weighted)
    if not converged:
        raise SystemExit(f"PageRank did not converge for the snapshot before {release_date}")
    ranked = pr.rank(scores, eligible)
    last_week = max((int(e["week"]) for e in before), default=None)
    return ranked, len(before), last_week


def metrics(poll_rows, ranked):
    """The comparison numbers for one poll release against one PageRank snapshot."""
    pagerank_rank = {team: r for r, team, _ in ranked}
    poll_rank = {row["team"]: int(row["rank"]) for row in poll_rows}
    poll_teams = sorted(poll_rank, key=lambda t: poll_rank[t])
    top = lambda n: {team for r, team, _ in ranked if r <= n}
    xs = [poll_rank[t] for t in poll_teams]
    ys = [pagerank_rank[t] for t in poll_teams]
    number_one = [team for r, team, _ in ranked if r == 1]
    return {
        "top25_overlap": len(set(poll_teams) & top(25)),
        "top10_overlap": len({t for t in poll_teams if poll_rank[t] <= 10} & top(10)),
        "top5_overlap": len({t for t in poll_teams if poll_rank[t] <= 5} & top(5)),
        "number_one_match": 1 if poll_teams[0] in number_one else 0,
        "spearman_top25": f"{spearman(xs, ys):.4f}",
        "kendall_top25": f"{kendall_tau_b(xs, ys):.4f}",
        "mean_abs_rank_diff_top25": f"{sum(abs(x - y) for x, y in zip(xs, ys)) / len(xs):.2f}",
        "max_pagerank_rank_of_ap_top25": max(ys),
    }


def compare(poll_rows_by_date, mode, vertices, edges, eligible):
    """One metrics row per poll release, plus the ranked snapshot used for each."""
    rows, snapshots = [], {}
    for release_date in sorted(poll_rows_by_date):
        poll_rows = poll_rows_by_date[release_date]
        ranked, game_count, last_week = snapshot_before(release_date, mode, vertices, edges, eligible)
        snapshots[release_date] = ranked
        row = {"poll_date": release_date, "poll_week": poll_rows[0]["poll_week"],
               "snapshot_week": last_week if last_week is not None else "", "games_in_snapshot": game_count}
        if game_count == 0:
            row.update({column: "n/a" for column in METRIC_COLUMNS[4:]})
        else:
            row.update(metrics(poll_rows, ranked))
        rows.append(row)
    return rows, snapshots


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def table(columns, rows):
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row[c]) for c in columns) + " |")
    return "\n".join(lines)


def side_by_side(season, release_date, poll_rows, snapshots_by_mode):
    """The AP top 25 beside the two PageRank top 25s for one poll release."""
    poll_rows = sorted(poll_rows, key=lambda r: int(r["rank"]))
    rank_of = {mode: {team: r for r, team, _ in ranked} for mode, ranked in snapshots_by_mode.items()}
    top_of = {mode: [(r, team) for r, team, _ in ranked if r <= 25] for mode, ranked in snapshots_by_mode.items()}
    lines = [f"# AP poll of {release_date} beside PageRank, {season} season", "",
             f"PageRank is computed from every game played before {release_date}. "
             "Beside each AP team is its PageRank rank in each mode. The two right-hand columns list the PageRank top 25 in each mode.", "",
             "| rank | AP team | PageRank rank, unweighted | PageRank rank, weighted | PageRank top 25, unweighted | PageRank top 25, weighted |",
             "| --- | --- | --- | --- | --- | --- |"]
    max_rows = max(len(poll_rows), len(top_of["unweighted"]), len(top_of["weighted"]))
    for i in range(max_rows):
        ap = poll_rows[i] if i < len(poll_rows) else None
        un = top_of["unweighted"][i] if i < len(top_of["unweighted"]) else None
        we = top_of["weighted"][i] if i < len(top_of["weighted"]) else None
        lines.append("| " + " | ".join([
            str(i + 1),
            ap["team"] if ap else "",
            str(rank_of["unweighted"][ap["team"]]) if ap else "",
            str(rank_of["weighted"][ap["team"]]) if ap else "",
            f"{un[0]}. {un[1]}" if un else "",
            f"{we[0]}. {we[1]}" if we else "",
        ]) + " |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Compare PageRank with the human polls for one season.")
    parser.add_argument("--season", type=int, required=True)
    args = parser.parse_args()
    season = args.season
    data_dir = REPO / "datasets" / str(season)
    graph_dir = REPO / "graph_model" / str(season)
    out_dir = REPO / "analysis" / str(season)
    out_dir.mkdir(parents=True, exist_ok=True)

    vertex_rows = read_csv(graph_dir / "vertices.csv")
    vertices = [v["team"] for v in vertex_rows]
    eligible = [v["team"] for v in vertex_rows if v["division"] == "FBS"]
    edges = read_csv(graph_dir / "edges.csv")

    rendered = [f"# PageRank against the human polls, {season} season", "",
                "Each row is one poll release. The PageRank snapshot for a row holds every game played before the poll's release date. "
                "The preseason poll has no games before it, so its metrics are n/a. The metrics are defined in `analysis/README.md`.", ""]
    ap_snapshots = {}
    for short, file_name, title in POLLS:
        poll_rows_by_date = {}
        for row in read_csv(data_dir / file_name):
            poll_rows_by_date.setdefault(row["poll_date"], []).append(row)
        if not poll_rows_by_date:
            continue
        for mode in MODES:
            rows, snapshots = compare(poll_rows_by_date, mode, vertices, edges, eligible)
            suffix = "" if short == "ap" else f"_{short}"
            write_csv(out_dir / f"comparison_{mode}{suffix}.csv", rows, METRIC_COLUMNS)
            rendered += [f"## {title}, {mode} PageRank", "", table(METRIC_COLUMNS, rows), ""]
            if short == "ap":
                ap_snapshots[mode] = snapshots
        if short == "ap":
            for release_date, poll_rows in sorted(poll_rows_by_date.items()):
                week = poll_rows[0]["poll_week"]
                page = side_by_side(season, release_date, poll_rows, {mode: ap_snapshots[mode][release_date] for mode in MODES})
                (out_dir / f"top25_side_by_side_week_{week}.md").write_text(page)
    (out_dir / "comparison.md").write_text("\n".join(rendered))
    print(f"season {season}: wrote comparison tables for {len(POLLS)} polls and {len(MODES)} modes to {out_dir}")


if __name__ == "__main__":
    main()
