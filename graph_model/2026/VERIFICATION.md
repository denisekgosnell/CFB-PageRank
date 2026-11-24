# Verification record for the 2026 graph

## Translation checks

Output of `python3 graph_model/verify_graph.py --season 2026`:

```
season 2026
  pass  1. edge count equals game count (822 edges, 822 games)
  pass  2. every game id appears exactly once in the edges, and vice versa (missing 0, extra 0, duplicates 0)
  pass  3. every edge runs from the loser to the winner with winner_score > loser_score (0 wrong)
  pass  4. every edge property equals the matching column in games.csv (0 wrong)
  pass  5. the vertex set equals the team set (0 vertices not in teams.csv, 0 teams without a vertex)
  pass  6. every edge endpoint is a vertex (0 unknown endpoints)
  pass  7. no self-loops (0 self-loops)
  pass  8. rebuilding games.csv from the edges reproduces every row (0 rows differ)
```

## Point checks against NCAA.com

Ten edges drawn at random with seed 20261124 and compared with the box score on NCAA.com, which shares no ids with the primary source. The match is made on the date, the two scores, and the two team names. Passed: 10 of 10.

| edge | edge properties | NCAA.com | check | URL |
| --- | --- | --- | --- | --- |
| Florida Atlantic loses_to Florida | game_date 2026-09-05, week 1, winner_score 66, loser_score 21, margin 45 | Florida 66, Florida Atlantic 21 on 2026-09-05 | pass | https://www.ncaa.com/game/6603643 |
| Murray State loses_to Middle Tennessee | game_date 2026-09-05, week 1, winner_score 38, loser_score 14, margin 24 | Middle Tennessee 38, Murray State 14 on 2026-09-05 | pass | https://www.ncaa.com/game/6640287 |
| Oklahoma loses_to Georgia | game_date 2026-09-26, week 4, winner_score 41, loser_score 13, margin 28 | Georgia 41, Oklahoma 13 on 2026-09-26 | pass | https://www.ncaa.com/game/6604190 |
| Hawai'i loses_to Arizona State | game_date 2026-10-10, week 6, winner_score 30, loser_score 12, margin 18 | Arizona State 30, Hawai'i 12 on 2026-10-10 | pass | https://www.ncaa.com/game/6604209 |
| UCF loses_to Baylor | game_date 2026-10-30, week 9, winner_score 41, loser_score 9, margin 32 | Baylor 41, UCF 9 on 2026-10-30 | pass | https://www.ncaa.com/game/6603631 |
| UL Monroe loses_to Southern Miss | game_date 2026-10-31, week 9, winner_score 35, loser_score 21, margin 14 | Southern Miss 35, UL Monroe 21 on 2026-10-31 | pass | https://www.ncaa.com/game/6603706 |
| Sacramento State loses_to Toledo | game_date 2026-11-04, week 10, winner_score 20, loser_score 17, margin 3 | Toledo 20, Sacramento State 17 on 2026-11-04 | pass | https://www.ncaa.com/game/6603979 |
| Ohio loses_to Miami (OH) | game_date 2026-11-10, week 11, winner_score 34, loser_score 17, margin 17 | Miami (OH) 34, Ohio 17 on 2026-11-10 | pass | https://www.ncaa.com/game/6603991 |
| Fresno State loses_to Texas State | game_date 2026-11-14, week 11, winner_score 37, loser_score 35, margin 2 | Texas State 37, Fresno State 35 on 2026-11-14 | pass | https://www.ncaa.com/game/6604225 |
| Hawai'i loses_to North Dakota State | game_date 2026-11-14, week 11, winner_score 21, loser_score 13, margin 8 | North Dakota State 21, Hawai'i 13 on 2026-11-14 | pass | https://www.ncaa.com/game/6604132 |
