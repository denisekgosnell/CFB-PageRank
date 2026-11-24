# Contributing

This repository is built to be rerun. Here is how to add a season, how to rerun the checks, and where the one secret goes.

## Adding a Season

1. Add the year to `SEASONS` in the `Makefile`, in `run_all.sh`, and in the `SEASONS` list at the top of each test file under `tests/`. Add its FBS team count to `EXPECTED_FBS_TEAMS` in `tests/test_datasets.py`, with the source for the count noted in `datasets/VERIFICATION.md`.
2. Run the collection for that season: `python3 datasets/collect.py --season 2027`. This needs the network and an API key (see below).
3. Build and check the datasets: `build_datasets.py`, `cross_check.py`, `spot_check.py`, `checksums.py`, then `write_verification.py`, each with `--season 2027`. The order is listed in `datasets/README.md`.
4. If the cross-check or the spot check reports a disagreement, find a third source, decide, and write the decision into `datasets/2027/resolutions.json` with the URL. Then rerun the build and the checks. The format is in `datasets/build_datasets.py`.
5. Write a few sentences in `datasets/2027/verification_notes.md` about anything a reader should know, and run `write_verification.py` again.
6. Run `make all` to build the graph, the PageRank tables, the comparison, and the page, then `make test`.
7. Commit the season folder under each directory in its own commit.

## Rerunning the Checks

`make test` runs every test. Each test file says at the top what it reads. None of them need the network or the raw cache under `datasets/_raw`, because the files they need are committed.

To rerun the data checks against the sources, run `datasets/collect.py` for the season first; it fills the raw cache, and `cross_check.py`, `spot_check.py`, and `graph_model/point_check.py` read from there.

## The API Key

The College Football Data API (https://collegefootballdata.com) needs a free key. `datasets/collect.py` reads it from the environment variable `CFBD_API_KEY` and sends it as a bearer token. The key is never written to disk. On a machine where a proxy attaches the key for you, leave the variable unset and the script sends plain requests.

## Writing

The READMEs are written in one voice, and `tests/test_voice.py` keeps them there. It fails on em dashes, en dashes, and a list of phrases kept in `tests/voice_banlist.txt`. If the test fails on something you wrote, rewrite the sentence rather than the list.
