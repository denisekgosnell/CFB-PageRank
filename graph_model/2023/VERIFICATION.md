# Verification record for the 2023 graph

## Translation checks

Output of `python3 graph_model/verify_graph.py --season 2023`:

```
season 2023
  pass  1. edge count equals game count (857 edges, 857 games)
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
| Nebraska loses_to Minnesota | game_date 2023-08-31, week 1, winner_score 13, loser_score 10, margin 3 | Minnesota 13, Nebraska 10 on 2023-08-31 | pass | https://www.ncaa.com/game/6154129 |
| McNeese loses_to Florida | game_date 2023-09-09, week 2, winner_score 49, loser_score 7, margin 42 | Florida 49, McNeese 7 on 2023-09-09 | pass | https://www.ncaa.com/game/6154331 |
| Northwestern loses_to Penn State | game_date 2023-09-30, week 5, winner_score 41, loser_score 13, margin 28 | Penn State 41, Northwestern 13 on 2023-09-30 | pass | https://www.ncaa.com/game/6154177 |
| Charlotte loses_to SMU | game_date 2023-09-30, week 5, winner_score 34, loser_score 16, margin 18 | SMU 34, Charlotte 16 on 2023-09-30 | pass | https://www.ncaa.com/game/6154464 |
| San Diego State loses_to Air Force | game_date 2023-09-30, week 5, winner_score 49, loser_score 10, margin 39 | Air Force 49, San Diego State 10 on 2023-09-30 | pass | https://www.ncaa.com/game/6154507 |
| UL Monroe loses_to South Alabama | game_date 2023-10-07, week 6, winner_score 55, loser_score 7, margin 48 | South Alabama 55, UL Monroe 7 on 2023-10-07 | pass | https://www.ncaa.com/game/6154539 |
| App State loses_to Coastal Carolina | game_date 2023-10-10, week 7, winner_score 27, loser_score 24, margin 3 | Coastal Carolina 27, App State 24 on 2023-10-10 | pass | https://www.ncaa.com/game/6154556 |
| Purdue loses_to Ohio State | game_date 2023-10-14, week 7, winner_score 41, loser_score 7, margin 34 | Ohio State 41, Purdue 7 on 2023-10-14 | pass | https://www.ncaa.com/game/6154103 |
| Marshall loses_to App State | game_date 2023-11-04, week 10, winner_score 31, loser_score 9, margin 22 | App State 31, Marshall 9 on 2023-11-04 | pass | https://www.ncaa.com/game/6154742 |
| San Diego State loses_to Colorado State | game_date 2023-11-11, week 11, winner_score 22, loser_score 19, margin 3 | Colorado State 22, San Diego State 19 on 2023-11-11 | pass | https://www.ncaa.com/game/6154812 |
