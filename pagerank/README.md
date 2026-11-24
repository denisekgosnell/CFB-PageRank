# PageRank

We have a graph where every loss is an edge from the team that lost to the team that won. Now we want a number for each team that says how much credit the season's results have sent its way. That number is PageRank, and this directory computes it from scratch, one week at a time, in two flavors.

The code here is licensed under Apache 2.0 and the result tables under CC BY 4.0. Copyright 2026 Denise Koessler Gosnell.

## What PageRank Does With Our Graph

Picture a fixed pool of credit spread evenly across every team before the season starts: 100 points each, and every team tied for first. Each round, every team passes the credit it holds out along its outgoing edges. In our graph an outgoing edge is a loss, so a team passes its credit to the teams that beat it. A team splits its credit across its losses in proportion to the edge weights. Then every team's new total is damped: 85 percent of what arrived, plus an equal share of the remaining 15 percent for everyone, so no team ever drops to zero. Repeat until the numbers stop moving. The pool is the same size at the end as at the start, 100 points per vertex, so a score of 100 means exactly average and the scores always add up to 100 times the number of vertices.

Two things fall out of this that are worth seeing before you read the tables.

First, credit compounds. Beat a team that beat good teams and you collect credit that those teams collected. That is the reason to use PageRank instead of counting wins.

Second, a team with no loss has no outgoing edge. In graph terms it is a dangling vertex. It still collects credit from every team it beat, but it has nowhere to send its own. The standard treatment, and the one `pagerank.py` uses, is to spread a dangling vertex's credit evenly across every vertex in the graph each round. An undefeated team therefore keeps the credit that flows to it and gives back only the small equal share that every vertex gives back. Early in the season, when most teams are undefeated, most of the credit moves this way, and the rankings are close to flat. As losses pile up, the edges carry more and more of it.

## The Settings

| setting | value | where it lives |
| --- | --- | --- |
| start value | 100 points per vertex, before the first round | `pagerank.py` |
| damping factor | 0.85 | `run_pagerank.py` |
| convergence | stop when the total absolute change in one round is below 1e-10 of the whole pool | `run_pagerank.py` |
| iteration limit | 1000 rounds | `run_pagerank.py` |
| dangling vertices | their credit is spread evenly across every vertex | `pagerank.py` |
| ties | scores within a billionth of a point share a rank | `pagerank.py` |
| vertices | every team in `vertices.csv`, FCS opponents included | `run_pagerank.py` |
| ranked teams | FBS teams only | `run_pagerank.py` |

Every weekly snapshot records how many rounds it took to converge. The last week of 2023 took 44 rounds unweighted and 68 rounds weighted.

## Unweighted and Weighted

In the unweighted graph every edge has weight 1. A team that lost twice sends half of its credit along each loss. If a team lost to the same opponent twice, that opponent gets two shares, because there are two edges.

In the weighted graph an edge's weight is the margin of victory, capped at 28 points:

```
weight = min(margin, 28)
```

A 35-point win and a 28-point win carry the same weight. A 3-point win carries 3. The cap is there so that one blowout does not swamp a whole season of close games. The `--cap` flag on `run_pagerank.py` lets you try a different cap, and `--cap 0` uses the raw margin. The tables published here use the cap of 28.

Let's walk through one team. In 2023, Oklahoma State lost three games: to South Alabama by 26, to Iowa State by 7, and to UCF by 42. In the unweighted graph, Oklahoma State sends one third of its credit along each of the three edges. In the weighted graph the weights are 26, 7, and 28 (the UCF margin hits the cap), for a total of 61, so South Alabama receives 26/61 of what Oklahoma State sends, Iowa State receives 7/61, and UCF receives 28/61. The team on the other end of the edge decides nothing about this; the split depends only on the loser's own losses.

## Week by Week

`run_pagerank.py` builds one snapshot per week, and one before the season. The preseason snapshot has no edges at all: every team holds 100 points and every team is tied for first, which is the starting line for everything that follows. Then, for week w, the script keeps every edge with `week` less than or equal to w, runs PageRank on the whole vertex set, and ranks the FBS teams. Week 0 is the handful of late-August games, so that snapshot has a few edges and still a lot of ties. The last snapshot is rivalry week, or, for the season in progress, the last week in the data.

Ranks are competition ranks. Teams whose scores are equal to within a billionth of a point share a rank, and the next distinct score takes the rank it would have had without the tie, so a sequence can read 1, 2, 2, 4. In the preseason every team is rank 1. Expect ties in the first week or two as well.

## The Files

| file | what it holds |
| --- | --- |
| `pagerank.py` | The algorithm and the ranking rule. Two functions, no file reading, nothing beyond the standard library. |
| `run_pagerank.py` | Reads a season's graph, runs the weekly snapshots, writes the tables. |
| `<season>/unweighted_results.csv` | One row per FBS team: `team`, `conference`, then `preseason_rank` and `preseason_score`, then `week_<w>_rank` and `week_<w>_score` for every week. Rows are sorted by the final week's rank. Scores are points with six decimal places. |
| `<season>/weighted_results.csv` | The same, for the weighted graph. |
| `<season>/unweighted_results.md`, `<season>/weighted_results.md` | The same tables rendered for reading on GitHub, with the season, mode, data cutoff, game count, and convergence settings above the table. |
| `<season>/snapshots/<mode>_preseason.json`, `<season>/snapshots/<mode>_week_<w>.json` | The full ranking for one snapshot, the games added that week, and the round count. The preseason file is stored as week -1. The visualizations read these. |

## How We Know It Is Right

`tests/test_pagerank.py` checks the implementation three ways. A four-vertex graph with an answer worked out by hand in the test itself, plus a graph with no edges to confirm that every vertex keeps its 100 points and ties for first. Every snapshot of every season, in both modes, against `networkx.pagerank` with the same damping, to within 1e-8 per vertex after dividing our points by the pool. And the result tables against the snapshots they came from, including the tie rule. networkx is a test dependency only; nothing a reader runs imports it.

## Rebuilding

```
python3 pagerank/run_pagerank.py --season 2024 --mode unweighted
python3 pagerank/run_pagerank.py --season 2024 --mode weighted
```

`make pagerank` runs both modes for every season.
