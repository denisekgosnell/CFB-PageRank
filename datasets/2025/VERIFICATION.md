# Verification record for the 2025 season

This file is written by `datasets/write_verification.py` from the output of the collection, cross-check, and spot-check scripts. Rerun those scripts and this one to rebuild it.

## Counts

Games in games.csv: 878

FBS teams in teams.csv: 136

Opponents from outside FBS: 94 FCS

Data collected at 2026-11-24T19:33:59Z (UTC). Last game in the dataset: 2025-11-29.

Rivalry week is week 14 (the week holding 2025-11-29). The dataset runs through rivalry week.

| week | first game | last game | games |
| --- | --- | --- | --- |
| 0 | 2025-08-23 | 2025-08-23 | 5 |
| 1 | 2025-08-28 | 2025-09-01 | 91 |
| 2 | 2025-09-05 | 2025-09-06 | 83 |
| 3 | 2025-09-11 | 2025-09-13 | 70 |
| 4 | 2025-09-18 | 2025-09-20 | 62 |
| 5 | 2025-09-25 | 2025-09-27 | 53 |
| 6 | 2025-10-02 | 2025-10-04 | 51 |
| 7 | 2025-10-08 | 2025-10-11 | 56 |
| 8 | 2025-10-14 | 2025-10-18 | 60 |
| 9 | 2025-10-21 | 2025-10-25 | 53 |
| 10 | 2025-10-28 | 2025-11-01 | 52 |
| 11 | 2025-11-04 | 2025-11-08 | 52 |
| 12 | 2025-11-11 | 2025-11-15 | 59 |
| 13 | 2025-11-18 | 2025-11-22 | 64 |
| 14 | 2025-11-25 | 2025-11-29 | 67 |

Games involving an FBS team that are not in games.csv:

| reason | games |
| --- | --- |
| after rivalry week | 10 |

The full list, one line per game:

- 2025-12-05 North Texas at Tulane (American Championship): after rivalry week
- 2025-12-05 Kennesaw State at Jacksonville State (Conference USA Championship): after rivalry week
- 2025-12-05 UNLV at Boise State (Mountain West Championship): after rivalry week
- 2025-12-05 Troy at James Madison (Sun Belt Championship): after rivalry week
- 2025-12-06 BYU at Texas Tech (Big 12 Championship): after rivalry week
- 2025-12-06 Duke at Virginia (ACC Championship): after rivalry week
- 2025-12-06 Miami (OH) at Western Michigan (MAC Championship): after rivalry week
- 2025-12-06 Georgia at Alabama (SEC Championship): after rivalry week
- 2025-12-06 Indiana at Ohio State (Big Ten Championship): after rivalry week
- 2025-12-13 Army at Navy: after rivalry week

## Cross-check against ESPN

Games found in ESPN by id: 878 of 878.

Open disagreements: 0. Completed ESPN games with an FBS team that we lack: 0. Poll rows that disagree: 0.

Values settled by a third source (54 entries in resolutions.json). The primary source and ESPN disagreed on each game row below; for the poll rows the archive disagreed with both. The value kept is the one in the dataset:

