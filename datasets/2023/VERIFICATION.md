# Verification record for the 2023 season

This file is written by `datasets/write_verification.py` from the output of the collection, cross-check, and spot-check scripts. Rerun those scripts and this one to rebuild it.

## Counts

Games in games.csv: 857

FBS teams in teams.csv: 133

Opponents from outside FBS: 96 FCS

Data collected at 2026-11-24T19:29:43Z (UTC). Last game in the dataset: 2023-11-25.

Rivalry week is week 13 (the week holding 2023-11-25). The dataset runs through rivalry week.

| week | first game | last game | games |
| --- | --- | --- | --- |
| 0 | 2023-08-26 | 2023-08-26 | 7 |
| 1 | 2023-08-31 | 2023-09-04 | 87 |
| 2 | 2023-09-07 | 2023-09-09 | 85 |
| 3 | 2023-09-14 | 2023-09-16 | 75 |
| 4 | 2023-09-21 | 2023-09-23 | 67 |
| 5 | 2023-09-28 | 2023-09-30 | 59 |
| 6 | 2023-10-04 | 2023-10-07 | 51 |
| 7 | 2023-10-10 | 2023-10-14 | 55 |
| 8 | 2023-10-17 | 2023-10-21 | 54 |
| 9 | 2023-10-24 | 2023-10-28 | 54 |
| 10 | 2023-10-31 | 2023-11-04 | 65 |
| 11 | 2023-11-07 | 2023-11-11 | 65 |
| 12 | 2023-11-14 | 2023-11-18 | 68 |
| 13 | 2023-11-21 | 2023-11-25 | 65 |

Games involving an FBS team that are not in games.csv:

| reason | games |
| --- | --- |
| after rivalry week | 11 |

The full list, one line per game:

- 2023-12-01 Oregon at Washington (Pac-12 Championship): after rivalry week
- 2023-12-01 New Mexico State at Liberty (Conference USA Championship): after rivalry week
- 2023-12-02 SMU at Tulane (American Athletic Championship): after rivalry week
- 2023-12-02 Louisville at Florida State (ACC Championship): after rivalry week
- 2023-12-02 Oklahoma State at Texas (Dr Pepper Big 12 Championship): after rivalry week
- 2023-12-02 Michigan at Iowa (Big Ten Championship): after rivalry week
- 2023-12-02 Miami (OH) at Toledo (MAC Championship): after rivalry week
- 2023-12-02 Boise State at UNLV (Mountain West Championship): after rivalry week
- 2023-12-02 Georgia at Alabama (SEC Championship): after rivalry week
- 2023-12-02 App State at Troy (Sun Belt Championship): after rivalry week
- 2023-12-09 Navy at Army: after rivalry week

## Cross-check against ESPN

Games found in ESPN by id: 857 of 857.

Open disagreements: 0. Completed ESPN games with an FBS team that we lack: 0. Poll rows that disagree: 0.

Values settled by a third source (10 entries in resolutions.json). The primary source and ESPN disagreed on each game row below; for the poll rows the archive disagreed with both. The value kept is the one in the dataset:

