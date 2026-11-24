# Sources

Every file under `datasets/` traces back to one of the four sources below. The
collection script, `datasets/collect.py`, is the only script in this repository
that touches the network. It records the exact URL, the time of the request, the
size, and the SHA-256 of every response in `datasets/_raw/<season>/manifest.json`.
That folder is not committed because it can be rebuilt by running the script.

All requests for this build were made on 2026-11-24.

## 1. College Football Data API (primary source)

Home: https://collegefootballdata.com

Used for the FBS team list, every regular-season game, and every weekly poll.
Access needs a free API key, sent as a bearer token.

| endpoint | parameters | what we take from it |
| --- | --- | --- |
| `https://api.collegefootballdata.com/teams/fbs` | `year=<season>` | the FBS members for the season: school, id, conference |
| `https://api.collegefootballdata.com/games` | `year=<season>`, `seasonType=regular` | every game at every level; we keep the games with at least one FBS team |
| `https://api.collegefootballdata.com/rankings` | `year=<season>`, `seasonType=regular` | the AP Top 25, the Coaches Poll, and the Playoff Committee Rankings, by week |

Two things to know about this source:

- Its `week` field puts the late-August games in week 1. We do not use that
  field. The week in `games.csv` is computed from the calendar, as described
  in `datasets/README.md`.
- Its `games` endpoint returns games from every level of college football,
  so the FBS filter is applied by us, by reading the `homeClassification`
  and `awayClassification` fields of each game.

## 2. ESPN (cross-check source)

Used to check every game and every poll row. ESPN and the primary source
share game ids and team ids, so the comparison needs no name matching.

| endpoint | parameters | what we take from it |
| --- | --- | --- |
| `https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard` | `dates=<YYYYMMDD>`, `groups=80`, `limit=500` | every FBS game on one day: teams, scores, date, flags |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/<season>/types/2/weeks/<week>/rankings` | none | the list of polls published that week |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/<season>/types/1/weeks/1/rankings` | none | the preseason polls, which some seasons file here |
| `.../rankings/1`, `.../rankings/2`, `.../rankings/21` | none | the AP Top 25, the Coaches Poll, and the CFP rankings, with the release date |

The scoreboard is asked one day at a time because its weekly form returns at
most 25 games for the 2024 season onward.

## 3. NCAA.com (third source for games)

Used for the spot checks of games. NCAA.com uses its own ids, so each game is
matched on the Eastern date, the two scores, and the two team names.

| page | what we take from it |
| --- | --- |
| `https://www.ncaa.com/scoreboard/football/fbs/<season>/<week>` | the final score of every FBS game that week, read from the data embedded in the page |
| `https://www.ncaa.com/game/<id>` | the box score page recorded next to each spot check |

## 4. College Poll Archive (third source for polls)

Used for the spot checks of the AP poll. Each page lists one poll with the
rank, team, points, and first-place votes.

| page | what we take from it |
| --- | --- |
| `https://www.collegepollarchive.com/football/ap/seasons.cfm?seasonid=<season>` | the link to the season's last poll |
| `https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=<id>` | one AP poll; the pages link to the previous poll, so the collector walks backward through the season |

## Tie-breakers

When the first two sources disagree, a third source settles the value and the
decision is written to `datasets/<season>/resolutions.json` with the URL that
settled it. The cloud environment that built this repository could not reach
school athletics sites, so the tie-breakers below come from NCAA.com,
College Poll Archive, published copies of the AP poll, and Wikipedia season
pages, each named in the resolution.

## Team names

`datasets/aliases.csv` maps every spelling of a team name seen in ESPN,
NCAA.com, and College Poll Archive to the canonical name used in
`teams.csv`. The canonical name is the one the primary source uses.
