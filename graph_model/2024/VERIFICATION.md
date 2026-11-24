# Verification record for the 2024 graph

## Translation checks

Output of `python3 graph_model/verify_graph.py --season 2024`:

```
season 2024
  pass  1. edge count equals game count (863 edges, 863 games)
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
| Western Michigan loses_to Wisconsin | game_date 2024-08-30, week 1, winner_score 28, loser_score 14, margin 14 | Wisconsin 28, Western Michigan 14 on 2024-08-30 | pass | https://www.ncaa.com/game/6306193 |
| Florida loses_to Miami | game_date 2024-08-31, week 1, winner_score 41, loser_score 17, margin 24 | Miami 41, Florida 17 on 2024-08-31 | pass | https://www.ncaa.com/game/6305956 |
| Ohio loses_to Kentucky | game_date 2024-09-21, week 4, winner_score 41, loser_score 6, margin 35 | Kentucky 41, Ohio 6 on 2024-09-21 | pass | https://www.ncaa.com/game/6306297 |
| Minnesota loses_to Michigan | game_date 2024-09-28, week 5, winner_score 27, loser_score 24, margin 3 | Michigan 27, Minnesota 24 on 2024-09-28 | pass | https://www.ncaa.com/game/6306005 |
| South Florida loses_to Tulane | game_date 2024-09-28, week 5, winner_score 45, loser_score 10, margin 35 | Tulane 45, South Florida 10 on 2024-09-28 | pass | https://www.ncaa.com/game/6306731 |
| Marshall loses_to Georgia Southern | game_date 2024-10-12, week 7, winner_score 24, loser_score 23, margin 1 | Georgia Southern 24, Marshall 23 on 2024-10-12 | pass | https://www.ncaa.com/game/6305983 |
| Southern Miss loses_to UL Monroe | game_date 2024-10-12, week 7, winner_score 38, loser_score 21, margin 17 | UL Monroe 38, Southern Miss 21 on 2024-10-12 | pass | https://www.ncaa.com/game/6306029 |
| Hawai'i loses_to Washington State | game_date 2024-10-19, week 8, winner_score 42, loser_score 10, margin 32 | Washington State 42, Hawai'i 10 on 2024-10-19 | pass | https://www.ncaa.com/game/6306566 |
| Coastal Carolina loses_to Troy | game_date 2024-11-02, week 10, winner_score 38, loser_score 24, margin 14 | Troy 38, Coastal Carolina 24 on 2024-11-02 | pass | https://www.ncaa.com/game/6306338 |
| Tulsa loses_to East Carolina | game_date 2024-11-14, week 12, winner_score 38, loser_score 31, margin 7 | East Carolina 38, Tulsa 31 on 2024-11-14 | pass | https://www.ncaa.com/game/6306695 |
