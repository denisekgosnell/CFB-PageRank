# Verification record for the datasets directory

Each season has its own record in `datasets/<season>/VERIFICATION.md`. This file
holds the checks that apply to the directory as a whole.

## Preflight

The network checks from the build environment, run before any collection and
again after the last collection on 2026-11-24:

```
2026-11-24T19:55:41Z
cfbd 200
espn 200
ncaa 200
ap 403
```

The College Football Data API answered with data and no key in the request,
which shows the environment attached the key. ESPN and NCAA.com answered. The AP
hub page answers a plain request with 403 from its own bot protection; the
poll spot checks use College Poll Archive and published copies of each poll
instead, as recorded in each season's file.

School athletics sites (for example arkansasrazorbacks.com, msuspartans.com,
kuathletics.com) could not be resolved from the build environment, so the
tie-breakers for venue flags came from NCAA.com game pages and Wikipedia season
pages, named in each season's `resolutions.json`.

## FBS membership

The number of FBS teams in each season's `teams.csv` against two independent
counts: the membership changes reported when each school moved up, and the
team count in the infobox of Wikipedia's season page.

| season | FBS teams in teams.csv | schools that joined FBS that season (primary source team list) | Wikipedia season page infobox |
| --- | --- | --- | --- |
| 2023 | 133 | Jacksonville State, Sam Houston | 133 |
| 2024 | 134 | Kennesaw State | 134 |
| 2025 | 136 | Delaware, Missouri State | 136 |
| 2026 | 138 | North Dakota State, Sacramento State | 138 |

Wikipedia pages read on 2026-11-24:
`https://en.wikipedia.org/wiki/2023_NCAA_Division_I_FBS_football_season`,
`https://en.wikipedia.org/wiki/2024_NCAA_Division_I_FBS_football_season`,
`https://en.wikipedia.org/wiki/2025_NCAA_Division_I_FBS_football_season`,
`https://en.wikipedia.org/wiki/2026_NCAA_Division_I_FBS_football_season`.
The 2026 additions are also reported in ESPN's realignment summary for 2026
(`https://www.espn.com/college-football/story/_/id/49498819/college-football-conference-changes-realignment-fbs`).

The expected counts are written into `tests/test_datasets.py`, so the suite
fails if a team list changes size.

## Classification of opponents

In every season, every game with an FBS team in it had either two FBS teams
or one FBS team and one FCS team. No FBS team played a Division II or
Division III opponent in these four regular seasons, so `teams.csv` holds
only the divisions `FBS` and `FCS`.

## The scripts

| script | what it proves |
| --- | --- |
| `datasets/cross_check.py` | every game and every poll row agrees with ESPN, or the disagreement is settled in `resolutions.json` |
| `datasets/spot_check.py` | the selected games agree with NCAA.com and every AP poll agrees with College Poll Archive, or the difference is settled |
| `datasets/checksums.py --check` | the CSV files match `checksums.sha256` |
| `tests/test_datasets.py` | the same checks, rerun from the committed files alone |
