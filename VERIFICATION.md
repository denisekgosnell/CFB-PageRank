# Verification record for the repository

Each directory has its own record: `datasets/VERIFICATION.md` and one per season under `datasets/<season>/`, one per season under `graph_model/<season>/`, and the test files under `tests/` for `pagerank/` and `analysis/`. This file holds the checks that cover the repository as a whole. They were run on 2026-11-24, and run again the same day after the PageRank start value was set to 100 points per team and the preseason snapshot and the per-poll scorecards were added.

## Rebuild from a fresh clone with the network disabled

A fresh clone of `main` was made in a scratch folder, the API key variable was left unset, and the proxy variables were pointed at an address that answers nothing. Then `make all` ran, followed by `git status` to see whether any rebuilt file differed from what is committed, and `make test`.

```
$ git rev-parse --short HEAD
d86e2ba

$ env -u CFBD_API_KEY HTTPS_PROXY=http://127.0.0.1:9 HTTP_PROXY=http://127.0.0.1:9 make all
season 2023 unweighted: 15 snapshots (preseason plus weeks 0..13), 857 games in the last one, 133 ranked teams
season 2023 weighted: 15 snapshots (preseason plus weeks 0..13), 857 games in the last one, 133 ranked teams
season 2024 unweighted: 16 snapshots (preseason plus weeks 0..14), 863 games in the last one, 134 ranked teams
season 2024 weighted: 16 snapshots (preseason plus weeks 0..14), 863 games in the last one, 134 ranked teams
season 2025 unweighted: 16 snapshots (preseason plus weeks 0..14), 878 games in the last one, 136 ranked teams
season 2025 weighted: 16 snapshots (preseason plus weeks 0..14), 878 games in the last one, 136 ranked teams
season 2026 unweighted: 14 snapshots (preseason plus weeks 0..12), 822 games in the last one, 138 ranked teams
season 2026 weighted: 14 snapshots (preseason plus weeks 0..12), 822 games in the last one, 138 ranked teams
python3 analysis/build_prediction.py --season 2026
exit 0

$ git status --short   (empty means every rebuilt file is byte-for-byte what is committed)
(end of status)

$ make test
........................................................................ [ 94%]
..............................................                           [100%]
838 passed in 3.06s
```

An empty `git status` means every derived file in the repository (the graph files, the PageRank tables and snapshots, the comparison tables, the scorecards, the prediction, and the pages) is exactly what the scripts produce from the datasets.

## The test suite

`make test` runs 838 tests in six files.

| file | what it covers |
| --- | --- |
| `tests/test_headers.py` | every source file carries the ownership header; the license, notice, and citation files name the owner |
| `tests/test_datasets.py` | the dataset columns, the week rule, team membership, the ESPN cross-check from the committed tables, the polls, and the checksums |
| `tests/test_graph_model.py` | the eight translation checks for every season and the GraphML export |
| `tests/test_pagerank.py` | a hand-computed toy graph, a graph with no edges (every team keeps 100 points and ties for first), every snapshot against networkx, and the result tables against the snapshots |
| `tests/test_analysis.py` | the rank correlations against scipy, every comparison row recomputed, every scorecard cell, the side-by-side pages, and the prediction against each poll |
| `tests/test_voice.py` | the voice rules below |

## The voice pass

First pass, 2026-11-24: 121 files scanned by `tests/test_voice.py` (every Markdown file, the docstrings and comments of every Python file, and the text of every page). Rewrites made: 10 (two sentences in the top-level README, three in the visualization README, two lines of text in the verification writer, two page headings in the comparison script, and one character in the test file itself).

Second pass, 2026-11-24, after the 100-point change: 127 files scanned, no rewrites needed.

The banned patterns live in `tests/voice_banlist.txt`, with a comment naming the source each group came from. Six sources from 2025 and 2026 were read for the list: Wikipedia's guide to the signs of AI writing, Pangram's data-backed list of tells, Plus AI's list of overused words and phrases, Grammarly's list of common AI words and transitions, a PCWorld column from June 2026 on which habits read as machine-written, and the COLING 2025 paper by Juzek and Ward on lexical overrepresentation. Words that the author uses in her own book are marked `allow:` in the list with the chapter and the phrase where she uses them.

The test fails on an em dash or an en dash anywhere, on any banned pattern, on a sentence that opens with a summary word, on more than one single-word list of three per file, on a heading with a colon or a stock title, and on any mention of a language model by name or of a machine author. Every one of its checks passes.

## Repository-wide search for a machine author

A whole-word, case-sensitive `git grep` for the names of language models and the words that would mark a machine author matches only these lines, which are part of the Apache License text itself:

```
LICENSE:32
LICENSE:114
```

Nothing else in the repository matches.

## Ownership

`tests/test_headers.py` passes: every `.py`, `.sh`, `.html`, `.svg`, and `.js` file and the `Makefile` carry the header, and `LICENSE`, `NOTICE`, and `CITATION.cff` name Denise Koessler Gosnell. The one third-party file, `visualization/lib/d3.v7.min.js`, keeps its own license beside it and is named in `NOTICE`.

## Commits

The co-author trailer setting (`includeCoAuthoredBy`) is turned off in the repository's committed tool settings file. Every commit on `main` carries only its subject line, as `git log` shows:

```
d86e2ba Denise Koessler Gosnell: Start every team at 100 points, add the preseason snapshot and per-poll scorecards

c96ef31 Denise Koessler Gosnell: Publish the site with GitHub Pages

e10ec6a Denise Koessler Gosnell: Name the settings file without its path in the verification record

3acec40 Denise Koessler Gosnell: Add the final verification record

26a20c1 Denise Koessler Gosnell: Documentation and voice pass

bdd451c Denise Koessler Gosnell: Add interactive week-by-week visualizations

1ef3c3f Denise Koessler Gosnell: Add poll comparison tables and 2026 prediction

f1b1cf1 Denise Koessler Gosnell: Add PageRank implementation and weekly results

adee680 Denise Koessler Gosnell: Add graph model, schema drawing, and translation verification

a8b5c1a Denise Koessler Gosnell: Add 2026 games and polls with verification

ff9f9bb Denise Koessler Gosnell: Add 2025 games and polls with verification

a5e5523 Denise Koessler Gosnell: Add 2024 games and polls with verification

f28e5b4 Denise Koessler Gosnell: Add 2023 games and polls with verification

df7a862 Denise Koessler Gosnell: Add dataset collection and verification scripts

4fe94e4 Denise Koessler Gosnell: Initialize repository: license, notice, citation, layout

1d8734e Denise Koessler Gosnell: Turn off co-author trailers in commit messages
```

The build instructions were never committed: `git ls-files` lists no instruction file.

## What is settled by a third source

Every disagreement between the first two data sources, and every place where the third source disagreed with both, is listed in the season records under `datasets/<season>/VERIFICATION.md` with the value kept and the URL that settled it. Across the four seasons, no score, no date, no winner, and no loser disagreed in any source. The disagreements were venue flags for home games played away from the usual stadium, the conference flag for games between two independents, one home-team designation at a neutral site, one first-place vote, and the point tallies of six AP polls in the archive.

## The 2026 cutoff

The 2026 records were collected at 2026-11-24T19:35:09Z. The last game in the dataset was played on 2026-11-21, the end of week 12. Rivalry week had not been played, and the CFP committee ranking of 2026-11-24 had not been released, so `analysis/2026_prediction/` holds the PageRank top 25 through week 12 checked against the AP Poll and the Coaches Poll of 2026-11-22 and the CFP ranking of 2026-11-17.
