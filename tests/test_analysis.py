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
"""Tests for the comparison with the human polls.

    1. The plain-Python rank correlations against scipy.stats, on random
       data with ties and on the real comparison rows.
    2. Every comparison row, recomputed from the graph and the poll.
    3. The side-by-side pages and the prediction file line up with the data.

scipy is a test dependency only. Run with: python3 -m pytest tests/test_analysis.py
"""

import csv
import importlib.util
import json
import random
from pathlib import Path

import pytest
from scipy import stats

REPO = Path(__file__).resolve().parent.parent
SEASONS = [2023, 2024, 2025, 2026]
MODES = ["unweighted", "weighted"]


def load_module(name, relative_path):
    spec = importlib.util.spec_from_file_location(name, REPO / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cmp = load_module("compare_to_polls", "analysis/compare_to_polls.py")


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


# ---------------------------------------------------------------------------
# 1. Rank correlations
# ---------------------------------------------------------------------------

def test_spearman_and_kendall_match_scipy_on_random_data_with_ties():
    rng = random.Random(7)
    for _ in range(50):
        xs = list(range(1, 26))
        ys = [rng.randint(1, 40) for _ in xs]
        assert abs(cmp.spearman(xs, ys) - stats.spearmanr(xs, ys).statistic) < 1e-12
        assert abs(cmp.kendall_tau_b(xs, ys) - stats.kendalltau(xs, ys).statistic) < 1e-12


def test_average_ranks_handle_ties():
    assert cmp.average_ranks([10, 20, 20, 30]) == [1.0, 2.5, 2.5, 4.0]


# ---------------------------------------------------------------------------
# 2. Every comparison row, recomputed
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("season", SEASONS)
def test_every_ap_comparison_row_can_be_recomputed(season, mode):
    graph_dir = REPO / "graph_model" / str(season)
    vertex_rows = read_csv(graph_dir / "vertices.csv")
    vertices = [v["team"] for v in vertex_rows]
    eligible = [v["team"] for v in vertex_rows if v["division"] == "FBS"]
    edges = read_csv(graph_dir / "edges.csv")
    polls = {}
    for row in read_csv(REPO / "datasets" / str(season) / "ap_poll.csv"):
        polls.setdefault(row["poll_date"], []).append(row)
    stored = read_csv(REPO / "analysis" / str(season) / f"comparison_{mode}.csv")
    assert [r["poll_date"] for r in stored] == sorted(polls)
    for row in stored:
        ranked, game_count, last_week = cmp.snapshot_before(row["poll_date"], mode, vertices, edges, eligible)
        assert int(row["games_in_snapshot"]) == game_count
        assert row["snapshot_week"] == ("" if last_week is None else str(last_week))
        if game_count == 0:
            assert row["spearman_top25"] == "n/a"
            continue
        expected = cmp.metrics(polls[row["poll_date"]], ranked)
        for key, value in expected.items():
            assert str(row[key]) == str(value), (season, mode, row["poll_date"], key)
        # The snapshot holds only games before the release date, and at least one game from the week before it.
        assert all(e["game_date"] < row["poll_date"] for e in edges if int(e["week"]) <= last_week)
        # Spearman stays inside [-1, 1] and the overlaps inside their ranges.
        assert -1.0 <= float(row["spearman_top25"]) <= 1.0
        assert 0 <= int(row["top25_overlap"]) <= 25 and 0 <= int(row["top10_overlap"]) <= 10 and 0 <= int(row["top5_overlap"]) <= 5


# ---------------------------------------------------------------------------
# 3. The pages beside the tables
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("season", SEASONS)
def test_one_side_by_side_page_per_ap_poll(season):
    polls = {}
    for row in read_csv(REPO / "datasets" / str(season) / "ap_poll.csv"):
        polls.setdefault(row["poll_date"], row["poll_week"])
    for release, week in polls.items():
        page = (REPO / "analysis" / str(season) / f"top25_side_by_side_week_{week}.md").read_text()
        assert release in page.splitlines()[0]
        # Twenty-five AP rows, each naming the AP team at that rank.
        ap_rows = sorted((r for r in read_csv(REPO / "datasets" / str(season) / "ap_poll.csv") if r["poll_date"] == release), key=lambda r: int(r["rank"]))
        table_rows = [line for line in page.splitlines() if line.startswith("| ") and line.split("|")[1].strip().isdigit()]
        for i, ap in enumerate(ap_rows[:25]):
            assert table_rows[i].split("|")[2].strip() == ap["team"]


def test_prediction_matches_the_last_snapshot():
    out = REPO / "analysis" / "2026_prediction"
    rows = read_csv(out / "prediction.csv")
    assert len(rows) == 25
    snapshot_dir = REPO / "pagerank" / "2026" / "snapshots"
    last_week = max(int(p.stem.split("_")[-1]) for p in snapshot_dir.glob("unweighted_week_*.json"))
    for mode in MODES:
        snap = json.loads((snapshot_dir / f"{mode}_week_{last_week}.json").read_text())
        for i, row in enumerate(rows):
            expected = snap["rankings"][i]
            assert row[f"{mode}_team"] == f"{expected['rank']}. {expected['team']}"
            assert abs(float(row[f"{mode}_score"]) - expected["score"]) < 1e-8
    ap = read_csv(REPO / "datasets" / "2026" / "ap_poll.csv")
    latest = max(r["poll_date"] for r in ap)
    top = sorted((r for r in ap if r["poll_date"] == latest), key=lambda r: int(r["rank"]))
    assert [r["ap_team"] for r in rows] == [r["team"] for r in top[:25]]
    assert latest in (out / "prediction.md").read_text()
