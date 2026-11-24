# Datasets

Every ranking in this repository starts here. Before we can ask the graph a single question, we need the full record of who played whom, on what day, and what the final score was. This directory holds that record for the 2023, 2024, 2025, and 2026 regular seasons, along with the weekly human polls that we compare against in `analysis/`.

The data in this directory is licensed under Creative Commons Attribution 4.0 (see `LICENSE-DATA` at the root of the repository). Copyright 2026 Denise Koessler Gosnell.

## What Is in Each Season Folder

Each season folder holds the same set of files.

| file | what it holds |
| --- | --- |
| `games.csv` | One row per regular-season game with at least one FBS team in it. This is the file the graph model is built from. |
| `teams.csv` | One row per team that appears in `games.csv`: every FBS team, plus the FCS teams that played one. |
| `ap_poll.csv` | The AP Top 25, one row per poll per team, from the preseason poll through the poll released after rivalry week. |
| `coaches_poll.csv` | The Coaches Poll, same shape. |
| `cfp_rankings.csv` | The College Football Playoff committee rankings for the weeks they exist, same shape minus the vote counts. |
| `espn_games.csv`, `espn_polls.csv` | ESPN's view of the same games and polls. We keep them so the test suite can rerun the cross-check without downloading anything. |
| `season_calendar.json` | The week windows, rivalry week, the poll cutoff, and when the data was collected. |
| `excluded_games.json` | Every game with an FBS team that we left out, and why. |
| `resolutions.json` | The handful of values where our first two sources disagreed and a third source settled it. |
| `cross_check.json`, `spot_checks.json` | The raw output of the two verification scripts. |
| `checksums.sha256`, `metadata.json` | A SHA-256 for every CSV file, and who compiled the data, when, and from where. |
| `VERIFICATION.md` | The human-readable verification record for the season. Start here if you want to know how much to trust a number. |

## The Columns in games.csv

| column | type | meaning |
| --- | --- | --- |
| `game_id` | string | The primary source's id for the game. ESPN uses the same id, which is what makes the cross-check exact. |
| `season` | int | The year the season started. |
| `week` | int | The week number by our calendar rule, explained below. |
| `game_date` | string | The calendar date of the game in US Eastern time, written as `YYYY-MM-DD`. |
| `home_team`, `away_team` | string | The canonical team names from `teams.csv`. For a neutral-site game, "home" is the designated home team. |
| `home_score`, `away_score` | int | The final score. |
| `winner`, `loser` | string | The same two teams, sorted by who won. These two columns become the direction of the edge in the graph. |
| `margin` | int | The winner's score minus the loser's score. Always positive. |
| `neutral_site` | bool | `true` when the game was played at a neutral site. |
| `conference_game` | bool | `true` when both teams were in the same conference and the game counted in the conference standings. |
| `overtime` | bool | `true` when the game went past four quarters. |
| `source` | string | Always `cfbd`, the short name of the primary source. |

Booleans are written as the words `true` and `false`.

The columns in `teams.csv` are `team`, `team_id`, `conference`, `division` (`FBS` or `FCS`), and `season`. The columns in the poll files are `season`, `poll_week`, `source_week`, `poll_date`, `rank`, `team`, and, for the two voted polls, `points` and `first_place_votes`.

## How We Number the Weeks

The week is the unit that the PageRank snapshots and the visualizations step through, so it has to mean the same thing everywhere. We do not take the week number from our sources, because they file the late-August games under week 1 and that leaves no room for a Week 0. Instead we compute the week from the calendar:

1. Week 1 is the Tuesday-through-Monday window that ends on Labor Day.
2. Week 0 is every game played before that window.
3. Each later week is the next Tuesday-through-Monday window.
4. Rivalry week is the week that holds the Saturday after Thanksgiving.

Labor Day is the first Monday of September and Thanksgiving is the fourth Thursday of November, so both are computed, never looked up. Each season's README lists the exact dates every week covered.

A poll's `poll_week` is the number of game weeks that had been played when the poll came out. The preseason poll is week 0. The poll released on the Tuesday after Labor Day is week 1, and so on. The `source_week` column keeps the week number the primary source used, for reference only. Nothing downstream reads it. The comparison in `analysis/` lines polls up with games by `poll_date`, never by week number.

## What We Left Out

The regular season, through rivalry week, is the whole scope. Conference championship games, bowl games, and the College Football Playoff are not here. Games that were scheduled and never played are not here either. Every one of these is listed in `excluded_games.json` with its reason.

FCS teams appear only as opponents of FBS teams. A game between two FCS teams is not collected, and FCS teams never appear in a ranking table. They are in the graph, though, because a loss to an FCS team is still a loss.

The 2026 season was still being played when this data was collected. Its folder holds every game completed by the time stamp in its `season_calendar.json`, and its README says which week that reaches.

## How We Checked the Data

Three sources, each checked against the others.

1. The College Football Data API is the primary source. Every row in every CSV file comes from it.
2. ESPN is the cross-check. It shares game ids and team ids with the primary source, so every game is looked up by id and compared field by field: date, both teams, both scores, and the three flags. Every poll row is compared the same way. The comparison runs in `cross_check.py` and again, from the committed `espn_games.csv` and `espn_polls.csv`, in `tests/test_datasets.py`.
3. NCAA.com and College Poll Archive are the third source. They share no ids with the other two, so games are matched on the date, the scores, and the team names. Twenty-five games per season are drawn at random with a fixed seed, every game of the season's final AP top 10 is added, and each one is checked against NCAA.com with the URL recorded. The same script also matches every other game of the season and reports the totals. Every AP poll in the dataset is checked against College Poll Archive rank by rank.

When two sources disagreed, a third one decided, and the decision went into `resolutions.json` with the URL that settled it. In every season, the disagreements were about whether a game at an alternate venue counts as neutral, whether two independents can play a conference game, which team was the designated home team at a neutral site, and a few vote tallies. Not one score, date, winner, or loser disagreed anywhere. The full list is in each season's `VERIFICATION.md`.

## Rebuilding the Datasets

The scripts run in this order. Only the first one needs the network.

```
python3 datasets/collect.py --season 2024
python3 datasets/build_datasets.py --season 2024
python3 datasets/cross_check.py --season 2024
python3 datasets/spot_check.py --season 2024
python3 datasets/checksums.py --season 2024
python3 datasets/write_verification.py --season 2024
```

`make data` runs the same sequence for every season. The sources, the endpoints, and the access dates are in `SOURCES.md`. The map from every spelling of a team name in the other sources to our canonical name is in `aliases.csv`.