| date | game or poll row | field | primary source | other sources | kept | settled by | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2023-09-02 | Western Carolina at Arkansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2023_Arkansas_Razorbacks_football_team | Played at War Memorial Stadium in Little Rock. The schedule lists it as an Arkansas home game, and the season summary counts one neutral-site game for Arkansas, the Texas A&M game in Arlington. |
| 2023-11-24 | Penn State at Michigan State | neutral_site | true | false | true | https://en.wikipedia.org/wiki/2023_Michigan_State_Spartans_football_team | Played at Ford Field in Detroit. The schedule marks the game as a neutral-site game, which agrees with the primary source. |
| 2023-09-02 | North Carolina at South Carolina | home_team | North Carolina | South Carolina | South Carolina | https://www.ncaa.com/game/6154260 and ESPN | Neutral-site game in Charlotte. NCAA.com and ESPN both designate South Carolina as the home team; the primary source designates North Carolina. The winner, the loser, and both teams' scores are the same in every source. |
| 2023-09-02 | North Carolina at South Carolina | away_team | South Carolina | North Carolina | North Carolina | https://www.ncaa.com/game/6154260 and ESPN | Neutral-site game in Charlotte. NCAA.com and ESPN both designate South Carolina as the home team; the primary source designates North Carolina. The winner, the loser, and both teams' scores are the same in every source. |
| 2023-09-02 | North Carolina at South Carolina | home_score | 31 | 17 | 17 | https://www.ncaa.com/game/6154260 and ESPN | Neutral-site game in Charlotte. NCAA.com and ESPN both designate South Carolina as the home team; the primary source designates North Carolina. The winner, the loser, and both teams' scores are the same in every source. |
| 2023-09-02 | North Carolina at South Carolina | away_score | 17 | 31 | 31 | https://www.ncaa.com/game/6154260 and ESPN | Neutral-site game in Charlotte. NCAA.com and ESPN both designate South Carolina as the home team; the primary source designates North Carolina. The winner, the loser, and both teams' scores are the same in every source. |
| 2023-10-28 | Massachusetts at Army | conference_game | true | false | false | datasets/2023/teams.csv (both teams are listed as FBS Independents) | Both teams were FBS Independents. A team with no conference cannot play a conference game, so the primary source's flag is a labeling quirk. |
| 2023-11-25 | UConn at Massachusetts | conference_game | true | false | false | datasets/2023/teams.csv (both teams are listed as FBS Independents) | Both teams were FBS Independents. A team with no conference cannot play a conference game, so the primary source's flag is a labeling quirk. |
| 2023-09-24 | ap_poll.csv Florida State | points | 1351 | ESPN 1351, archive 1366 | 1351 | https://lsusports.net/news/2023/09/24/sept-24-football-national-rankings | College Poll Archive lists different point totals. The primary source and ESPN agree, and a published copy of the poll from the day it was released shows the same totals as ours. |
| 2023-09-24 | ap_poll.csv Florida | points | 235 | ESPN 235, archive 220 | 235 | https://lsusports.net/news/2023/09/24/sept-24-football-national-rankings | College Poll Archive lists different point totals. The primary source and ESPN agree, and a published copy of the poll from the day it was released shows the same totals as ours. |

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
| Hawai'i | 13 |
| Houston | 12 |
| Illinois | 12 |
| Indiana | 12 |
| Iowa | 12 |
| Iowa State | 12 |
| Jacksonville State | 12 |
| James Madison | 12 |
| Kansas | 12 |
| Kansas State | 12 |
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
| NC State | 12 |
| Navy | 11 |
| Nebraska | 12 |
| Nevada | 12 |
| New Mexico | 12 |
| New Mexico State | 13 |
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

Random draw of 25 games with seed 20261124, plus every game of the top 10 in the AP poll of 2023-11-26 (Alabama, Florida State, Georgia, Michigan, Missouri, Ohio State, Oregon, Penn State, Texas, Washington).

Selected games checked: 135. Passed: 135.

Beyond the selection, every game in the season was matched to NCAA.com by date, by score, and by team name: 857 of 857 agree, 0 could not be matched.

