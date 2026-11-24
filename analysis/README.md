# Analysis

The question this repository set out to answer is a question about time. How many weeks into a season does a ranking computed from results alone start to look like the ranking that people vote on? This directory holds the measurements. It does not hold the answer. The tables are here for you to read, and the conclusions are yours to draw.

The code here is licensed under Apache 2.0 and the tables under CC BY 4.0. Copyright 2026 Denise Koessler Gosnell.

## How a Poll Is Lined Up With a Snapshot

A poll is released after a week's games, on a Sunday for the AP and Coaches polls and on a Tuesday for the CFP committee. The fair comparison is with a PageRank snapshot that knows exactly what the voters knew. So for each poll release with date D, `compare_to_polls.py` runs PageRank on every edge whose `game_date` is before D and compares that result with the poll. The `snapshot_week` column records the last game week in that snapshot.

The preseason poll comes out before any game is played. The PageRank snapshot before it is the starting line, every team at 100 points and tied for first, so there is no ranking to compare with. Its row carries `preseason` as the snapshot week and `n/a` in every metric column, and it is left in the table to mark where the season starts.

Every comparison is made twice, once with the unweighted graph and once with the weighted graph (margin capped at 28), and against each of the three polls in the datasets: the AP Top 25, the Coaches Poll, and the CFP committee rankings for the weeks they exist.

## The Metrics

Each row of a comparison table is one poll release. The metrics are computed over the 25 teams in that poll. Where a metric says "AP" it means whichever poll the table is for.

| metric | definition |
| --- | --- |
| `top25_overlap` | Number of teams in both the AP top 25 and the PageRank top 25. |
| `top10_overlap` | Same, for the top 10. |
| `top5_overlap` | Same, for the top 5. |
| `number_one_match` | 1 if the AP number one is the PageRank number one, else 0. |
| `exact_rank_matches` | Number of the 25 AP teams whose PageRank rank equals their AP rank. |
| `spearman_top25` | Spearman rank correlation between the AP rank and the PageRank rank for the 25 AP-ranked teams. Ties in the PageRank ranks get their average rank. |
| `kendall_top25` | Kendall's tau-b for the same 25 teams. |
| `mean_abs_rank_diff_top25` | Mean of the absolute difference between the AP rank and the PageRank rank over the 25 AP-ranked teams. |
| `max_pagerank_rank_of_ap_top25` | The worst PageRank rank held by any AP top-25 team. |
| `games_in_snapshot` | Number of edges in the snapshot. |

Two more columns describe the row: `poll_week` is the poll's week in the datasets, and `snapshot_week` is the last game week the snapshot holds.

## The Scorecard

The comparison tables measure distance. The scorecard asks a blunter question for each poll: did PageRank get it right? `scorecard_<mode>.csv` has one row per poll week and one column group per poll. For each poll released that week, the group holds the release date, the number of the poll's 25 teams that PageRank placed at exactly the same rank, the number of them that PageRank had anywhere in its own top 25, and whether the two number ones agree. The three groups sit side by side, so one row shows the AP Poll, the Coaches Poll, and the CFP committee rankings for the same week. A cell is `n/a` for the preseason poll and blank in a week when that poll was not released.

The PageRank rank in every metric is a competition rank among FBS teams, so when PageRank has not separated two teams yet they share a rank. Early in the season that happens a lot, and the correlations reflect it.

## The Files

| file | what it holds |
| --- | --- |
| `<season>/comparison_unweighted.csv` | One row per AP poll release, unweighted PageRank. |
| `<season>/comparison_weighted.csv` | Same, weighted PageRank. |
| `<season>/comparison_<mode>_coaches.csv` | The same two tables against the Coaches Poll. |
| `<season>/comparison_<mode>_cfp.csv` | The same two tables against the CFP committee rankings. |
| `<season>/scorecard_<mode>.csv` | The scorecard: one row per poll week, one column group per poll. |
| `<season>/comparison.md` | All six comparison tables and both scorecards, rendered. |
| `<season>/scorecard.md` | The two scorecards on their own. |
| `<season>/top25_side_by_side_week_<N>.md` | For the AP poll of week N: the 25 AP teams with each team's PageRank rank in both modes beside it, the Coaches Poll and the CFP rankings released the same week, and the PageRank top 25 in both modes in the right-hand columns. |
| `2026_prediction/prediction.md`, `prediction.csv` | The PageRank top 25 for the season in progress, as of the data cutoff, in both modes. Beside every team: its rank in the most recent AP Poll, Coaches Poll, and CFP rankings in the dataset, and whether each one is an exact match. A summary table counts the matches per poll. |

## How We Know the Numbers Are Right

`tests/test_analysis.py` checks the Spearman and Kendall functions against `scipy.stats` on random data with ties, recomputes every row of every AP comparison table from the graph and the poll, confirms that each snapshot holds only games played before the poll's release, checks every scorecard cell against the comparison table it came from, checks that every side-by-side page lists the AP teams in order, and checks the prediction file against the final weekly snapshot and against each poll. scipy is a test dependency only.

## Rebuilding

```
python3 analysis/compare_to_polls.py --season 2024
python3 analysis/build_prediction.py --season 2026
```

`make analysis` runs both for every season.
