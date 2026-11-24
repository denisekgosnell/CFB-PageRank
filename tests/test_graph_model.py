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
"""Tests for the graph model: the eight translation checks, rerun for every season.

What these tests read
    datasets/<season>/games.csv and teams.csv
    graph_model/<season>/vertices.csv, edges.csv, and graph.graphml

Run them with: python3 -m pytest tests/test_graph_model.py
"""

import csv
import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SEASONS = [2023, 2024, 2025, 2026]


def load_module(name, relative_path):
    spec = importlib.util.spec_from_file_location(name, REPO / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


@pytest.mark.parametrize("season", SEASONS)
def test_the_eight_translation_checks_pass(season):
    verify = load_module("verify_graph", "graph_model/verify_graph.py")
    data = REPO / "datasets" / str(season)
    graph = REPO / "graph_model" / str(season)
    results = verify.run_checks(read_csv(data / "games.csv"), read_csv(data / "teams.csv"),
                                read_csv(graph / "vertices.csv"), read_csv(graph / "edges.csv"))
    failed = [f"{name} ({detail})" for name, passed, detail in results if not passed]
    assert not failed, failed


@pytest.mark.parametrize("season", SEASONS)
def test_the_graphml_file_holds_the_same_graph(season):
    graph = REPO / "graph_model" / str(season)
    tree = ET.parse(graph / "graph.graphml")
    ns = {"g": "http://graphml.graphdrawing.org/xmlns"}
    nodes = tree.getroot().findall(".//g:node", ns)
    edges = tree.getroot().findall(".//g:edge", ns)
    assert len(nodes) == len(read_csv(graph / "vertices.csv"))
    assert len(edges) == len(read_csv(graph / "edges.csv"))
    expected = {(e["source"], e["target"], e["game_id"]) for e in read_csv(graph / "edges.csv")}
    found = {(e.get("source"), e.get("target"), e.get("id")) for e in edges}
    assert found == expected


def test_edge_row_puts_the_loser_first():
    build = load_module("build_graph", "graph_model/build_graph.py")
    game = {"game_id": "1", "game_date": "2024-09-07", "week": "1", "home_team": "Home", "away_team": "Away",
            "home_score": "14", "away_score": "21", "winner": "Away", "loser": "Home", "margin": "7", "neutral_site": "false"}
    edge = build.edge_row(game)
    assert edge["source"] == "Home" and edge["target"] == "Away"
    assert edge["winner_score"] == 21 and edge["loser_score"] == 14


def test_every_season_has_undefeated_teams_as_dangling_vertices():
    """An undefeated team has no outgoing edge. That is a feature, and PageRank has to handle it."""
    for season in SEASONS:
        graph = REPO / "graph_model" / str(season)
        losers = {e["source"] for e in read_csv(graph / "edges.csv")}
        vertices = {v["team"] for v in read_csv(graph / "vertices.csv")}
        assert vertices - losers, f"{season}: no team is undefeated, which is not what the data says"
