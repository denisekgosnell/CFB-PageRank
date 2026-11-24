# CFB-PageRank

A graph model and ranking of Division I college football teams. Because humans introduce bias.

Think about the last time you argued about a college football ranking. Somebody had a case built on wins, somebody else had a case built on who those wins came against, and the poll that settled it was a vote. This repository asks a narrower question with no voters in it: if the only thing we know is who beat whom, how does a ranking computed from the graph of results compare with the one people vote on, and how many weeks does it take for the two to start to agree?

Everything needed to look into that question is here, in the order the work was done.

1. `datasets/` holds every regular-season game for 2023, 2024, 2025, and 2026 (year to date), plus the weekly AP Top 25, Coaches Poll, and CFP committee rankings. Every game was checked against three sources.
2. `graph_model/` turns the games into a graph with one sentence as its schema: `Team loses_to Team`. The date, the week, and the score sit on each edge.
3. `pagerank/` computes PageRank on that graph, written from scratch, one week at a time, unweighted and weighted by margin of victory.
4. `analysis/` lines each weekly PageRank up with the poll released the same week and measures the distance between them. It also holds the PageRank top 25 for the 2026 season as of the data cutoff.
5. `visualization/` has one page per season with a slider: drag it across the weeks and watch the ranking move.

Each directory has its own README that explains its piece the way we would at a whiteboard: start from the question, show the data, show the shape, walk through one example. Each one also has a verification record. Accuracy was the first requirement of this work, so every step either runs a test or writes down how it was checked.

## The Question, Precisely

A team that loses a game points to the team that beat it. Run PageRank on that graph and credit flows from losers to winners, and from winners to the teams that beat them. Snapshot the graph after each week of the season and you get a weekly ranking with no vote in it. The comparison tables in `analysis/` put that ranking beside the human polls, week by week, for four seasons. The tables are measurements. The conclusions are left to the reader.

## Running It Yourself

The scripts use the Python standard library only (Python 3.11 or newer). The tests need `pytest`, `networkx`, and `scipy`, which are listed in `requirements.txt`.

```
make all      rebuild everything downstream of datasets/, no network needed
make test     run the test suite
make data     collect and verify the raw datasets again (needs the network and an API key)
```

`run_all.sh` does the same as `make all` without make. `CONTRIBUTING.md` explains how to add a season.

## What Is Where

| directory | what it holds | how it was checked |
| --- | --- | --- |
| `datasets/` | Games, teams, and polls per season. | Every game and poll row against ESPN by id, a sample of games and every AP poll against NCAA.com and College Poll Archive by name, and a written record per season. |
| `graph_model/` | The schema figure, the graph files, and the translation scripts. | Eight translation checks per season, plus ten edges per season checked against NCAA.com. |
| `pagerank/` | The algorithm and the weekly result tables. | A hand-computed toy graph, and every weekly snapshot against networkx. |
| `analysis/` | The comparison tables and the 2026 top 25. | Rank correlations against scipy, and every table row recomputed. |
| `visualization/` | One interactive page per season. | Opened in a headless browser with the slider, the mode toggle, the search box, and both views exercised. |
| `tests/` | The test suite, including the voice check that keeps the prose in one register. | `make test` |

## How to Cite

If you use this repository, its data, or its results, please cite it.

> Gosnell, Denise Koessler. *CFB-PageRank: a graph model and PageRank ranking of Division I college football*. 2026. https://github.com/denisekgosnell/CFB-PageRank

```
@software{gosnell_cfb_pagerank_2026,
  author = {Gosnell, Denise Koessler},
  title = {CFB-PageRank: a graph model and PageRank ranking of Division I college football},
  year = {2026},
  url = {https://github.com/denisekgosnell/CFB-PageRank}
}
```

`CITATION.cff` holds the same information in a form that GitHub and reference managers read.

## License

Copyright 2026 Denise Koessler Gosnell.

The source code is licensed under the Apache License, Version 2.0 (`LICENSE`). Everything that is not source code (the datasets, the graph files, the result tables, the figures, and the documentation) is licensed under the Creative Commons Attribution 4.0 International License (`LICENSE-DATA`). Either way, reuse requires attribution. `NOTICE` lists the data sources and the one third-party library included in the repository.