| date | game | our result | NCAA.com result | why selected | check | URL |
| --- | --- | --- | --- | --- | --- | --- |
| 2023-08-26 | Florida International at Louisiana Tech | Louisiana Tech 22, Florida International 17 | Louisiana Tech 22, Florida International 17 | random draw | pass | https://www.ncaa.com/game/6154189 |
| 2023-08-31 | Nebraska at Minnesota | Minnesota 13, Nebraska 10 | Minnesota 13, Nebraska 10 | random draw | pass | https://www.ncaa.com/game/6154129 |
| 2023-08-31 | South Dakota at Missouri | Missouri 35, South Dakota 10 | Missouri 35, South Dakota 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154194 |
| 2023-09-02 | Middle Tennessee at Alabama | Alabama 56, Middle Tennessee 7 | Alabama 56, Middle Tennessee 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154252 |
| 2023-09-02 | UT Martin at Georgia | Georgia 48, UT Martin 7 | Georgia 48, UT Martin 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154257 |
| 2023-09-02 | Ohio State at Indiana | Ohio State 23, Indiana 3 | Ohio State 23, Indiana 3 | final AP top 10 | pass | https://www.ncaa.com/game/6154119 |
| 2023-09-02 | East Carolina at Michigan | Michigan 30, East Carolina 3 | Michigan 30, East Carolina 3 | final AP top 10 | pass | https://www.ncaa.com/game/6154949 |
| 2023-09-02 | West Virginia at Penn State | Penn State 38, West Virginia 15 | Penn State 38, West Virginia 15 | final AP top 10 | pass | https://www.ncaa.com/game/6154942 |
| 2023-09-02 | Portland State at Oregon | Oregon 81, Portland State 7 | Oregon 81, Portland State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154212 |
| 2023-09-02 | Boise State at Washington | Washington 56, Boise State 19 | Washington 56, Boise State 19 | final AP top 10 | pass | https://www.ncaa.com/game/6154214 |
| 2023-09-02 | Rice at Texas | Texas 37, Rice 10 | Texas 37, Rice 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154222 |
| 2023-09-03 | LSU at Florida State | Florida State 45, LSU 24 | Florida State 45, LSU 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154264 |
| 2023-09-09 | Texas at Alabama | Texas 34, Alabama 24 | Texas 34, Alabama 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154314 |
| 2023-09-09 | McNeese at Florida | Florida 49, McNeese 7 | Florida 49, McNeese 7 | random draw | pass | https://www.ncaa.com/game/6154331 |
| 2023-09-09 | Ball State at Georgia | Georgia 45, Ball State 3 | Georgia 45, Ball State 3 | final AP top 10 | pass | https://www.ncaa.com/game/6154275 |
| 2023-09-09 | UNLV at Michigan | Michigan 35, UNLV 7 | Michigan 35, UNLV 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154950 |
| 2023-09-09 | Middle Tennessee at Missouri | Missouri 23, Middle Tennessee 19 | Missouri 23, Middle Tennessee 19 | final AP top 10 | pass | https://www.ncaa.com/game/6154313 |
| 2023-09-09 | Youngstown State at Ohio State | Ohio State 35, Youngstown State 7 | Ohio State 35, Youngstown State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154100 |
| 2023-09-09 | Delaware at Penn State | Penn State 63, Delaware 7 | Penn State 63, Delaware 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154943 |
| 2023-09-09 | Oregon at Texas Tech | Oregon 38, Texas Tech 30 | Oregon 38, Texas Tech 30 | final AP top 10 | pass | https://www.ncaa.com/game/6154312 |
| 2023-09-09 | Tulsa at Washington | Washington 43, Tulsa 10 | Washington 43, Tulsa 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154283 |
| 2023-09-09 | Southern Miss at Florida State | Florida State 66, Southern Miss 13 | Florida State 66, Southern Miss 13 | final AP top 10 | pass | https://www.ncaa.com/game/6154336 |
| 2023-09-09 | Fordham at Buffalo | Fordham 40, Buffalo 37 | Fordham 40, Buffalo 37 | random draw | pass | https://www.ncaa.com/game/6154306 |
| 2023-09-16 | Liberty at Buffalo | Liberty 55, Buffalo 27 | Liberty 55, Buffalo 27 | random draw | pass | https://www.ncaa.com/game/6154345 |
| 2023-09-16 | South Carolina at Georgia | Georgia 24, South Carolina 14 | Georgia 24, South Carolina 14 | final AP top 10 | pass | https://www.ncaa.com/game/6154363 |
| 2023-09-16 | Penn State at Illinois | Penn State 30, Illinois 13 | Penn State 30, Illinois 13 | final AP top 10 | pass | https://www.ncaa.com/game/6154172 |
| 2023-09-16 | Bowling Green at Michigan | Michigan 31, Bowling Green 6 | Michigan 31, Bowling Green 6 | final AP top 10 | pass | https://www.ncaa.com/game/6154951 |
| 2023-09-16 | Washington at Michigan State | Washington 41, Michigan State 7 | Washington 41, Michigan State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154947 |
| 2023-09-16 | Kansas State at Missouri | Missouri 30, Kansas State 27 | Missouri 30, Kansas State 27 | final AP top 10 | pass | https://www.ncaa.com/game/6154344 |
| 2023-09-16 | Western Kentucky at Ohio State | Ohio State 63, Western Kentucky 10 | Ohio State 63, Western Kentucky 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154101 |
| 2023-09-16 | Alabama at South Florida | Alabama 17, South Florida 3 | Alabama 17, South Florida 3 | final AP top 10 | pass | https://www.ncaa.com/game/6154365 |
| 2023-09-16 | Hawai'i at Oregon | Oregon 55, Hawai'i 10 | Oregon 55, Hawai'i 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154368 |
| 2023-09-16 | Florida State at Boston College | Florida State 31, Boston College 29 | Florida State 31, Boston College 29 | final AP top 10 | pass | https://www.ncaa.com/game/6154349 |
| 2023-09-16 | Wyoming at Texas | Texas 31, Wyoming 10 | Texas 31, Wyoming 10 | random draw | pass | https://www.ncaa.com/game/6154389 |
| 2023-09-23 | Ole Miss at Alabama | Alabama 24, Ole Miss 10 | Alabama 24, Ole Miss 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154425 |
| 2023-09-23 | UAB at Georgia | Georgia 49, UAB 21 | Georgia 49, UAB 21 | final AP top 10 | pass | https://www.ncaa.com/game/6154426 |
| 2023-09-23 | Memphis at Missouri | Missouri 34, Memphis 27 | Missouri 34, Memphis 27 | final AP top 10 | pass | https://www.ncaa.com/game/6154440 |
| 2023-09-23 | Rutgers at Michigan | Michigan 31, Rutgers 7 | Michigan 31, Rutgers 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154175 |
| 2023-09-23 | Iowa at Penn State | Penn State 31, Iowa 0 | Penn State 31, Iowa 0 | final AP top 10 | pass | https://www.ncaa.com/game/6154096 |
| 2023-09-23 | Ohio State at Notre Dame | Ohio State 17, Notre Dame 14 | Ohio State 17, Notre Dame 14 | final AP top 10 | pass | https://www.ncaa.com/game/6154102 |
| 2023-09-23 | Colorado at Oregon | Oregon 42, Colorado 6 | Oregon 42, Colorado 6 | final AP top 10 | pass | https://www.ncaa.com/game/6154431 |
| 2023-09-23 | California at Washington | Washington 59, California 32 | Washington 59, California 32 | final AP top 10 | pass | https://www.ncaa.com/game/6154456 |
| 2023-09-23 | Florida State at Clemson | Florida State 31, Clemson 24 | Florida State 31, Clemson 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154409 |
| 2023-09-23 | Texas at Baylor | Texas 38, Baylor 6 | Texas 38, Baylor 6 | final AP top 10 | pass | https://www.ncaa.com/game/6154416 |
| 2023-09-28 | Temple at Tulsa | Tulsa 48, Temple 26 | Tulsa 48, Temple 26 | random draw | pass | https://www.ncaa.com/game/6154457 |
| 2023-09-30 | Georgia at Auburn | Georgia 27, Auburn 20 | Georgia 27, Auburn 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154479 |
| 2023-09-30 | Alabama at Mississippi State | Alabama 40, Mississippi State 17 | Alabama 40, Mississippi State 17 | final AP top 10 | pass | https://www.ncaa.com/game/6154470 |
| 2023-09-30 | Michigan at Nebraska | Michigan 45, Nebraska 7 | Michigan 45, Nebraska 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154149 |
| 2023-09-30 | Penn State at Northwestern | Penn State 41, Northwestern 13 | Penn State 41, Northwestern 13 | random draw | pass | https://www.ncaa.com/game/6154177 |
| 2023-09-30 | Missouri at Vanderbilt | Missouri 38, Vanderbilt 21 | Missouri 38, Vanderbilt 21 | final AP top 10 | pass | https://www.ncaa.com/game/6154485 |
| 2023-09-30 | Washington at Arizona | Washington 31, Arizona 24 | Washington 31, Arizona 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154467 |
| 2023-09-30 | Oregon at Stanford | Oregon 42, Stanford 6 | Oregon 42, Stanford 6 | final AP top 10 | pass | https://www.ncaa.com/game/6154495 |
| 2023-09-30 | Kansas at Texas | Texas 40, Kansas 14 | Texas 40, Kansas 14 | final AP top 10 | pass | https://www.ncaa.com/game/6154483 |
| 2023-09-30 | Charlotte at SMU | SMU 34, Charlotte 16 | SMU 34, Charlotte 16 | random draw | pass | https://www.ncaa.com/game/6154464 |
| 2023-09-30 | San Diego State at Air Force | Air Force 49, San Diego State 10 | Air Force 49, San Diego State 10 | random draw | pass | https://www.ncaa.com/game/6154507 |
| 2023-10-07 | Kentucky at Georgia | Georgia 51, Kentucky 13 | Georgia 51, Kentucky 13 | final AP top 10 | pass | https://www.ncaa.com/game/6154534 |
| 2023-10-07 | Michigan at Minnesota | Michigan 52, Minnesota 10 | Michigan 52, Minnesota 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154133 |
| 2023-10-07 | LSU at Missouri | LSU 49, Missouri 39 | LSU 49, Missouri 39 | final AP top 10 | pass | https://www.ncaa.com/game/6154532 |
| 2023-10-07 | Maryland at Ohio State | Ohio State 37, Maryland 17 | Ohio State 37, Maryland 17 | final AP top 10 | pass | https://www.ncaa.com/game/6154120 |
| 2023-10-07 | Alabama at Texas A&M | Alabama 26, Texas A&M 20 | Alabama 26, Texas A&M 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154523 |
| 2023-10-07 | Virginia Tech at Florida State | Florida State 39, Virginia Tech 17 | Florida State 39, Virginia Tech 17 | final AP top 10 | pass | https://www.ncaa.com/game/6154527 |
| 2023-10-07 | William & Mary at Virginia | Virginia 27, William & Mary 13 | Virginia 27, William & Mary 13 | random draw | pass | https://www.ncaa.com/game/6154521 |
| 2023-10-07 | Oklahoma at Texas | Oklahoma 34, Texas 30 | Oklahoma 34, Texas 30 | final AP top 10 | pass | https://www.ncaa.com/game/6154545 |
| 2023-10-07 | South Alabama at UL Monroe | South Alabama 55, UL Monroe 7 | South Alabama 55, UL Monroe 7 | random draw | pass | https://www.ncaa.com/game/6154539 |
| 2023-10-07 | San José State at Boise State | Boise State 35, San José State 27 | Boise State 35, San José State 27 | random draw | pass | https://www.ncaa.com/game/6154553 |
| 2023-10-10 | Liberty at Jacksonville State | Liberty 31, Jacksonville State 13 | Liberty 31, Jacksonville State 13 | random draw | pass | https://www.ncaa.com/game/6154555 |
| 2023-10-10 | Coastal Carolina at App State | Coastal Carolina 27, App State 24 | Coastal Carolina 27, App State 24 | random draw | pass | https://www.ncaa.com/game/6154556 |
| 2023-10-14 | Arkansas at Alabama | Alabama 24, Arkansas 21 | Alabama 24, Arkansas 21 | final AP top 10 | pass | https://www.ncaa.com/game/6154584 |
| 2023-10-14 | Missouri at Kentucky | Missouri 38, Kentucky 21 | Missouri 38, Kentucky 21 | final AP top 10 | pass | https://www.ncaa.com/game/6154575 |
| 2023-10-14 | Indiana at Michigan | Michigan 52, Indiana 7 | Michigan 52, Indiana 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154159 |
| 2023-10-14 | Massachusetts at Penn State | Penn State 63, Massachusetts 0 | Penn State 63, Massachusetts 0 | final AP top 10 | pass | https://www.ncaa.com/game/6154181 |
| 2023-10-14 | Ohio State at Purdue | Ohio State 41, Purdue 7 | Ohio State 41, Purdue 7 | random draw | pass | https://www.ncaa.com/game/6154103 |
| 2023-10-14 | Georgia at Vanderbilt | Georgia 37, Vanderbilt 20 | Georgia 37, Vanderbilt 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154582 |
| 2023-10-14 | Oregon at Washington | Washington 36, Oregon 33 | Washington 36, Oregon 33 | final AP top 10 | pass | https://www.ncaa.com/game/6154580 |
| 2023-10-14 | Syracuse at Florida State | Florida State 41, Syracuse 3 | Florida State 41, Syracuse 3 | final AP top 10 | pass | https://www.ncaa.com/game/6154574 |
| 2023-10-14 | UAB at UTSA | UTSA 41, UAB 20 | UTSA 41, UAB 20 | random draw | pass | https://www.ncaa.com/game/6154587 |
| 2023-10-21 | Tennessee at Alabama | Alabama 34, Tennessee 20 | Alabama 34, Tennessee 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154629 |
| 2023-10-21 | Michigan at Michigan State | Michigan 49, Michigan State 0 | Michigan 49, Michigan State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6154948 |
| 2023-10-21 | South Carolina at Missouri | Missouri 34, South Carolina 12 | Missouri 34, South Carolina 12 | final AP top 10 | pass | https://www.ncaa.com/game/6154627 |
| 2023-10-21 | Penn State at Ohio State | Ohio State 20, Penn State 12 | Ohio State 20, Penn State 12 | final AP top 10 | pass | https://www.ncaa.com/game/6154121 |
| 2023-10-21 | Washington State at Oregon | Oregon 38, Washington State 24 | Oregon 38, Washington State 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154636 |
| 2023-10-21 | Arizona State at Washington | Washington 15, Arizona State 7 | Washington 15, Arizona State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154624 |
| 2023-10-21 | Duke at Florida State | Florida State 38, Duke 20 | Florida State 38, Duke 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154617 |
| 2023-10-21 | Texas at Houston | Texas 31, Houston 24 | Texas 31, Houston 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154619 |
| 2023-10-28 | Georgia at Florida | Georgia 43, Florida 20 | Georgia 43, Florida 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154695 |
| 2023-10-28 | Indiana at Penn State | Penn State 33, Indiana 24 | Penn State 33, Indiana 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154161 |
| 2023-10-28 | Ohio State at Wisconsin | Ohio State 24, Wisconsin 10 | Ohio State 24, Wisconsin 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154122 |
| 2023-10-28 | Washington at Stanford | Washington 42, Stanford 33 | Washington 42, Stanford 33 | final AP top 10 | pass | https://www.ncaa.com/game/6154689 |
| 2023-10-28 | Oregon at Utah | Oregon 35, Utah 6 | Oregon 35, Utah 6 | final AP top 10 | pass | https://www.ncaa.com/game/6154663 |
| 2023-10-28 | Florida State at Wake Forest | Florida State 41, Wake Forest 16 | Florida State 41, Wake Forest 16 | random draw | pass | https://www.ncaa.com/game/6154662 |
| 2023-10-28 | BYU at Texas | Texas 35, BYU 6 | Texas 35, BYU 6 | final AP top 10 | pass | https://www.ncaa.com/game/6154676 |
| 2023-11-04 | LSU at Alabama | Alabama 42, LSU 28 | Alabama 42, LSU 28 | final AP top 10 | pass | https://www.ncaa.com/game/6154735 |
| 2023-11-04 | Missouri at Georgia | Georgia 30, Missouri 21 | Georgia 30, Missouri 21 | final AP top 10 | pass | https://www.ncaa.com/game/6154734 |
| 2023-11-04 | Penn State at Maryland | Penn State 51, Maryland 15 | Penn State 51, Maryland 15 | final AP top 10 | pass | https://www.ncaa.com/game/6154940 |
| 2023-11-04 | Purdue at Michigan | Michigan 41, Purdue 13 | Michigan 41, Purdue 13 | final AP top 10 | pass | https://www.ncaa.com/game/6154145 |
| 2023-11-04 | Ohio State at Rutgers | Ohio State 35, Rutgers 16 | Ohio State 35, Rutgers 16 | final AP top 10 | pass | https://www.ncaa.com/game/6154123 |
| 2023-11-04 | California at Oregon | Oregon 63, California 19 | Oregon 63, California 19 | final AP top 10 | pass | https://www.ncaa.com/game/6154757 |
| 2023-11-04 | Washington at USC | Washington 52, USC 42 | Washington 52, USC 42 | final AP top 10 | pass | https://www.ncaa.com/game/6154740 |
| 2023-11-04 | Florida State at Pittsburgh | Florida State 24, Pittsburgh 7 | Florida State 24, Pittsburgh 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154725 |
| 2023-11-04 | Kansas State at Texas | Texas 33, Kansas State 30 | Texas 33, Kansas State 30 | final AP top 10 | pass | https://www.ncaa.com/game/6154730 |
| 2023-11-04 | Marshall at App State | App State 31, Marshall 9 | App State 31, Marshall 9 | random draw | pass | https://www.ncaa.com/game/6154742 |
| 2023-11-07 | Ball State at Northern Illinois | Ball State 20, Northern Illinois 17 | Ball State 20, Northern Illinois 17 | random draw | pass | https://www.ncaa.com/game/6154760 |
| 2023-11-11 | Ole Miss at Georgia | Georgia 52, Ole Miss 17 | Georgia 52, Ole Miss 17 | final AP top 10 | pass | https://www.ncaa.com/game/6154791 |
| 2023-11-11 | Alabama at Kentucky | Alabama 49, Kentucky 21 | Alabama 49, Kentucky 21 | final AP top 10 | pass | https://www.ncaa.com/game/6154780 |
| 2023-11-11 | Tennessee at Missouri | Missouri 36, Tennessee 7 | Missouri 36, Tennessee 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154790 |
| 2023-11-11 | Michigan State at Ohio State | Ohio State 38, Michigan State 3 | Ohio State 38, Michigan State 3 | final AP top 10 | pass | https://www.ncaa.com/game/6154124 |
| 2023-11-11 | Michigan at Penn State | Michigan 24, Penn State 15 | Michigan 24, Penn State 15 | final AP top 10 | pass | https://www.ncaa.com/game/6154944 |
| 2023-11-11 | Northwestern at Wisconsin | Northwestern 24, Wisconsin 10 | Northwestern 24, Wisconsin 10 | random draw | pass | https://www.ncaa.com/game/6154111 |
| 2023-11-11 | USC at Oregon | Oregon 36, USC 27 | Oregon 36, USC 27 | final AP top 10 | pass | https://www.ncaa.com/game/6154799 |
| 2023-11-11 | Utah at Washington | Washington 35, Utah 28 | Washington 35, Utah 28 | final AP top 10 | pass | https://www.ncaa.com/game/6154783 |
| 2023-11-11 | Miami at Florida State | Florida State 27, Miami 20 | Florida State 27, Miami 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154777 |
| 2023-11-11 | Texas at TCU | Texas 29, TCU 26 | Texas 29, TCU 26 | final AP top 10 | pass | https://www.ncaa.com/game/6154775 |
| 2023-11-11 | San Diego State at Colorado State | Colorado State 22, San Diego State 19 | Colorado State 22, San Diego State 19 | random draw | pass | https://www.ncaa.com/game/6154812 |
| 2023-11-18 | Chattanooga at Alabama | Alabama 66, Chattanooga 10 | Alabama 66, Chattanooga 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154862 |
| 2023-11-18 | Michigan at Maryland | Michigan 31, Maryland 24 | Michigan 31, Maryland 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154941 |
| 2023-11-18 | Florida at Missouri | Missouri 33, Florida 31 | Missouri 33, Florida 31 | final AP top 10 | pass | https://www.ncaa.com/game/6154846 |
| 2023-11-18 | Minnesota at Ohio State | Ohio State 37, Minnesota 3 | Ohio State 37, Minnesota 3 | final AP top 10 | pass | https://www.ncaa.com/game/6154125 |
| 2023-11-18 | Rutgers at Penn State | Penn State 27, Rutgers 6 | Penn State 27, Rutgers 6 | final AP top 10 | pass | https://www.ncaa.com/game/6154936 |
| 2023-11-18 | Georgia at Tennessee | Georgia 38, Tennessee 10 | Georgia 38, Tennessee 10 | final AP top 10 | pass | https://www.ncaa.com/game/6154840 |
| 2023-11-18 | Oregon at Arizona State | Oregon 49, Arizona State 13 | Oregon 49, Arizona State 13 | final AP top 10 | pass | https://www.ncaa.com/game/6154853 |
| 2023-11-18 | Washington at Oregon State | Washington 22, Oregon State 20 | Washington 22, Oregon State 20 | final AP top 10 | pass | https://www.ncaa.com/game/6154831 |
| 2023-11-18 | North Alabama at Florida State | Florida State 58, North Alabama 13 | Florida State 58, North Alabama 13 | final AP top 10 | pass | https://www.ncaa.com/game/6154838 |
| 2023-11-18 | Texas at Iowa State | Texas 26, Iowa State 16 | Texas 26, Iowa State 16 | final AP top 10 | pass | https://www.ncaa.com/game/6154824 |
| 2023-11-24 | Missouri at Arkansas | Missouri 48, Arkansas 14 | Missouri 48, Arkansas 14 | final AP top 10 | pass | https://www.ncaa.com/game/6154888 |
| 2023-11-24 | Penn State at Michigan State | Penn State 42, Michigan State 0 | Penn State 42, Michigan State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6154945 |
| 2023-11-24 | Oregon State at Oregon | Oregon 31, Oregon State 7 | Oregon 31, Oregon State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154889 |
| 2023-11-24 | Texas Tech at Texas | Texas 57, Texas Tech 7 | Texas 57, Texas Tech 7 | final AP top 10 | pass | https://www.ncaa.com/game/6154890 |
| 2023-11-25 | Alabama at Auburn | Alabama 27, Auburn 24 | Alabama 27, Auburn 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154906 |
| 2023-11-25 | Florida State at Florida | Florida State 24, Florida 15 | Florida State 24, Florida 15 | final AP top 10 | pass | https://www.ncaa.com/game/6154891 |
| 2023-11-25 | Georgia at Georgia Tech | Georgia 31, Georgia Tech 23 | Georgia 31, Georgia Tech 23 | final AP top 10 | pass | https://www.ncaa.com/game/6154913 |
| 2023-11-25 | Ohio State at Michigan | Michigan 30, Ohio State 24 | Michigan 30, Ohio State 24 | final AP top 10 | pass | https://www.ncaa.com/game/6154104 |
| 2023-11-25 | Washington State at Washington | Washington 24, Washington State 21 | Washington 24, Washington State 21 | final AP top 10 | pass | https://www.ncaa.com/game/6154908 |
| 2023-11-25 | Virginia Tech at Virginia | Virginia Tech 55, Virginia 17 | Virginia Tech 55, Virginia 17 | random draw | pass | https://www.ncaa.com/game/6154895 |
| 2023-11-25 | Tulsa at East Carolina | Tulsa 29, East Carolina 27 | Tulsa 29, East Carolina 27 | random draw | pass | https://www.ncaa.com/game/6154920 |
| 2023-11-25 | Miami (OH) at Ball State | Miami (OH) 17, Ball State 15 | Miami (OH) 17, Ball State 15 | random draw | pass | https://www.ncaa.com/game/6154916 |