| date | game or poll row | field | primary source | other sources | kept | settled by | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-08-29 | UNLV at Sam Houston | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Sam_Houston_Bearkats_football_team | Sam Houston played its 2025 home games at Shell Energy Stadium in Houston. The schedule lists each as a home game. |
| 2025-10-09 | Jacksonville State at Sam Houston | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Sam_Houston_Bearkats_football_team | Sam Houston played its 2025 home games at Shell Energy Stadium in Houston. The schedule lists each as a home game. |
| 2025-10-15 | UTEP at Sam Houston | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Sam_Houston_Bearkats_football_team | Sam Houston played its 2025 home games at Shell Energy Stadium in Houston. The schedule lists each as a home game. |
| 2025-11-15 | Delaware at Sam Houston | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Sam_Houston_Bearkats_football_team | Sam Houston played its 2025 home games at Shell Energy Stadium in Houston. The schedule lists each as a home game. |
| 2025-11-29 | Florida International at Sam Houston | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Sam_Houston_Bearkats_football_team | Sam Houston played its 2025 home games at Shell Energy Stadium in Houston. The schedule lists each as a home game. |
| 2025-09-06 | Arkansas State at Arkansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Arkansas_Razorbacks_football_team | Played at War Memorial Stadium in Little Rock. The schedule lists it as an Arkansas home game. |
| 2025-11-15 | Michigan at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Northwestern_Wildcats_football_team | Played at Wrigley Field in Chicago. The schedule lists each as a Northwestern home game. |
| 2025-11-22 | Minnesota at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2025_Northwestern_Wildcats_football_team | Played at Wrigley Field in Chicago. The schedule lists each as a Northwestern home game. |
| 2025-09-02 | ap_poll.csv Oregon | first_place_votes | 0 | ESPN 1 | 1 | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1252 | ESPN and College Poll Archive both record one first-place vote for Oregon in the September 2, 2025 poll. The primary source records none. |
| 2025-10-12 | ap_poll.csv Vanderbilt | points | 547 | ESPN 547, archive 548 | 547 | https://www.ncaa.com/news/football/article/2025-10-12/indiana-rises-top-3-oklahoma-falls-new-ap-top-25 | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-12 | ap_poll.csv Virginia | points | 521 | ESPN 521, archive 522 | 521 | https://www.ncaa.com/news/football/article/2025-10-12/indiana-rises-top-3-oklahoma-falls-new-ap-top-25 | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-12 | ap_poll.csv USC | points | 361 | ESPN 361, archive 353 | 361 | https://www.ncaa.com/news/football/article/2025-10-12/indiana-rises-top-3-oklahoma-falls-new-ap-top-25 | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-12 | ap_poll.csv Memphis | points | 285 | ESPN 285, archive 286 | 285 | https://www.ncaa.com/news/football/article/2025-10-12/indiana-rises-top-3-oklahoma-falls-new-ap-top-25 | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-12 | ap_poll.csv Utah | points | 261 | ESPN 261, archive 264 | 261 | https://www.ncaa.com/news/football/article/2025-10-12/indiana-rises-top-3-oklahoma-falls-new-ap-top-25 | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-12 | ap_poll.csv Cincinnati | points | 184 | ESPN 184, archive 185 | 184 | https://www.ncaa.com/news/football/article/2025-10-12/indiana-rises-top-3-oklahoma-falls-new-ap-top-25 | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-12 | ap_poll.csv Nebraska | points | 149 | ESPN 149, archive 148 | 149 | https://www.ncaa.com/news/football/article/2025-10-12/indiana-rises-top-3-oklahoma-falls-new-ap-top-25 | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Georgia Tech | points | 1143 | ESPN 1143, archive 1144 | 1143 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv BYU | points | 975 | ESPN 975, archive 974 | 975 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Oklahoma | points | 882 | ESPN 882, archive 883 | 882 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Virginia | points | 624 | ESPN 624, archive 615 | 624 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Tennessee | points | 527 | ESPN 527, archive 528 | 527 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Louisville | points | 458 | ESPN 458, archive 459 | 458 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv LSU | points | 388 | ESPN 388, archive 389 | 388 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Cincinnati | points | 350 | ESPN 350, archive 351 | 350 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Texas | points | 318 | ESPN 318, archive 319 | 318 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Arizona State | points | 155 | ESPN 155, archive 156 | 155 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-10-19 | ap_poll.csv Michigan | points | 123 | ESPN 123, archive 124 | 123 | https://www.ncaa.com/news/football/article/2025-10-19/vanderbilt-and-georgia-tech-jump-ap-top-25-after-week-8-upsets | College Poll Archive lists different point totals. The primary source and ESPN agree, and NCAA.com's published copy of the poll shows the same totals as ours. |
| 2025-11-30 | ap_poll.csv BYU | points | 982 | ESPN 982, archive 980 | 982 | https://greatbendpost.com/posts/3a150dda-d8bc-448a-9479-2c8107628160 | College Poll Archive lists different point totals. The primary source and ESPN agree, and a wire-service copy of the poll published the day it was released shows the same totals as ours. |
| 2025-11-30 | ap_poll.csv Vanderbilt | points | 871 | ESPN 871, archive 872 | 871 | https://greatbendpost.com/posts/3a150dda-d8bc-448a-9479-2c8107628160 | College Poll Archive lists different point totals. The primary source and ESPN agree, and a wire-service copy of the poll published the day it was released shows the same totals as ours. |
| 2025-11-30 | ap_poll.csv Texas | points | 861 | ESPN 861, archive 862 | 861 | https://greatbendpost.com/posts/3a150dda-d8bc-448a-9479-2c8107628160 | College Poll Archive lists different point totals. The primary source and ESPN agree, and a wire-service copy of the poll published the day it was released shows the same totals as ours. |
| 2025-11-09 | ap_poll.csv Ohio State | points | 1610 | ESPN 1610, archive 1585 | 1610 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Ohio State | first_place_votes | 55 | ESPN 55, archive 54 | 55 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Indiana | points | 1549 | ESPN 1549, archive 1525 | 1549 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Texas A&M | points | 1518 | ESPN 1518, archive 1495 | 1518 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Alabama | points | 1427 | ESPN 1427, archive 1405 | 1427 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Georgia | points | 1353 | ESPN 1353, archive 1332 | 1353 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Ole Miss | points | 1248 | ESPN 1248, archive 1230 | 1248 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Oregon | points | 1245 | ESPN 1245, archive 1224 | 1245 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Texas Tech | points | 1211 | ESPN 1211, archive 1193 | 1211 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Notre Dame | points | 1102 | ESPN 1102, archive 1085 | 1102 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Texas | points | 961 | ESPN 961, archive 945 | 961 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Oklahoma | points | 928 | ESPN 928, archive 913 | 928 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv BYU | points | 898 | ESPN 898, archive 886 | 898 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Vanderbilt | points | 821 | ESPN 821, archive 807 | 821 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Georgia Tech | points | 788 | ESPN 788, archive 775 | 788 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Utah | points | 695 | ESPN 695, archive 684 | 695 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Miami | points | 683 | ESPN 683, archive 673 | 683 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv USC | points | 645 | ESPN 645, archive 636 | 645 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Michigan | points | 498 | ESPN 498, archive 490 | 498 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Tennessee | points | 276 | ESPN 276, archive 269 | 276 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Cincinnati | points | 224 | ESPN 224, archive 218 | 224 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv Pittsburgh | points | 201 | ESPN 201, archive 198 | 201 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv James Madison | points | 167 | ESPN 167, archive 163 | 167 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |
| 2025-11-09 | ap_poll.csv South Florida | points | 116 | ESPN 116, archive 115 | 116 | https://www.buckeyesports.com/ohio-state-remains-at-no-1-in-latest-ap-poll | College Poll Archive lists every tally about one ballot lower than ours, with Ohio State at 54 first-place votes instead of 55. The primary source and ESPN agree with each other, and a report published the day of the poll gives Indiana six first-place votes and Texas A&M four, which leaves 55 of the 65 ballots for Ohio State, as we have it. |

## Completeness

Games played by each FBS team in the dataset. The most common count is 12.

