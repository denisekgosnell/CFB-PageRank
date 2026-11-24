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
"""Tests for the PageRank implementation.

Three kinds of check:
    1. A four-vertex toy graph with an answer worked out by hand.
    2. Every weekly snapshot of every season, in both modes, against
       networkx.pagerank with the same damping, to within 1e-8 per vertex.
       networkx is a test dependency only; the scripts never import it.
    3. The result tables agree with the snapshots they were built from.

Run them with: python3 -m pytest tests/test_pagerank.py
"""

import csv
import importlib.util
import json
from pathlib import Path

import networkx as nx
import pytest

REPO = Path(__file__).resolve().parent.parent
SEASONS = [2023, 2024, 2025, 2026]
MODES = ["unweighted", "weighted"]


def load_module(name, relative_path):
    spec = importlib.util.spec_from_file_location(name, REPO / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pr = load_module("pagerank", "pagerank/pagerank.py")


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


# ---------------------------------------------------------------------------
# 1. The toy graph
# ---------------------------------------------------------------------------

def test_toy_graph_matches_the_hand_computed_answer():
    """Four teams. A lost to B. B lost to C. C lost to A. D is undefeated and never played.

    With damping d and four vertices, the fixed point has to satisfy
        score(A) = (1-d)/4 + d*dangling/4 + d*score(C)
    and the same for B and C around the cycle, while D only receives the
    equal share and its own dangling share. By symmetry A, B, and C share
    one value s, D has value t, and 3s + t = 1. Solving with d = 0.85:
        t = (1-d)/4 + d*t/4            =>  t = 0.15 / (4 - 0.85) = 0.047619...
        s = (1 - t) / 3                 =>  s = 0.317460...
    """
    vertices = ["A", "B", "C", "D"]
    edges = [("A", "B", 1.0), ("B", "C", 1.0), ("C", "A", 1.0)]
    scores, iterations, converged = pr.pagerank(vertices, edges, damping=0.85, tolerance=1e-12)
    assert converged
    t = 0.15 / (4 - 0.85)
    s = (1 - t) / 3
    assert abs(scores["D"] - t) < 1e-9
    for team in "ABC":
        assert abs(scores[team] - s) < 1e-9
    assert abs(sum(scores.values()) - 1.0) < 1e-12


def test_weights_split_the_outgoing_credit_in_proportion():
    """A lost to B by 7 and to C by 21, so C should receive three times what B receives from A."""
    vertices = ["A", "B", "C"]
    edges = [("A", "B", 7.0), ("A", "C", 21.0)]
    scores, _, converged = pr.pagerank(vertices, edges, tolerance=1e-12)
    assert converged
    # B and C are dangling, so they pass their credit to everyone equally. The
    # only difference between B and C is what A sends them, so the gap between
    # their scores is exactly the gap in what A sends.
    from_a_to_b = 0.85 * scores["A"] * 7 / 28
    from_a_to_c = 0.85 * scores["A"] * 21 / 28
    assert abs((scores["C"] - scores["B"]) - (from_a_to_c - from_a_to_b)) < 1e-9


def test_rank_shares_a_rank_on_ties_and_skips_the_next():
    scores = {"A": 0.4, "B": 0.3, "C": 0.3, "D": 0.1 - 5e-13, "E": 0.1}
    ranked = pr.rank(scores, ["A", "B", "C", "D", "E"])
    assert [(r, v) for r, v, _ in ranked] == [(1, "A"), (2, "B"), (2, "C"), (4, "D"), (4, "E")]


# ---------------------------------------------------------------------------
# 2. Every weekly snapshot against networkx
# ---------------------------------------------------------------------------

def networkx_scores(vertices, edges):
    """The same graph in networkx, with parallel edges summed into one weight."""
    graph = nx.DiGraph()
    graph.add_nodes_from(vertices)
    for source, target, weight in edges:
        if graph.has_edge(source, target):
            graph[source][target]["weight"] += weight
        else:
            graph.add_edge(source, target, weight=weight)
    return nx.pagerank(graph, alpha=0.85, tol=1e-12, max_iter=2000, weight="weight")


@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("season", SEASONS)
def test_every_weekly_snapshot_matches_networkx(season, mode):
    graph_dir = REPO / "graph_model" / str(season)
    vertices = [v["team"] for v in read_csv(graph_dir / "vertices.csv")]
    edges = read_csv(graph_dir / "edges.csv")
    snapshot_dir = REPO / "pagerank" / str(season) / "snapshots"
    checked = 0
    for path in sorted(snapshot_dir.glob(f"{mode}_week_*.json")):
        snap = json.loads(path.read_text())
        week, cap = snap["week"], snap["cap"]
        through = [e for e in edges if int(e["week"]) <= week]
        weighted = []
        for e in through:
            weight = 1.0 if mode == "unweighted" else float(min(int(e["margin"]), cap) if cap else int(e["margin"]))
            weighted.append((e["source"], e["target"], weight))
        ours, _, converged = pr.pagerank(vertices, weighted)
        assert converged
        theirs = networkx_scores(vertices, weighted)
        for vertex in vertices:
            assert abs(ours[vertex] - theirs[vertex]) < 1e-8, (season, mode, week, vertex)
        # The stored snapshot is what we just recomputed.
        stored = {r["team"]: r["score"] for r in snap["rankings"]}
        for team, score in stored.items():
            assert abs(ours[team] - score) < 1e-9, (season, mode, week, team)
        assert snap["games_in_snapshot"] == len(through)
        checked += 1
    assert checked > 0


# ---------------------------------------------------------------------------
# 3. The result tables agree with the snapshots
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("season", SEASONS)
def test_result_table_matches_the_snapshots(season, mode):
    season_dir = REPO / "pagerank" / str(season)
    rows = {r["team"]: r for r in read_csv(season_dir / f"{mode}_results.csv")}
    fbs = {v["team"] for v in read_csv(REPO / "graph_model" / str(season) / "vertices.csv") if v["division"] == "FBS"}
    assert set(rows) == fbs
    for path in sorted((season_dir / "snapshots").glob(f"{mode}_week_*.json")):
        snap = json.loads(path.read_text())
        week = snap["week"]
        ranked = {r["team"]: r for r in snap["rankings"]}
        assert set(ranked) == fbs
        for team, record in ranked.items():
            assert int(rows[team][f"week_{week}_rank"]) == record["rank"]
            assert abs(float(rows[team][f"week_{week}_score"]) - record["score"]) < 1e-8
        # Ranks are competition ranks: sorted by score, ties share, next rank skips.
        expected = pr.rank({t: r["score"] for t, r in ranked.items()}, list(fbs))
        assert [(rk, t) for rk, t, _ in expected] == [(r["rank"], r["team"]) for r in snap["rankings"]]
