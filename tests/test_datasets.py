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
"""Tests for the datasets: internal consistency, the week rule, and the cross-check.

What these tests read
    datasets/<season>/games.csv, teams.csv, the three poll files,
    season_calendar.json, resolutions.json, espn_games.csv, espn_polls.csv,
    and checksums.sha256.

What they do not need
    The raw cache under datasets/_raw. The ESPN comparison runs against
    espn_games.csv and espn_polls.csv, which cross_check.py wrote from the
    raw cache and which are committed with the datasets.

Run them with: python3 -m pytest tests/test_datasets.py
"""

import csv
import hashlib
import json
from datetime import date, timedelta
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
DATASETS = REPO / "datasets"
SEASONS = [2023, 2024, 2025, 2026]

GAME_COLUMNS = [
    "game_id", "season", "week", "game_date", "home_team", "away_team",
    "home_score", "away_score", "winner", "loser", "margin",
    "neutral_site", "conference_game", "overtime", "source",
]

# The number of FBS programs each season, from the membership changes
# recorded in datasets/VERIFICATION.md (2023: 133; Kennesaw State joined
# in 2024; Delaware and Missouri State in 2025; North Dakota State and
# Sacramento State in 2026).
EXPECTED_FBS_TEAMS = {2023: 133, 2024: 134, 2025: 136, 2026: 138}


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load(season, name):
    return read_csv(DATASETS / str(season) / name)


def calendar(season):
    return json.loads((DATASETS / str(season) / "season_calendar.json").read_text())


def resolutions(season):
    path = DATASETS / str(season) / "resolutions.json"
    return json.loads(path.read_text()) if path.exists() else []


# ---------------------------------------------------------------------------
# The week rule, written again here from the words in the README so the
# test does not share code with the script it checks.
# ---------------------------------------------------------------------------

def first_monday_of_september(season):
    day = date(season, 9, 1)
    while day.weekday() != 0:
        day += timedelta(days=1)
    return day


def fourth_thursday_of_november(season):
    day = date(season, 11, 1)
    while day.weekday() != 3:
        day += timedelta(days=1)
    return day + timedelta(weeks=3)


def expected_week(game_day, season):
    week_one_tuesday = first_monday_of_september(season) - timedelta(days=6)
    if game_day < week_one_tuesday:
        return 0
    return 1 + (game_day - week_one_tuesday).days // 7


# ---------------------------------------------------------------------------
# games.csv
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("season", SEASONS)
def test_games_have_the_documented_columns(season):
    with (DATASETS / str(season) / "games.csv").open(newline="", encoding="utf-8") as handle:
        header = next(csv.reader(handle))
    assert header == GAME_COLUMNS


@pytest.mark.parametrize("season", SEASONS)
def test_every_game_row_is_internally_consistent(season):
    seen = set()
    for row in load(season, "games.csv"):
        assert row["game_id"] not in seen, f"duplicate game id {row['game_id']}"
        seen.add(row["game_id"])
        home, away = int(row["home_score"]), int(row["away_score"])
        assert home != away, f"tie score in {row['game_id']}"
        winner = row["home_team"] if home > away else row["away_team"]
        loser = row["away_team"] if home > away else row["home_team"]
        assert row["winner"] == winner and row["loser"] == loser
        assert int(row["margin"]) == abs(home - away)
        assert row["home_team"] != row["away_team"]
        assert int(row["season"]) == season
        for flag in ("neutral_site", "conference_game", "overtime"):
            assert row[flag] in ("true", "false")


@pytest.mark.parametrize("season", SEASONS)
def test_week_numbers_follow_the_calendar_rule(season):
    rows = load(season, "games.csv")
    for row in rows:
        assert int(row["week"]) == expected_week(date.fromisoformat(row["game_date"]), season), row["game_id"]
    rivalry_saturday = fourth_thursday_of_november(season) + timedelta(days=2)
    rivalry_week = expected_week(rivalry_saturday, season)
    assert calendar(season)["rivalry_week"] == rivalry_week
    assert max(int(row["week"]) for row in rows) <= rivalry_week
    first = min(rows, key=lambda r: r["game_date"])
    assert int(first["week"]) == 0, "every season here opens with Week 0 games"


@pytest.mark.parametrize("season", SEASONS)
def test_every_team_in_a_game_is_in_teams_csv(season):
    teams = {row["team"]: row for row in load(season, "teams.csv")}
    for row in load(season, "games.csv"):
        assert row["home_team"] in teams and row["away_team"] in teams
        assert "FBS" in (teams[row["home_team"]]["division"], teams[row["away_team"]]["division"])
    fbs = [row for row in teams.values() if row["division"] == "FBS"]
    assert len(fbs) == EXPECTED_FBS_TEAMS[season]
    assert len({row["team_id"] for row in teams.values()}) == len(teams), "team ids must be unique"