## Polls

ap_poll.csv: 14 polls from 2023-08-14 to 2023-11-26, 350 rows. Every poll lists exactly 25 teams.

coaches_poll.csv: 14 polls from 2023-08-07 to 2023-11-26, 350 rows. Every poll lists exactly 25 teams.

cfp_rankings.csv: 5 polls from 2023-10-31 to 2023-11-28, 125 rows. Every poll lists exactly 25 teams.

AP polls checked against College Poll Archive (the rank and the team, then the points and the first-place votes, for every ranked team):

| poll date | archive page | teams compared | check | URL |
| --- | --- | --- | --- | --- |
| 2023-08-14 | 2023 Preseason AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1218 |
| 2023-09-05 | September 5, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1219 |
| 2023-09-10 | September 10, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1220 |
| 2023-09-17 | September 17, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1221 |
| 2023-09-24 | September 24, 2023 AP Football Poll | 25 | settled | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1222 |
| 2023-10-01 | October 1, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1223 |
| 2023-10-08 | October 8, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1224 |
| 2023-10-15 | October 15, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1225 |
| 2023-10-22 | October 22, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1226 |
| 2023-10-29 | October 29, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1227 |
| 2023-11-05 | November 5, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1228 |
| 2023-11-12 | November 12, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1229 |
| 2023-11-19 | November 19, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1230 |
| 2023-11-26 | November 26, 2023 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1231 |
| 2023-12-03 | December 3, 2023 AP Football Poll |  | not in dataset | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1232 |

