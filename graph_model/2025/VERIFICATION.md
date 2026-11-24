# Verification record for the 2025 graph

## Translation checks

Output of `python3 graph_model/verify_graph.py --season 2025`:

```
season 2025
  pass  1. edge count equals game count (878 edges, 878 games)
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
| Long Island University loses_to Florida | game_date 2025-08-30, week 1, winner_score 55, loser_score 0, margin 55 | Florida 55, Long Island University 0 on 2025-08-30 | pass | https://www.ncaa.com/game/6458802 |
| Old Dominion loses_to Indiana | game_date 2025-08-30, week 1, winner_score 27, loser_score 14, margin 13 | Indiana 27, Old Dominion 14 on 2025-08-30 | pass | https://www.ncaa.com/game/6459519 |
| Saint Francis loses_to Buffalo | game_date 2025-09-06, week 2, winner_score 45, loser_score 6, margin 39 | Buffalo 45, Saint Francis 6 on 2025-09-06 | pass | https://www.ncaa.com/game/6459279 |
| SE Louisiana loses_to LSU | game_date 2025-09-20, week 4, winner_score 56, loser_score 10, margin 46 | LSU 56, SE Louisiana 10 on 2025-09-20 | pass | https://www.ncaa.com/game/6458841 |
| Illinois loses_to Indiana | game_date 2025-09-20, week 4, winner_score 63, loser_score 10, margin 53 | Indiana 63, Illinois 10 on 2025-09-20 | pass | https://www.ncaa.com/game/6459521 |
| Texas State loses_to Arkansas State | game_date 2025-10-04, week 6, winner_score 31, loser_score 30, margin 1 | Arkansas State 31, Texas State 30 on 2025-10-04 | pass | https://www.ncaa.com/game/6459208 |
| San José State loses_to Wyoming | game_date 2025-10-11, week 7, winner_score 35, loser_score 28, margin 7 | Wyoming 35, San José State 28 on 2025-10-11 | pass | https://www.ncaa.com/game/6459343 |
| UL Monroe loses_to Coastal Carolina | game_date 2025-10-11, week 7, winner_score 23, loser_score 8, margin 15 | Coastal Carolina 23, UL Monroe 8 on 2025-10-11 | pass | https://www.ncaa.com/game/6459335 |
| Kent State loses_to Toledo | game_date 2025-10-18, week 8, winner_score 45, loser_score 10, margin 35 | Toledo 45, Kent State 10 on 2025-10-18 | pass | https://www.ncaa.com/game/6458869 |
| Marshall loses_to Coastal Carolina | game_date 2025-10-30, week 10, winner_score 44, loser_score 27, margin 17 | Coastal Carolina 44, Marshall 27 on 2025-10-30 | pass | https://www.ncaa.com/game/6459591 |