@pytest.mark.parametrize("season", SEASONS)
def test_every_fbs_team_played_at_least_once(season):
    played = set()
    for row in load(season, "games.csv"):
        played.update((row["home_team"], row["away_team"]))
    for row in load(season, "teams.csv"):
        if row["division"] == "FBS":
            assert row["team"] in played, row["team"]


# ---------------------------------------------------------------------------
# The cross-check against ESPN, rerun from the committed ESPN tables
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("season", SEASONS)
def test_games_agree_with_espn_except_where_a_third_source_settled_it(season):
    team_ids = {row["team"]: row["team_id"] for row in load(season, "teams.csv")}
    espn = {row["game_id"]: row for row in load(season, "espn_games.csv")}
    settled = {(r.get("game_id"), r["field"]) for r in resolutions(season)}
    for row in load(season, "games.csv"):
        other = espn[row["game_id"]]
        assert team_ids[row["home_team"]] == other["home_team_id"] or (row["game_id"], "home_team") in settled
        assert team_ids[row["away_team"]] == other["away_team_id"] or (row["game_id"], "away_team") in settled
        for field in ("game_date", "home_score", "away_score", "neutral_site", "conference_game", "overtime"):
            assert row[field] == other[field] or (row["game_id"], field) in settled, (row["game_id"], field)


@pytest.mark.parametrize("season", SEASONS)
def test_no_completed_espn_game_with_an_fbs_team_is_missing(season):
    fbs_ids = {row["team_id"] for row in load(season, "teams.csv") if row["division"] == "FBS"}
    have = {row["game_id"] for row in load(season, "games.csv")}
    last_day = calendar(season)["last_game_in_dataset"]
    for row in load(season, "espn_games.csv"):
        if row["completed"] != "true" or row["game_date"] > last_day:
            continue
        if row["home_team_id"] in fbs_ids or row["away_team_id"] in fbs_ids:
            assert row["game_id"] in have, row


# ---------------------------------------------------------------------------
# The polls
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("season", SEASONS)
@pytest.mark.parametrize("file_name,short", [("ap_poll.csv", "ap"), ("coaches_poll.csv", "coaches"), ("cfp_rankings.csv", "cfp")])
def test_polls_are_complete_and_agree_with_espn(season, file_name, short):
    rows = load(season, file_name)
    fbs = {row["team"] for row in load(season, "teams.csv") if row["division"] == "FBS"}
    espn = {}
    for row in load(season, "espn_polls.csv"):
        if row["poll"] == short:
            espn.setdefault(row["poll_date"], set()).add((row["team"], int(row["rank"])))
    settled = {(r.get("poll_date"), r.get("team"), r["field"]) for r in resolutions(season)}
    by_date = {}
    for row in rows:
        by_date.setdefault(row["poll_date"], []).append(row)
    for released, poll in by_date.items():
        ranks = sorted(int(r["rank"]) for r in poll)
        if len(poll) == 26:
            # Two teams tied for 25th. The AP lists both.
            assert ranks[-2:] == [25, 25], released
        else:
            assert len(poll) == 25, released
        for row in poll:
            assert row["team"] in fbs, row
        assert {(r["team"], int(r["rank"])) for r in poll} == espn[released], released
    dates = sorted(by_date)
    weeks = [int(by_date[d][0]["poll_week"]) for d in dates]
    assert weeks == sorted(weeks), "poll weeks must not decrease as release dates increase"


@pytest.mark.parametrize("season", SEASONS)
def test_poll_week_counts_the_game_weeks_played_before_the_release(season):
    games = load(season, "games.csv")
    for file_name in ("ap_poll.csv", "coaches_poll.csv", "cfp_rankings.csv"):
        for row in load(season, file_name):
            before = [int(g["week"]) for g in games if g["game_date"] < row["poll_date"]]
            assert int(row["poll_week"]) == (max(before) if before else 0), (file_name, row["poll_date"])


# ---------------------------------------------------------------------------
# Checksums
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("season", SEASONS)
def test_checksums_match_the_files(season):
    season_dir = DATASETS / str(season)
    stored = {}
    for line in (season_dir / "checksums.sha256").read_text().splitlines():
        digest, name = line.split("  ")
        stored[name] = digest
    for path in season_dir.glob("*.csv"):
        assert stored[path.name] == hashlib.sha256(path.read_bytes()).hexdigest(), path.name
    assert set(stored) == {path.name for path in season_dir.glob("*.csv")}