Polls where the archive's tallies differ from ours. In each case the primary source and ESPN agree with each other, and a published copy of the poll (named in resolutions.json) confirms our values:

- 2023-09-24: Florida State points: ours 1351, archive 1366; Florida points: ours 235, archive 220

## Checksums

Regenerated after the last change and confirmed with `python3 datasets/checksums.py --season 2023 --check`:

```
834f4afbd56c84e0c3cfd38b6d0fa00de3a9cb28590386efa88a2d3154cb8bb9  ap_poll.csv
f63516c5e41d5359f593f604add3b2b5a81f7db8f15bef98877fd312aee51ad7  cfp_rankings.csv
fa05ea85b3caaba15f1fd5d9b0120876fc4cd02a848540329a7a87cd9435efa2  coaches_poll.csv
527f2a4d37a15f4226e235d497f9cf9740e35585d35c2b6c73ca667267f122b8  espn_games.csv
510ba6d1be68a925e97bc722bf7833c7d4dbf0d322e9f7ee0727f1a13816f6a5  espn_polls.csv
13a13f2380d48d3fb3c81fffd165b1f76521af944a15c1d4cd7117ae0c4046da  games.csv
7e7f4fa44a2801e840d92f75a14ebbd4e77dff7fee77d2646184b0485834fe79  teams.csv
```

## Notes

Three things in this season's record deserve a sentence of explanation.

1. South Carolina and North Carolina met at a neutral site in Charlotte on September 2. Every source agrees on the result (North Carolina 31, South Carolina 17) and on the neutral site. The primary source designated North Carolina as the home team; ESPN and NCAA.com both designated South Carolina. We kept the designation that two of the three sources use, and the change is listed in the cross-check table above. No edge in the graph depends on this designation.

2. The AP poll released September 24 is the one poll where College Poll Archive's tallies differ from ours: it lists Florida State with 1,366 points and Florida with 220, while the primary source and ESPN both list 1,351 and 235. A published copy of the poll from that day (https://lsusports.net/news/2023/09/24/sept-24-football-national-rankings) shows 1,351 and 235, so our values stand. The ranks are the same in every source.

3. Michigan State's game against Penn State on November 24 was played at Ford Field in Detroit. The primary source calls it a neutral site and ESPN does not. The Wikipedia season page for Michigan State marks it as a neutral-site game, so the neutral flag stays true. Arkansas's game against Western Carolina on September 2 went the other way: it was played at War Memorial Stadium in Little Rock, which the Wikipedia season page lists as an Arkansas home game, so its neutral flag is false.