| team | games |
| --- | --- |
| Air Force | 12 |
| Akron | 12 |
| Alabama | 12 |
| App State | 12 |
| Arizona | 12 |
| Arizona State | 12 |
| Arkansas | 12 |
| Arkansas State | 12 |
| Army | 11 |
| Auburn | 12 |
| BYU | 12 |
| Ball State | 12 |
| Baylor | 12 |
| Boise State | 12 |
| Boston College | 12 |
| Bowling Green | 12 |
| Buffalo | 12 |
| California | 12 |
| Central Michigan | 12 |
| Charlotte | 12 |
| Cincinnati | 12 |
| Clemson | 12 |
| Coastal Carolina | 12 |
| Colorado | 12 |
| Colorado State | 12 |
| Delaware | 12 |
| Duke | 12 |
| East Carolina | 12 |
| Eastern Michigan | 12 |
| Florida | 12 |
| Florida Atlantic | 12 |
| Florida International | 12 |
| Florida State | 12 |
| Fresno State | 12 |
| Georgia | 12 |
| Georgia Southern | 12 |
| Georgia State | 12 |
| Georgia Tech | 12 |
| Hawai'i | 12 |
| Houston | 12 |
| Illinois | 12 |
| Indiana | 12 |
| Iowa | 12 |
| Iowa State | 12 |
| Jacksonville State | 12 |
| James Madison | 12 |
| Kansas | 12 |
| Kansas State | 12 |
| Kennesaw State | 12 |
| Kent State | 12 |
| Kentucky | 12 |
| LSU | 12 |
| Liberty | 12 |
| Louisiana | 12 |
| Louisiana Tech | 12 |
| Louisville | 12 |
| Marshall | 12 |
| Maryland | 12 |
| Massachusetts | 12 |
| Memphis | 12 |
| Miami | 12 |
| Miami (OH) | 12 |
| Michigan | 12 |
| Michigan State | 12 |
| Middle Tennessee | 12 |
| Minnesota | 12 |
| Mississippi State | 12 |
| Missouri | 12 |
| Missouri State | 12 |
| NC State | 12 |
| Navy | 11 |
| Nebraska | 12 |
| Nevada | 12 |
| New Mexico | 12 |
| New Mexico State | 12 |
| North Carolina | 12 |
| North Texas | 12 |
| Northern Illinois | 12 |
| Northwestern | 12 |
| Notre Dame | 12 |
| Ohio | 12 |
| Ohio State | 12 |
| Oklahoma | 12 |
| Oklahoma State | 12 |
| Old Dominion | 12 |
| Ole Miss | 12 |
| Oregon | 12 |
| Oregon State | 12 |
| Penn State | 12 |
| Pittsburgh | 12 |
| Purdue | 12 |
| Rice | 12 |
| Rutgers | 12 |
| SMU | 12 |
| Sam Houston | 12 |
| San Diego State | 12 |
| San José State | 12 |
| South Alabama | 12 |
| South Carolina | 12 |
| South Florida | 12 |
| Southern Miss | 12 |
| Stanford | 12 |
| Syracuse | 12 |
| TCU | 12 |
| Temple | 12 |
| Tennessee | 12 |
| Texas | 12 |
| Texas A&M | 12 |
| Texas State | 12 |
| Texas Tech | 12 |
| Toledo | 12 |
| Troy | 12 |
| Tulane | 12 |
| Tulsa | 12 |
| UAB | 12 |
| UCF | 12 |
| UCLA | 12 |
| UConn | 12 |
| UL Monroe | 12 |
| UNLV | 12 |
| USC | 12 |
| UTEP | 12 |
| UTSA | 12 |
| Utah | 12 |
| Utah State | 12 |
| Vanderbilt | 12 |
| Virginia | 12 |
| Virginia Tech | 12 |
| Wake Forest | 12 |
| Washington | 12 |
| Washington State | 12 |
| West Virginia | 12 |
| Western Kentucky | 12 |
| Western Michigan | 12 |
| Wisconsin | 12 |
| Wyoming | 12 |

## Spot checks against NCAA.com

Random draw of 25 games with seed 20261124, plus every game of the top 10 in the AP poll of 2025-11-30 (Alabama, Georgia, Indiana, Notre Dame, Ohio State, Oklahoma, Ole Miss, Oregon, Texas A&M, Texas Tech).

Selected games checked: 134. Passed: 134.

Beyond the selection, every game in the season was matched to NCAA.com by date, by score, and by team name: 878 of 878 agree, 0 could not be matched.

Games where NCAA.com designates a different home team (scores and teams agree; this is a designation, not a result):

- 2025-11-01 Georgia at Florida: we list Florida as home, NCAA.com lists Georgia (https://www.ncaa.com/game/6458809)

| date | game | our result | NCAA.com result | why selected | check | URL |
| --- | --- | --- | --- | --- | --- | --- |
| 2025-08-30 | Alabama at Florida State | Florida State 31, Alabama 17 | Florida State 31, Alabama 17 | final AP top 10 | pass | https://www.ncaa.com/game/6459216 |
| 2025-08-30 | Alabama A&M at Arkansas | Arkansas 52, Alabama A&M 7 | Arkansas 52, Alabama A&M 7 | random draw | pass | https://www.ncaa.com/game/6459210 |
| 2025-08-30 | Long Island University at Florida | Florida 55, Long Island University 0 | Florida 55, Long Island University 0 | random draw | pass | https://www.ncaa.com/game/6458802 |
| 2025-08-30 | Marshall at Georgia | Georgia 45, Marshall 7 | Georgia 45, Marshall 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459414 |
| 2025-08-30 | Georgia State at Ole Miss | Ole Miss 63, Georgia State 7 | Ole Miss 63, Georgia State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459178 |
| 2025-08-30 | Illinois State at Oklahoma | Oklahoma 35, Illinois State 3 | Oklahoma 35, Illinois State 3 | final AP top 10 | pass | https://www.ncaa.com/game/6459562 |
| 2025-08-30 | Texas at Ohio State | Ohio State 14, Texas 7 | Ohio State 14, Texas 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459545 |
| 2025-08-30 | UTSA at Texas A&M | Texas A&M 42, UTSA 24 | Texas A&M 42, UTSA 24 | final AP top 10 | pass | https://www.ncaa.com/game/6459066 |
| 2025-08-30 | Montana State at Oregon | Oregon 59, Montana State 13 | Oregon 59, Montana State 13 | final AP top 10 | pass | https://www.ncaa.com/game/6459280 |
| 2025-08-30 | Old Dominion at Indiana | Indiana 27, Old Dominion 14 | Indiana 27, Old Dominion 14 | random draw | pass | https://www.ncaa.com/game/6459519 |
| 2025-08-30 | Arkansas-Pine Bluff at Texas Tech | Texas Tech 67, Arkansas-Pine Bluff 7 | Texas Tech 67, Arkansas-Pine Bluff 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459653 |
| 2025-08-31 | Notre Dame at Miami | Miami 27, Notre Dame 24 | Miami 27, Notre Dame 24 | final AP top 10 | pass | https://www.ncaa.com/game/6459624 |
| 2025-09-06 | UL Monroe at Alabama | Alabama 73, UL Monroe 0 | Alabama 73, UL Monroe 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459332 |
| 2025-09-06 | Austin Peay at Georgia | Georgia 28, Austin Peay 6 | Georgia 28, Austin Peay 6 | final AP top 10 | pass | https://www.ncaa.com/game/6459386 |
| 2025-09-06 | Ole Miss at Kentucky | Ole Miss 30, Kentucky 23 | Ole Miss 30, Kentucky 23 | final AP top 10 | pass | https://www.ncaa.com/game/6459179 |
| 2025-09-06 | Michigan at Oklahoma | Oklahoma 24, Michigan 13 | Oklahoma 24, Michigan 13 | final AP top 10 | pass | https://www.ncaa.com/game/6459563 |
| 2025-09-06 | Utah State at Texas A&M | Texas A&M 44, Utah State 22 | Texas A&M 44, Utah State 22 | final AP top 10 | pass | https://www.ncaa.com/game/6459067 |
| 2025-09-06 | Kennesaw State at Indiana | Indiana 56, Kennesaw State 9 | Indiana 56, Kennesaw State 9 | final AP top 10 | pass | https://www.ncaa.com/game/6459520 |
| 2025-09-06 | Grambling at Ohio State | Ohio State 70, Grambling 0 | Ohio State 70, Grambling 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459546 |
| 2025-09-06 | Oklahoma State at Oregon | Oregon 69, Oklahoma State 3 | Oregon 69, Oklahoma State 3 | final AP top 10 | pass | https://www.ncaa.com/game/6459283 |
| 2025-09-06 | Kent State at Texas Tech | Texas Tech 62, Kent State 14 | Texas Tech 62, Kent State 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459263 |
| 2025-09-06 | Saint Francis at Buffalo | Buffalo 45, Saint Francis 6 | Buffalo 45, Saint Francis 6 | random draw | pass | https://www.ncaa.com/game/6459279 |
| 2025-09-12 | Indiana State at Indiana | Indiana 73, Indiana State 0 | Indiana 73, Indiana State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459445 |
| 2025-09-13 | Wisconsin at Alabama | Alabama 38, Wisconsin 14 | Alabama 38, Wisconsin 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459303 |
| 2025-09-13 | Arkansas at Ole Miss | Ole Miss 41, Arkansas 35 | Ole Miss 41, Arkansas 35 | final AP top 10 | pass | https://www.ncaa.com/game/6459180 |
| 2025-09-13 | Oklahoma at Temple | Oklahoma 42, Temple 3 | Oklahoma 42, Temple 3 | final AP top 10 | pass | https://www.ncaa.com/game/6459129 |
| 2025-09-13 | Georgia at Tennessee | Georgia 44, Tennessee 41 | Georgia 44, Tennessee 41 | final AP top 10 | pass | https://www.ncaa.com/game/6459399 |
| 2025-09-13 | Texas A&M at Notre Dame | Texas A&M 41, Notre Dame 40 | Texas A&M 41, Notre Dame 40 | final AP top 10 | pass | https://www.ncaa.com/game/6459068 |
| 2025-09-13 | Ohio at Ohio State | Ohio State 37, Ohio 9 | Ohio State 37, Ohio 9 | final AP top 10 | pass | https://www.ncaa.com/game/6459547 |
| 2025-09-13 | Oregon at Northwestern | Oregon 34, Northwestern 14 | Oregon 34, Northwestern 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459287 |
| 2025-09-13 | USC at Purdue | USC 33, Purdue 17 | USC 33, Purdue 17 | random draw | pass | https://www.ncaa.com/game/6459086 |
| 2025-09-13 | Oregon State at Texas Tech | Texas Tech 45, Oregon State 14 | Texas Tech 45, Oregon State 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459375 |
| 2025-09-13 | Air Force at Utah State | Utah State 49, Air Force 30 | Utah State 49, Air Force 30 | random draw | pass | https://www.ncaa.com/game/6459168 |
| 2025-09-13 | Buffalo at Kent State | Buffalo 31, Kent State 28 | Buffalo 31, Kent State 28 | random draw | pass | https://www.ncaa.com/game/6459266 |
| 2025-09-20 | SE Louisiana at LSU | LSU 56, SE Louisiana 10 | LSU 56, SE Louisiana 10 | random draw | pass | https://www.ncaa.com/game/6458841 |
| 2025-09-20 | Tulane at Ole Miss | Ole Miss 45, Tulane 10 | Ole Miss 45, Tulane 10 | final AP top 10 | pass | https://www.ncaa.com/game/6458817 |
| 2025-09-20 | Auburn at Oklahoma | Oklahoma 24, Auburn 17 | Oklahoma 24, Auburn 17 | final AP top 10 | pass | https://www.ncaa.com/game/6459151 |
| 2025-09-20 | Oregon State at Oregon | Oregon 41, Oregon State 7 | Oregon 41, Oregon State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459288 |
| 2025-09-20 | Illinois at Indiana | Indiana 63, Illinois 10 | Indiana 63, Illinois 10 | random draw | pass | https://www.ncaa.com/game/6459521 |
| 2025-09-20 | Purdue at Notre Dame | Notre Dame 56, Purdue 30 | Notre Dame 56, Purdue 30 | final AP top 10 | pass | https://www.ncaa.com/game/6459087 |
| 2025-09-20 | Texas Tech at Utah | Texas Tech 34, Utah 10 | Texas Tech 34, Utah 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459189 |
| 2025-09-27 | Notre Dame at Arkansas | Notre Dame 56, Arkansas 13 | Notre Dame 56, Arkansas 13 | final AP top 10 | pass | https://www.ncaa.com/game/6459248 |
| 2025-09-27 | Alabama at Georgia | Alabama 24, Georgia 21 | Alabama 24, Georgia 21 | final AP top 10 | pass | https://www.ncaa.com/game/6459415 |
| 2025-09-27 | LSU at Ole Miss | Ole Miss 24, LSU 19 | Ole Miss 24, LSU 19 | final AP top 10 | pass | https://www.ncaa.com/game/6458847 |
| 2025-09-27 | Auburn at Texas A&M | Texas A&M 16, Auburn 10 | Texas A&M 16, Auburn 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459069 |
| 2025-09-27 | Ohio State at Washington | Ohio State 24, Washington 6 | Ohio State 24, Washington 6 | final AP top 10 | pass | https://www.ncaa.com/game/6459548 |
| 2025-09-27 | Indiana at Iowa | Indiana 20, Iowa 15 | Indiana 20, Iowa 15 | final AP top 10 | pass | https://www.ncaa.com/game/6459370 |
| 2025-09-27 | Oregon at Penn State | Oregon 30, Penn State 24 | Oregon 30, Penn State 24 | final AP top 10 | pass | https://www.ncaa.com/game/6459289 |
| 2025-09-27 | BYU at Colorado | BYU 24, Colorado 21 | BYU 24, Colorado 21 | random draw | pass | https://www.ncaa.com/game/6459661 |
| 2025-10-04 | Vanderbilt at Alabama | Alabama 30, Vanderbilt 14 | Alabama 30, Vanderbilt 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459558 |
| 2025-10-04 | Kentucky at Georgia | Georgia 35, Kentucky 14 | Georgia 35, Kentucky 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459350 |
| 2025-10-04 | Kent State at Oklahoma | Oklahoma 44, Kent State 0 | Oklahoma 44, Kent State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459267 |
| 2025-10-04 | Mississippi State at Texas A&M | Texas A&M 31, Mississippi State 9 | Texas A&M 31, Mississippi State 9 | final AP top 10 | pass | https://www.ncaa.com/game/6459070 |
| 2025-10-04 | Minnesota at Ohio State | Ohio State 42, Minnesota 3 | Ohio State 42, Minnesota 3 | final AP top 10 | pass | https://www.ncaa.com/game/6458947 |
| 2025-10-04 | Texas Tech at Houston | Texas Tech 35, Houston 11 | Texas Tech 35, Houston 11 | final AP top 10 | pass | https://www.ncaa.com/game/6458855 |
| 2025-10-04 | Boise State at Notre Dame | Notre Dame 28, Boise State 7 | Notre Dame 28, Boise State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459566 |
| 2025-10-04 | Texas State at Arkansas State | Arkansas State 31, Texas State 30 | Arkansas State 31, Texas State 30 | random draw | pass | https://www.ncaa.com/game/6459208 |
| 2025-10-11 | Georgia at Auburn | Georgia 20, Auburn 10 | Georgia 20, Auburn 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459152 |
| 2025-10-11 | Washington State at Ole Miss | Ole Miss 24, Washington State 21 | Ole Miss 24, Washington State 21 | final AP top 10 | pass | https://www.ncaa.com/game/6459181 |
| 2025-10-11 | Alabama at Missouri | Alabama 27, Missouri 24 | Alabama 27, Missouri 24 | final AP top 10 | pass | https://www.ncaa.com/game/6459234 |
| 2025-10-11 | Oklahoma at Texas | Texas 23, Oklahoma 6 | Texas 23, Oklahoma 6 | final AP top 10 | pass | https://www.ncaa.com/game/6459561 |
| 2025-10-11 | Florida at Texas A&M | Texas A&M 34, Florida 17 | Texas A&M 34, Florida 17 | final AP top 10 | pass | https://www.ncaa.com/game/6458807 |
| 2025-10-11 | Ohio State at Illinois | Ohio State 34, Illinois 16 | Ohio State 34, Illinois 16 | final AP top 10 | pass | https://www.ncaa.com/game/6459536 |
| 2025-10-11 | Indiana at Oregon | Indiana 30, Oregon 20 | Indiana 30, Oregon 20 | final AP top 10 | pass | https://www.ncaa.com/game/6459290 |
| 2025-10-11 | NC State at Notre Dame | Notre Dame 36, NC State 7 | Notre Dame 36, NC State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459200 |
| 2025-10-11 | UCF at Cincinnati | Cincinnati 20, UCF 11 | Cincinnati 20, UCF 11 | random draw | pass | https://www.ncaa.com/game/6458934 |
| 2025-10-11 | Kansas at Texas Tech | Texas Tech 42, Kansas 17 | Texas Tech 42, Kansas 17 | final AP top 10 | pass | https://www.ncaa.com/game/6459017 |
| 2025-10-11 | San José State at Wyoming | Wyoming 35, San José State 28 | Wyoming 35, San José State 28 | random draw | pass | https://www.ncaa.com/game/6459343 |
| 2025-10-11 | UL Monroe at Coastal Carolina | Coastal Carolina 23, UL Monroe 8 | Coastal Carolina 23, UL Monroe 8 | random draw | pass | https://www.ncaa.com/game/6459335 |
| 2025-10-18 | Tennessee at Alabama | Alabama 37, Tennessee 20 | Alabama 37, Tennessee 20 | final AP top 10 | pass | https://www.ncaa.com/game/6459402 |
| 2025-10-18 | Texas A&M at Arkansas | Texas A&M 45, Arkansas 42 | Texas A&M 45, Arkansas 42 | final AP top 10 | pass | https://www.ncaa.com/game/6459071 |
| 2025-10-18 | Ole Miss at Georgia | Georgia 43, Ole Miss 35 | Georgia 43, Ole Miss 35 | random draw | pass | https://www.ncaa.com/game/6459182 |
| 2025-10-18 | Oklahoma at South Carolina | Oklahoma 26, South Carolina 7 | Oklahoma 26, South Carolina 7 | final AP top 10 | pass | https://www.ncaa.com/game/6458996 |
| 2025-10-18 | USC at Notre Dame | Notre Dame 34, USC 24 | Notre Dame 34, USC 24 | final AP top 10 | pass | https://www.ncaa.com/game/6459656 |
| 2025-10-18 | Oregon at Rutgers | Oregon 56, Rutgers 10 | Oregon 56, Rutgers 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459291 |
| 2025-10-18 | Ohio State at Wisconsin | Ohio State 34, Wisconsin 0 | Ohio State 34, Wisconsin 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459308 |
| 2025-10-18 | Michigan State at Indiana | Indiana 38, Michigan State 13 | Indiana 38, Michigan State 13 | final AP top 10 | pass | https://www.ncaa.com/game/6459522 |
| 2025-10-18 | Texas Tech at Arizona State | Arizona State 26, Texas Tech 22 | Arizona State 26, Texas Tech 22 | final AP top 10 | pass | https://www.ncaa.com/game/6459509 |
| 2025-10-18 | Temple at Charlotte | Temple 49, Charlotte 14 | Temple 49, Charlotte 14 | random draw | pass | https://www.ncaa.com/game/6459133 |
| 2025-10-18 | Kent State at Toledo | Toledo 45, Kent State 10 | Toledo 45, Kent State 10 | random draw | pass | https://www.ncaa.com/game/6458869 |
| 2025-10-25 | Texas A&M at LSU | Texas A&M 49, LSU 25 | Texas A&M 49, LSU 25 | final AP top 10 | pass | https://www.ncaa.com/game/6458843 |
| 2025-10-25 | Ole Miss at Oklahoma | Ole Miss 34, Oklahoma 26 | Ole Miss 34, Oklahoma 26 | final AP top 10 | pass | https://www.ncaa.com/game/6459183 |
| 2025-10-25 | Alabama at South Carolina | Alabama 29, South Carolina 22 | Alabama 29, South Carolina 22 | final AP top 10 | pass | https://www.ncaa.com/game/6458997 |
| 2025-10-25 | UCLA at Indiana | Indiana 56, UCLA 6 | Indiana 56, UCLA 6 | final AP top 10 | pass | https://www.ncaa.com/game/6459523 |
| 2025-10-25 | Wisconsin at Oregon | Oregon 21, Wisconsin 7 | Oregon 21, Wisconsin 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459292 |
| 2025-10-25 | Oklahoma State at Texas Tech | Texas Tech 42, Oklahoma State 0 | Texas Tech 42, Oklahoma State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459579 |
| 2025-10-30 | Marshall at Coastal Carolina | Coastal Carolina 44, Marshall 27 | Coastal Carolina 44, Marshall 27 | random draw | pass | https://www.ncaa.com/game/6459591 |
| 2025-11-01 | Georgia at Florida | Georgia 24, Florida 20 | Georgia 24, Florida 20 | final AP top 10 | pass | https://www.ncaa.com/game/6458809 |
| 2025-11-01 | South Carolina at Ole Miss | Ole Miss 30, South Carolina 14 | Ole Miss 30, South Carolina 14 | final AP top 10 | pass | https://www.ncaa.com/game/6458998 |
| 2025-11-01 | Oklahoma at Tennessee | Oklahoma 33, Tennessee 27 | Oklahoma 33, Tennessee 27 | final AP top 10 | pass | https://www.ncaa.com/game/6459403 |
| 2025-11-01 | Indiana at Maryland | Indiana 55, Maryland 10 | Indiana 55, Maryland 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459524 |
| 2025-11-01 | Penn State at Ohio State | Ohio State 38, Penn State 14 | Ohio State 38, Penn State 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459549 |
| 2025-11-01 | Notre Dame at Boston College | Notre Dame 25, Boston College 10 | Notre Dame 25, Boston College 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459646 |
| 2025-11-01 | Texas Tech at Kansas State | Texas Tech 43, Kansas State 20 | Texas Tech 43, Kansas State 20 | final AP top 10 | pass | https://www.ncaa.com/game/6459243 |
| 2025-11-08 | LSU at Alabama | Alabama 20, LSU 9 | Alabama 20, LSU 9 | final AP top 10 | pass | https://www.ncaa.com/game/6458849 |
| 2025-11-08 | The Citadel at Ole Miss | Ole Miss 49, The Citadel 0 | Ole Miss 49, The Citadel 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459184 |
| 2025-11-08 | Georgia at Mississippi State | Georgia 41, Mississippi State 21 | Georgia 41, Mississippi State 21 | final AP top 10 | pass | https://www.ncaa.com/game/6459081 |
| 2025-11-08 | Texas A&M at Missouri | Texas A&M 38, Missouri 17 | Texas A&M 38, Missouri 17 | final AP top 10 | pass | https://www.ncaa.com/game/6459072 |
| 2025-11-08 | Indiana at Penn State | Indiana 27, Penn State 24 | Indiana 27, Penn State 24 | final AP top 10 | pass | https://www.ncaa.com/game/6459525 |
| 2025-11-08 | Ohio State at Purdue | Ohio State 34, Purdue 10 | Ohio State 34, Purdue 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459090 |
| 2025-11-08 | Oregon at Iowa | Oregon 18, Iowa 16 | Oregon 18, Iowa 16 | final AP top 10 | pass | https://www.ncaa.com/game/6459293 |
| 2025-11-08 | BYU at Texas Tech | Texas Tech 29, BYU 7 | Texas Tech 29, BYU 7 | random draw | pass | https://www.ncaa.com/game/6459654 |
| 2025-11-08 | Navy at Notre Dame | Notre Dame 49, Navy 10 | Notre Dame 49, Navy 10 | random draw | pass | https://www.ncaa.com/game/6459629 |
| 2025-11-11 | Kent State at Akron | Kent State 42, Akron 35 | Kent State 42, Akron 35 | random draw | pass | https://www.ncaa.com/game/6458894 |
| 2025-11-14 | Minnesota at Oregon | Oregon 42, Minnesota 13 | Oregon 42, Minnesota 13 | final AP top 10 | pass | https://www.ncaa.com/game/6458952 |
| 2025-11-15 | Oklahoma at Alabama | Oklahoma 23, Alabama 21 | Oklahoma 23, Alabama 21 | final AP top 10 | pass | https://www.ncaa.com/game/6459559 |
| 2025-11-15 | Texas at Georgia | Georgia 35, Texas 10 | Georgia 35, Texas 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459418 |
| 2025-11-15 | Florida at Ole Miss | Ole Miss 34, Florida 24 | Ole Miss 34, Florida 24 | final AP top 10 | pass | https://www.ncaa.com/game/6458811 |
| 2025-11-15 | South Carolina at Texas A&M | Texas A&M 31, South Carolina 30 | Texas A&M 31, South Carolina 30 | final AP top 10 | pass | https://www.ncaa.com/game/6458999 |
| 2025-11-15 | UCLA at Ohio State | Ohio State 48, UCLA 10 | Ohio State 48, UCLA 10 | final AP top 10 | pass | https://www.ncaa.com/game/6459550 |
| 2025-11-15 | Wisconsin at Indiana | Indiana 31, Wisconsin 7 | Indiana 31, Wisconsin 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459310 |
| 2025-11-15 | Notre Dame at Pittsburgh | Notre Dame 37, Pittsburgh 15 | Notre Dame 37, Pittsburgh 15 | final AP top 10 | pass | https://www.ncaa.com/game/6459532 |
| 2025-11-15 | UCF at Texas Tech | Texas Tech 48, UCF 9 | Texas Tech 48, UCF 9 | final AP top 10 | pass | https://www.ncaa.com/game/6458937 |
| 2025-11-15 | UTSA at Charlotte | UTSA 28, Charlotte 7 | UTSA 28, Charlotte 7 | random draw | pass | https://www.ncaa.com/game/6459665 |
| 2025-11-22 | Eastern Illinois at Alabama | Alabama 56, Eastern Illinois 0 | Alabama 56, Eastern Illinois 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459124 |
| 2025-11-22 | Charlotte at Georgia | Georgia 35, Charlotte 3 | Georgia 35, Charlotte 3 | final AP top 10 | pass | https://www.ncaa.com/game/6459420 |
| 2025-11-22 | Missouri at Oklahoma | Oklahoma 17, Missouri 6 | Oklahoma 17, Missouri 6 | final AP top 10 | pass | https://www.ncaa.com/game/6459237 |
| 2025-11-22 | Samford at Texas A&M | Texas A&M 48, Samford 0 | Texas A&M 48, Samford 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459073 |
| 2025-11-22 | USC at Oregon | Oregon 42, USC 27 | Oregon 42, USC 27 | final AP top 10 | pass | https://www.ncaa.com/game/6459294 |
| 2025-11-22 | Rutgers at Ohio State | Ohio State 42, Rutgers 9 | Ohio State 42, Rutgers 9 | final AP top 10 | pass | https://www.ncaa.com/game/6459551 |
| 2025-11-22 | Syracuse at Notre Dame | Notre Dame 70, Syracuse 7 | Notre Dame 70, Syracuse 7 | final AP top 10 | pass | https://www.ncaa.com/game/6459657 |
| 2025-11-28 | Georgia at Georgia Tech | Georgia 16, Georgia Tech 9 | Georgia 16, Georgia Tech 9 | final AP top 10 | pass | https://www.ncaa.com/game/6459425 |
| 2025-11-28 | Ole Miss at Mississippi State | Ole Miss 38, Mississippi State 19 | Ole Miss 38, Mississippi State 19 | final AP top 10 | pass | https://www.ncaa.com/game/6459083 |
| 2025-11-28 | Texas A&M at Texas | Texas 27, Texas A&M 17 | Texas 27, Texas A&M 17 | final AP top 10 | pass | https://www.ncaa.com/game/6459074 |
| 2025-11-28 | Indiana at Purdue | Indiana 56, Purdue 3 | Indiana 56, Purdue 3 | final AP top 10 | pass | https://www.ncaa.com/game/6459092 |
| 2025-11-29 | Alabama at Auburn | Alabama 27, Auburn 20 | Alabama 27, Auburn 20 | final AP top 10 | pass | https://www.ncaa.com/game/6459158 |
| 2025-11-29 | LSU at Oklahoma | Oklahoma 17, LSU 13 | Oklahoma 17, LSU 13 | final AP top 10 | pass | https://www.ncaa.com/game/6458850 |
| 2025-11-29 | Oregon at Washington | Oregon 26, Washington 14 | Oregon 26, Washington 14 | final AP top 10 | pass | https://www.ncaa.com/game/6459295 |
| 2025-11-29 | Wisconsin at Minnesota | Minnesota 17, Wisconsin 7 | Minnesota 17, Wisconsin 7 | random draw | pass | https://www.ncaa.com/game/6458954 |
| 2025-11-29 | Ohio State at Michigan | Ohio State 27, Michigan 9 | Ohio State 27, Michigan 9 | final AP top 10 | pass | https://www.ncaa.com/game/6459552 |
| 2025-11-29 | Notre Dame at Stanford | Notre Dame 49, Stanford 20 | Notre Dame 49, Stanford 20 | final AP top 10 | pass | https://www.ncaa.com/game/6459501 |
| 2025-11-29 | Texas Tech at West Virginia | Texas Tech 49, West Virginia 0 | Texas Tech 49, West Virginia 0 | final AP top 10 | pass | https://www.ncaa.com/game/6459655 |
| 2025-11-29 | UTEP at Delaware | Delaware 61, UTEP 31 | Delaware 61, UTEP 31 | random draw | pass | https://www.ncaa.com/game/6459330 |
| 2025-11-29 | Army at UTSA | Army 27, UTSA 24 | Army 27, UTSA 24 | random draw | pass | https://www.ncaa.com/game/6458918 |

## Polls

ap_poll.csv: 15 polls from 2025-08-11 to 2025-11-30, 375 rows. Every poll lists exactly 25 teams.

coaches_poll.csv: 15 polls from 2025-08-04 to 2025-11-30, 375 rows. Every poll lists exactly 25 teams.

cfp_rankings.csv: 5 polls from 2025-11-04 to 2025-12-02, 125 rows. Every poll lists exactly 25 teams.

AP polls checked against College Poll Archive (the rank and the team, then the points and the first-place votes, for every ranked team):

| poll date | archive page | teams compared | check | URL |
| --- | --- | --- | --- | --- |
| 2025-08-11 | 2025 Preseason AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1251 |
| 2025-09-02 | September 2, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1252 |
| 2025-09-07 | September 7, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1253 |
| 2025-09-14 | September 14, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1254 |
| 2025-09-21 | September 21, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1255 |
| 2025-09-28 | September 28, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1256 |
| 2025-10-05 | October 5, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1257 |
| 2025-10-12 | October 12, 2025 AP Football Poll | 25 | settled | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1258 |
| 2025-10-19 | October 19, 2025 AP Football Poll | 25 | settled | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1259 |
| 2025-10-26 | October 26, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1260 |
| 2025-11-02 | November 2, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1261 |
| 2025-11-09 | November 9, 2025 AP Football Poll | 25 | settled | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1262 |
| 2025-11-16 | November 16, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1263 |
| 2025-11-23 | November 23, 2025 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1264 |
| 2025-11-30 | November 30, 2025 AP Football Poll | 25 | settled | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1265 |
| 2025-12-07 | December 7, 2025 AP Football Poll |  | not in dataset | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1266 |

Polls where the archive's tallies differ from ours. In each case the primary source and ESPN agree with each other, and a published copy of the poll (named in resolutions.json) confirms our values:

- 2025-10-12: Vanderbilt points: ours 547, archive 548; Virginia points: ours 521, archive 522; USC points: ours 361, archive 353; Memphis points: ours 285, archive 286; Utah points: ours 261, archive 264; Cincinnati points: ours 184, archive 185; Nebraska points: ours 149, archive 148
- 2025-10-19: Georgia Tech points: ours 1143, archive 1144; BYU points: ours 975, archive 974; Oklahoma points: ours 882, archive 883; Virginia points: ours 624, archive 615; Tennessee points: ours 527, archive 528; Louisville points: ours 458, archive 459; LSU points: ours 388, archive 389; Cincinnati points: ours 350, archive 351; Texas points: ours 318, archive 319; Arizona State points: ours 155, archive 156; Michigan points: ours 123, archive 124
- 2025-11-09: Ohio State points: ours 1610, archive 1585; Ohio State first_place_votes: ours 55, archive 54; Indiana points: ours 1549, archive 1525; Texas A&M points: ours 1518, archive 1495; Alabama points: ours 1427, archive 1405; Georgia points: ours 1353, archive 1332; Ole Miss points: ours 1248, archive 1230; Oregon points: ours 1245, archive 1224; Texas Tech points: ours 1211, archive 1193; Notre Dame points: ours 1102, archive 1085; Texas points: ours 961, archive 945; Oklahoma points: ours 928, archive 913; BYU points: ours 898, archive 886; Vanderbilt points: ours 821, archive 807; Georgia Tech points: ours 788, archive 775; Utah points: ours 695, archive 684; Miami points: ours 683, archive 673; USC points: ours 645, archive 636; Michigan points: ours 498, archive 490; Tennessee points: ours 276, archive 269; Cincinnati points: ours 224, archive 218; Pittsburgh points: ours 201, archive 198; James Madison points: ours 167, archive 163; South Florida points: ours 116, archive 115
- 2025-11-30: BYU points: ours 982, archive 980; Vanderbilt points: ours 871, archive 872; Texas points: ours 861, archive 862

## Checksums

Regenerated after the last change and confirmed with `python3 datasets/checksums.py --season 2025 --check`:

```
132adcbbb4d8e769b7b394cc13b746d580473da209d03aeb9ee53dd2f2c5d8f1  ap_poll.csv
659519b4c31934de6c427f7788cc3cc602e5818832f6af807ae364191dabe4d2  cfp_rankings.csv
0abd37f3bb915f409ecdcf3f1e29483b60c9fb0f36bd59bb2a50cbd0006d2d72  coaches_poll.csv
6c8906946d878141072fdeb88b539cd6d1e5a76dd16a33bfd3b7e9f12e4891e4  espn_games.csv
3ed487d71e02fe591b97588b3400220b73a00d7480f9c28e619362b26575e72b  espn_polls.csv
57e8ba5fcded15d610899e0054523a9808c905888f8f4030727defb54c9cd785  games.csv
24b2d571440af47cac5ea6eebaec0e2aaba19220c603dbf624f0b290c707abd6  teams.csv
```

## Notes

Four things in this season's record deserve a sentence of explanation.

1. Eight games carry a neutral-site flag in the primary source that ESPN does not carry. All of them are home games played away from the home team's usual stadium: Sam Houston played its home schedule at Shell Energy Stadium in Houston, Arkansas played Arkansas State at War Memorial Stadium in Little Rock, and Northwestern played Michigan and Minnesota at Wrigley Field. The Wikipedia season page for each school lists these as home games, so the neutral flag is false for each one. The full list is in the cross-check table above.

2. Georgia and Florida met at a neutral site in Jacksonville on November 1. The primary source and ESPN designate Florida as the home team; NCAA.com designates Georgia. We kept the designation that two of the three sources use. Every source agrees on the result.

3. The AP poll released September 2 gives Oregon one first-place vote in ESPN and in College Poll Archive, and none in the primary source. Two sources against one, so the row carries one vote. It is listed in the cross-check table above.

4. Four AP polls (October 12, October 19, November 9, and November 30) have point tallies in College Poll Archive that differ from ours by a point or two per team, and the November 9 archive copy counts one ballot fewer than ours. In every case the primary source and ESPN agree with each other, and a copy of the poll published on the day of release matches our totals. The copies are named in `resolutions.json` and listed under the poll checks above. Not one rank differs.
