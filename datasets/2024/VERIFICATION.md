# Verification record for the 2024 season

This file is written by `datasets/write_verification.py` from the output of the collection, cross-check, and spot-check scripts. Rerun those scripts and this one to rebuild it.

## Counts

Games in games.csv: 863

FBS teams in teams.csv: 134

Opponents from outside FBS: 96 FCS

Data collected at 2026-11-24T19:32:41Z (UTC). Last game in the dataset: 2024-11-30.

Rivalry week is week 14 (the week holding 2024-11-30). The dataset runs through rivalry week.

| week | first game | last game | games |
| --- | --- | --- | --- |
| 0 | 2024-08-24 | 2024-08-24 | 4 |
| 1 | 2024-08-29 | 2024-09-02 | 96 |
| 2 | 2024-09-06 | 2024-09-07 | 78 |
| 3 | 2024-09-12 | 2024-09-14 | 63 |
| 4 | 2024-09-19 | 2024-09-21 | 64 |
| 5 | 2024-09-26 | 2024-09-28 | 55 |
| 6 | 2024-10-03 | 2024-10-05 | 49 |
| 7 | 2024-10-08 | 2024-10-12 | 52 |
| 8 | 2024-10-15 | 2024-10-19 | 59 |
| 9 | 2024-10-22 | 2024-10-26 | 57 |
| 10 | 2024-10-29 | 2024-11-02 | 49 |
| 11 | 2024-11-05 | 2024-11-09 | 50 |
| 12 | 2024-11-12 | 2024-11-16 | 55 |
| 13 | 2024-11-19 | 2024-11-23 | 65 |
| 14 | 2024-11-26 | 2024-11-30 | 67 |

Games involving an FBS team that are not in games.csv:

| reason | games |
| --- | --- |
| after rivalry week | 10 |
| not played: no final score in the source | 1 |

The full list, one line per game:

- 2024-09-28 Liberty at App State: not played: no final score in the source
- 2024-12-06 Tulane at Army (American Athletic Championship): after rivalry week
- 2024-12-06 Western Kentucky at Jacksonville State (Conference USA Championship): after rivalry week
- 2024-12-06 UNLV at Boise State (Mountain West Championship): after rivalry week
- 2024-12-07 Clemson at SMU (ACC Championship): after rivalry week
- 2024-12-07 Penn State at Oregon (Big Ten Championship): after rivalry week
- 2024-12-07 Iowa State at Arizona State (Dr Pepper Big 12 Championship): after rivalry week
- 2024-12-07 Ohio at Miami (OH) (MAC Championship): after rivalry week
- 2024-12-07 Georgia at Texas (SEC Championship): after rivalry week
- 2024-12-07 Marshall at Louisiana (Sun Belt Championship): after rivalry week
- 2024-12-14 Navy at Army: after rivalry week

## Cross-check against ESPN

Games found in ESPN by id: 863 of 863.

Open disagreements: 0. Completed ESPN games with an FBS team that we lack: 0. Poll rows that disagree: 0.

Values settled by a third source (20 entries in resolutions.json). The primary source and ESPN disagreed on each game row below; for the poll rows the archive disagreed with both. The value kept is the one in the dataset:

| date | game or poll row | field | primary source | other sources | kept | settled by | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-08-29 | Lindenwood at Kansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Kansas_Jayhawks_football_team | Kansas played its 2024 home games at Children's Mercy Park and Arrowhead Stadium in Kansas City while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-09-13 | UNLV at Kansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Kansas_Jayhawks_football_team | Kansas played its 2024 home games at Children's Mercy Park and Arrowhead Stadium in Kansas City while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-09-28 | TCU at Kansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Kansas_Jayhawks_football_team | Kansas played its 2024 home games at Children's Mercy Park and Arrowhead Stadium in Kansas City while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-10-19 | Houston at Kansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Kansas_Jayhawks_football_team | Kansas played its 2024 home games at Children's Mercy Park and Arrowhead Stadium in Kansas City while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-11-09 | Iowa State at Kansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Kansas_Jayhawks_football_team | Kansas played its 2024 home games at Children's Mercy Park and Arrowhead Stadium in Kansas City while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-11-23 | Colorado at Kansas | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Kansas_Jayhawks_football_team | Kansas played its 2024 home games at Children's Mercy Park and Arrowhead Stadium in Kansas City while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-08-31 | Miami (OH) at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Northwestern_Wildcats_football_team | Northwestern played its 2024 home games at Martin Stadium on campus and one at Wrigley Field while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-09-06 | Duke at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Northwestern_Wildcats_football_team | Northwestern played its 2024 home games at Martin Stadium on campus and one at Wrigley Field while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-09-14 | Eastern Illinois at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Northwestern_Wildcats_football_team | Northwestern played its 2024 home games at Martin Stadium on campus and one at Wrigley Field while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-10-05 | Indiana at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Northwestern_Wildcats_football_team | Northwestern played its 2024 home games at Martin Stadium on campus and one at Wrigley Field while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-10-19 | Wisconsin at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Northwestern_Wildcats_football_team | Northwestern played its 2024 home games at Martin Stadium on campus and one at Wrigley Field while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-11-16 | Ohio State at Northwestern | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_Northwestern_Wildcats_football_team | Northwestern played its 2024 home games at Martin Stadium on campus and one at Wrigley Field while its own stadium was rebuilt. The schedule lists each as a home game. |
| 2024-09-07 | Central Michigan at Florida International | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_FIU_Panthers_football_team | Played at Pitbull Stadium in Miami, which is FIU's own stadium under a sponsor's name. The schedule lists each as a home game. |
| 2024-09-21 | Monmouth at Florida International | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_FIU_Panthers_football_team | Played at Pitbull Stadium in Miami, which is FIU's own stadium under a sponsor's name. The schedule lists each as a home game. |
| 2024-09-28 | Louisiana Tech at Florida International | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_FIU_Panthers_football_team | Played at Pitbull Stadium in Miami, which is FIU's own stadium under a sponsor's name. The schedule lists each as a home game. |
| 2024-10-22 | Sam Houston at Florida International | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_FIU_Panthers_football_team | Played at Pitbull Stadium in Miami, which is FIU's own stadium under a sponsor's name. The schedule lists each as a home game. |
| 2024-10-29 | New Mexico State at Florida International | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_FIU_Panthers_football_team | Played at Pitbull Stadium in Miami, which is FIU's own stadium under a sponsor's name. The schedule lists each as a home game. |
| 2024-11-30 | Middle Tennessee at Florida International | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_FIU_Panthers_football_team | Played at Pitbull Stadium in Miami, which is FIU's own stadium under a sponsor's name. The schedule lists each as a home game. |
| 2024-10-12 | Memphis at South Florida | neutral_site | true | false | false | https://en.wikipedia.org/wiki/2024_South_Florida_Bulls_football_team | Moved to Camping World Stadium in Orlando because of Hurricane Milton. The schedule lists it as a South Florida home game. |
| 2024-11-30 | UConn at Massachusetts | conference_game | true | false | false | datasets/2024/teams.csv (both teams are listed as FBS Independents) | Both teams were FBS Independents. A team with no conference cannot play a conference game, so the primary source's flag is a labeling quirk. |

## Completeness

Games played by each FBS team in the dataset. The most common count is 12.

| team | games |
| --- | --- |
| Air Force | 12 |
| Akron | 12 |
| Alabama | 12 |
| App State | 11 |
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
| Liberty | 11 |
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
| Nevada | 13 |
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

Random draw of 25 games with seed 20261124, plus every game of the top 10 in the AP poll of 2024-12-01 (Boise State, Georgia, Indiana, Notre Dame, Ohio State, Oregon, Penn State, SMU, Tennessee, Texas).

Selected games checked: 138. Passed: 138.

Beyond the selection, every game in the season was matched to NCAA.com on date, scores, and team names: 863 of 863 agree, 0 could not be matched.

| date | game | our result | NCAA.com result | why selected | check | URL |
| --- | --- | --- | --- | --- | --- | --- |
| 2024-08-24 | SMU at Nevada | SMU 29, Nevada 24 | SMU 29, Nevada 24 | final AP top 10 | pass | https://www.ncaa.com/game/6305901 |
| 2024-08-29 | Arkansas-Pine Bluff at Arkansas | Arkansas 70, Arkansas-Pine Bluff 0 | Arkansas 70, Arkansas-Pine Bluff 0 | random draw | pass | https://www.ncaa.com/game/6305947 |
| 2024-08-29 | Sacramento State at San José State | San José State 42, Sacramento State 24 | San José State 42, Sacramento State 24 | random draw | pass | https://www.ncaa.com/game/6306431 |
| 2024-08-29 | SE Louisiana at Tulane | Tulane 52, SE Louisiana 0 | Tulane 52, SE Louisiana 0 | random draw | pass | https://www.ncaa.com/game/6306730 |
| 2024-08-30 | Western Michigan at Wisconsin | Wisconsin 28, Western Michigan 14 | Wisconsin 28, Western Michigan 14 | random draw | pass | https://www.ncaa.com/game/6306193 |
| 2024-08-31 | Miami at Florida | Miami 41, Florida 17 | Miami 41, Florida 17 | random draw | pass | https://www.ncaa.com/game/6305956 |
| 2024-08-31 | Clemson at Georgia | Georgia 34, Clemson 3 | Georgia 34, Clemson 3 | final AP top 10 | pass | https://www.ncaa.com/game/6306369 |
| 2024-08-31 | Chattanooga at Tennessee | Tennessee 69, Chattanooga 3 | Tennessee 69, Chattanooga 3 | final AP top 10 | pass | https://www.ncaa.com/game/6306364 |
| 2024-08-31 | Colorado State at Texas | Texas 52, Colorado State 0 | Texas 52, Colorado State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6306214 |
| 2024-08-31 | Notre Dame at Texas A&M | Notre Dame 23, Texas A&M 13 | Notre Dame 23, Texas A&M 13 | final AP top 10 | pass | https://www.ncaa.com/game/6305925 |
| 2024-08-31 | Florida International at Indiana | Indiana 31, Florida International 7 | Indiana 31, Florida International 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305868 |
| 2024-08-31 | Akron at Ohio State | Ohio State 52, Akron 6 | Ohio State 52, Akron 6 | final AP top 10 | pass | https://www.ncaa.com/game/6305891 |
| 2024-08-31 | Idaho at Oregon | Oregon 24, Idaho 14 | Oregon 24, Idaho 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306161 |
| 2024-08-31 | Penn State at West Virginia | Penn State 34, West Virginia 12 | Penn State 34, West Virginia 12 | final AP top 10 | pass | https://www.ncaa.com/game/6306207 |
| 2024-08-31 | Houston Christian at SMU | SMU 59, Houston Christian 7 | SMU 59, Houston Christian 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305902 |
| 2024-08-31 | Boise State at Georgia Southern | Boise State 56, Georgia Southern 45 | Boise State 56, Georgia Southern 45 | final AP top 10 | pass | https://www.ncaa.com/game/6305978 |
| 2024-09-06 | Western Illinois at Indiana | Indiana 77, Western Illinois 3 | Indiana 77, Western Illinois 3 | final AP top 10 | pass | https://www.ncaa.com/game/6305869 |
| 2024-09-06 | BYU at SMU | BYU 18, SMU 15 | BYU 18, SMU 15 | final AP top 10 | pass | https://www.ncaa.com/game/6305903 |
| 2024-09-07 | Tennessee Tech at Georgia | Georgia 48, Tennessee Tech 3 | Georgia 48, Tennessee Tech 3 | final AP top 10 | pass | https://www.ncaa.com/game/6306370 |
| 2024-09-07 | Tennessee at NC State | Tennessee 51, NC State 10 | Tennessee 51, NC State 10 | final AP top 10 | pass | https://www.ncaa.com/game/6306365 |
| 2024-09-07 | Texas at Michigan | Texas 31, Michigan 12 | Texas 31, Michigan 12 | final AP top 10 | pass | https://www.ncaa.com/game/6306149 |
| 2024-09-07 | Western Michigan at Ohio State | Ohio State 56, Western Michigan 0 | Ohio State 56, Western Michigan 0 | final AP top 10 | pass | https://www.ncaa.com/game/6305892 |
| 2024-09-07 | Boise State at Oregon | Oregon 37, Boise State 34 | Oregon 37, Boise State 34 | final AP top 10 | pass | https://www.ncaa.com/game/6306162 |
| 2024-09-07 | Bowling Green at Penn State | Penn State 34, Bowling Green 27 | Penn State 34, Bowling Green 27 | final AP top 10 | pass | https://www.ncaa.com/game/6306208 |
| 2024-09-07 | Northern Illinois at Notre Dame | Northern Illinois 16, Notre Dame 14 | Northern Illinois 16, Notre Dame 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306286 |
| 2024-09-13 | Arizona at Kansas State | Kansas State 31, Arizona 7 | Kansas State 31, Arizona 7 | random draw | pass | https://www.ncaa.com/game/6306446 |
| 2024-09-14 | Georgia at Kentucky | Georgia 13, Kentucky 12 | Georgia 13, Kentucky 12 | final AP top 10 | pass | https://www.ncaa.com/game/6306359 |
| 2024-09-14 | Kent State at Tennessee | Tennessee 71, Kent State 0 | Tennessee 71, Kent State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6306275 |
| 2024-09-14 | UTSA at Texas | Texas 56, UTSA 7 | Texas 56, UTSA 7 | final AP top 10 | pass | https://www.ncaa.com/game/6306215 |
| 2024-09-14 | Indiana at UCLA | Indiana 42, UCLA 13 | Indiana 42, UCLA 13 | final AP top 10 | pass | https://www.ncaa.com/game/6305870 |
| 2024-09-14 | Oregon at Oregon State | Oregon 49, Oregon State 14 | Oregon 49, Oregon State 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306163 |
| 2024-09-14 | Notre Dame at Purdue | Notre Dame 66, Purdue 7 | Notre Dame 66, Purdue 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305881 |
| 2024-09-21 | Ohio at Kentucky | Kentucky 41, Ohio 6 | Kentucky 41, Ohio 6 | random draw | pass | https://www.ncaa.com/game/6306297 |
| 2024-09-21 | Tennessee at Oklahoma | Tennessee 25, Oklahoma 15 | Tennessee 25, Oklahoma 15 | final AP top 10 | pass | https://www.ncaa.com/game/6306232 |
| 2024-09-21 | UL Monroe at Texas | Texas 51, UL Monroe 3 | Texas 51, UL Monroe 3 | final AP top 10 | pass | https://www.ncaa.com/game/6306216 |
| 2024-09-21 | Charlotte at Indiana | Indiana 52, Charlotte 14 | Indiana 52, Charlotte 14 | random draw | pass | https://www.ncaa.com/game/6305871 |
| 2024-09-21 | Marshall at Ohio State | Ohio State 49, Marshall 14 | Ohio State 49, Marshall 14 | final AP top 10 | pass | https://www.ncaa.com/game/6305893 |
| 2024-09-21 | Kent State at Penn State | Penn State 56, Kent State 0 | Penn State 56, Kent State 0 | final AP top 10 | pass | https://www.ncaa.com/game/6306209 |
| 2024-09-21 | Miami (OH) at Notre Dame | Notre Dame 28, Miami (OH) 3 | Notre Dame 28, Miami (OH) 3 | final AP top 10 | pass | https://www.ncaa.com/game/6306280 |
| 2024-09-21 | TCU at SMU | SMU 66, TCU 42 | SMU 66, TCU 42 | final AP top 10 | pass | https://www.ncaa.com/game/6305904 |
| 2024-09-21 | Kansas at West Virginia | West Virginia 32, Kansas 28 | West Virginia 32, Kansas 28 | random draw | pass | https://www.ncaa.com/game/6306420 |
| 2024-09-21 | Portland State at Boise State | Boise State 56, Portland State 14 | Boise State 56, Portland State 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306595 |
| 2024-09-21 | Eastern Washington at Nevada | Nevada 49, Eastern Washington 16 | Nevada 49, Eastern Washington 16 | random draw | pass | https://www.ncaa.com/game/6306582 |
| 2024-09-28 | Georgia at Alabama | Alabama 41, Georgia 34 | Alabama 41, Georgia 34 | final AP top 10 | pass | https://www.ncaa.com/game/6306371 |
| 2024-09-28 | Mississippi State at Texas | Texas 35, Mississippi State 13 | Texas 35, Mississippi State 13 | final AP top 10 | pass | https://www.ncaa.com/game/6306076 |
| 2024-09-28 | Illinois at Penn State | Penn State 21, Illinois 7 | Penn State 21, Illinois 7 | final AP top 10 | pass | https://www.ncaa.com/game/6306158 |
| 2024-09-28 | Maryland at Indiana | Indiana 42, Maryland 28 | Indiana 42, Maryland 28 | final AP top 10 | pass | https://www.ncaa.com/game/6305872 |
| 2024-09-28 | Minnesota at Michigan | Michigan 27, Minnesota 24 | Michigan 27, Minnesota 24 | random draw | pass | https://www.ncaa.com/game/6306005 |
| 2024-09-28 | Ohio State at Michigan State | Ohio State 38, Michigan State 7 | Ohio State 38, Michigan State 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305894 |
| 2024-09-28 | Oregon at UCLA | Oregon 34, UCLA 13 | Oregon 34, UCLA 13 | final AP top 10 | pass | https://www.ncaa.com/game/6306164 |
| 2024-09-28 | Louisville at Notre Dame | Notre Dame 31, Louisville 24 | Notre Dame 31, Louisville 24 | final AP top 10 | pass | https://www.ncaa.com/game/6306303 |
| 2024-09-28 | Florida State at SMU | SMU 42, Florida State 16 | SMU 42, Florida State 16 | final AP top 10 | pass | https://www.ncaa.com/game/6305905 |
| 2024-09-28 | Washington State at Boise State | Boise State 45, Washington State 24 | Boise State 45, Washington State 24 | final AP top 10 | pass | https://www.ncaa.com/game/6306564 |
| 2024-09-28 | South Florida at Tulane | Tulane 45, South Florida 10 | Tulane 45, South Florida 10 | random draw | pass | https://www.ncaa.com/game/6306731 |
| 2024-10-04 | Michigan State at Oregon | Oregon 31, Michigan State 10 | Oregon 31, Michigan State 10 | final AP top 10 | pass | https://www.ncaa.com/game/6306085 |
| 2024-10-05 | Tennessee at Arkansas | Arkansas 19, Tennessee 14 | Arkansas 19, Tennessee 14 | final AP top 10 | pass | https://www.ncaa.com/game/6305951 |
| 2024-10-05 | Auburn at Georgia | Georgia 31, Auburn 13 | Georgia 31, Auburn 13 | final AP top 10 | pass | https://www.ncaa.com/game/6306372 |
| 2024-10-05 | Indiana at Northwestern | Indiana 41, Northwestern 24 | Indiana 41, Northwestern 24 | final AP top 10 | pass | https://www.ncaa.com/game/6305873 |
| 2024-10-05 | Iowa at Ohio State | Ohio State 35, Iowa 7 | Ohio State 35, Iowa 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305895 |
| 2024-10-05 | UCLA at Penn State | Penn State 27, UCLA 11 | Penn State 27, UCLA 11 | final AP top 10 | pass | https://www.ncaa.com/game/6306205 |
| 2024-10-05 | SMU at Louisville | SMU 34, Louisville 27 | SMU 34, Louisville 27 | final AP top 10 | pass | https://www.ncaa.com/game/6305906 |
| 2024-10-05 | Utah State at Boise State | Boise State 62, Utah State 30 | Boise State 62, Utah State 30 | final AP top 10 | pass | https://www.ncaa.com/game/6306596 |
| 2024-10-05 | East Carolina at Charlotte | Charlotte 55, East Carolina 24 | Charlotte 55, East Carolina 24 | random draw | pass | https://www.ncaa.com/game/6306699 |
| 2024-10-12 | Mississippi State at Georgia | Georgia 41, Mississippi State 31 | Georgia 41, Mississippi State 31 | final AP top 10 | pass | https://www.ncaa.com/game/6306077 |
| 2024-10-12 | Texas at Oklahoma | Texas 34, Oklahoma 3 | Texas 34, Oklahoma 3 | final AP top 10 | pass | https://www.ncaa.com/game/6306217 |
| 2024-10-12 | Florida at Tennessee | Tennessee 23, Florida 17 | Tennessee 23, Florida 17 | final AP top 10 | pass | https://www.ncaa.com/game/6305960 |
| 2024-10-12 | Ohio State at Oregon | Oregon 32, Ohio State 31 | Oregon 32, Ohio State 31 | final AP top 10 | pass | https://www.ncaa.com/game/6305896 |
| 2024-10-12 | Penn State at USC | Penn State 33, USC 30 | Penn State 33, USC 30 | final AP top 10 | pass | https://www.ncaa.com/game/6306199 |
| 2024-10-12 | Stanford at Notre Dame | Notre Dame 49, Stanford 7 | Notre Dame 49, Stanford 7 | final AP top 10 | pass | https://www.ncaa.com/game/6306304 |
| 2024-10-12 | Boise State at Hawai'i | Boise State 28, Hawai'i 7 | Boise State 28, Hawai'i 7 | final AP top 10 | pass | https://www.ncaa.com/game/6306597 |
| 2024-10-12 | Marshall at Georgia Southern | Georgia Southern 24, Marshall 23 | Georgia Southern 24, Marshall 23 | random draw | pass | https://www.ncaa.com/game/6305983 |
| 2024-10-12 | Southern Miss at UL Monroe | UL Monroe 38, Southern Miss 21 | UL Monroe 38, Southern Miss 21 | random draw | pass | https://www.ncaa.com/game/6306029 |
| 2024-10-18 | Oregon at Purdue | Oregon 35, Purdue 0 | Oregon 35, Purdue 0 | final AP top 10 | pass | https://www.ncaa.com/game/6305886 |
| 2024-10-19 | South Carolina at Oklahoma | South Carolina 35, Oklahoma 9 | South Carolina 35, Oklahoma 9 | random draw | pass | https://www.ncaa.com/game/6306061 |
| 2024-10-19 | Alabama at Tennessee | Tennessee 24, Alabama 17 | Tennessee 24, Alabama 17 | final AP top 10 | pass | https://www.ncaa.com/game/6306366 |
| 2024-10-19 | Georgia at Texas | Georgia 30, Texas 15 | Georgia 30, Texas 15 | final AP top 10 | pass | https://www.ncaa.com/game/6306218 |
| 2024-10-19 | Nebraska at Indiana | Indiana 56, Nebraska 7 | Indiana 56, Nebraska 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305874 |
| 2024-10-19 | Notre Dame at Georgia Tech | Notre Dame 31, Georgia Tech 13 | Notre Dame 31, Georgia Tech 13 | final AP top 10 | pass | https://www.ncaa.com/game/6306305 |
| 2024-10-19 | SMU at Stanford | SMU 40, Stanford 10 | SMU 40, Stanford 10 | final AP top 10 | pass | https://www.ncaa.com/game/6305907 |
| 2024-10-19 | Hawai'i at Washington State | Washington State 42, Hawai'i 10 | Washington State 42, Hawai'i 10 | random draw | pass | https://www.ncaa.com/game/6306566 |
| 2024-10-25 | Boise State at UNLV | Boise State 29, UNLV 24 | Boise State 29, UNLV 24 | final AP top 10 | pass | https://www.ncaa.com/game/6306592 |
| 2024-10-26 | Texas at Vanderbilt | Texas 27, Vanderbilt 24 | Texas 27, Vanderbilt 24 | final AP top 10 | pass | https://www.ncaa.com/game/6306219 |
| 2024-10-26 | Illinois at Oregon | Oregon 38, Illinois 9 | Oregon 38, Illinois 9 | final AP top 10 | pass | https://www.ncaa.com/game/6306159 |
| 2024-10-26 | Washington at Indiana | Indiana 31, Washington 17 | Indiana 31, Washington 17 | final AP top 10 | pass | https://www.ncaa.com/game/6305875 |
| 2024-10-26 | Nebraska at Ohio State | Ohio State 21, Nebraska 17 | Ohio State 21, Nebraska 17 | final AP top 10 | pass | https://www.ncaa.com/game/6305897 |
| 2024-10-26 | Penn State at Wisconsin | Penn State 28, Wisconsin 13 | Penn State 28, Wisconsin 13 | final AP top 10 | pass | https://www.ncaa.com/game/6306197 |
| 2024-10-26 | Notre Dame at Navy | Notre Dame 51, Navy 14 | Notre Dame 51, Navy 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306306 |
| 2024-10-26 | SMU at Duke | SMU 28, Duke 27 | SMU 28, Duke 27 | final AP top 10 | pass | https://www.ncaa.com/game/6305908 |
| 2024-10-26 | Cincinnati at Colorado | Colorado 34, Cincinnati 23 | Colorado 34, Cincinnati 23 | random draw | pass | https://www.ncaa.com/game/6306520 |
| 2024-11-01 | San Diego State at Boise State | Boise State 56, San Diego State 24 | Boise State 56, San Diego State 24 | final AP top 10 | pass | https://www.ncaa.com/game/6306598 |
| 2024-11-02 | Florida at Georgia | Georgia 34, Florida 20 | Georgia 34, Florida 20 | final AP top 10 | pass | https://www.ncaa.com/game/6305962 |
| 2024-11-02 | Kentucky at Tennessee | Tennessee 28, Kentucky 18 | Tennessee 28, Kentucky 18 | final AP top 10 | pass | https://www.ncaa.com/game/6306361 |
| 2024-11-02 | Indiana at Michigan State | Indiana 47, Michigan State 10 | Indiana 47, Michigan State 10 | final AP top 10 | pass | https://www.ncaa.com/game/6305876 |
| 2024-11-02 | Oregon at Michigan | Oregon 38, Michigan 17 | Oregon 38, Michigan 17 | final AP top 10 | pass | https://www.ncaa.com/game/6306154 |
| 2024-11-02 | Ohio State at Penn State | Ohio State 20, Penn State 13 | Ohio State 20, Penn State 13 | final AP top 10 | pass | https://www.ncaa.com/game/6305898 |
| 2024-11-02 | Pittsburgh at SMU | SMU 48, Pittsburgh 25 | SMU 48, Pittsburgh 25 | final AP top 10 | pass | https://www.ncaa.com/game/6305909 |
| 2024-11-02 | Coastal Carolina at Troy | Troy 38, Coastal Carolina 24 | Troy 38, Coastal Carolina 24 | random draw | pass | https://www.ncaa.com/game/6306338 |
| 2024-11-09 | Georgia at Ole Miss | Ole Miss 28, Georgia 10 | Ole Miss 28, Georgia 10 | final AP top 10 | pass | https://www.ncaa.com/game/6306072 |
| 2024-11-09 | Mississippi State at Tennessee | Tennessee 33, Mississippi State 14 | Tennessee 33, Mississippi State 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306079 |
| 2024-11-09 | Florida at Texas | Texas 49, Florida 17 | Texas 49, Florida 17 | final AP top 10 | pass | https://www.ncaa.com/game/6305963 |
| 2024-11-09 | Michigan at Indiana | Indiana 20, Michigan 15 | Indiana 20, Michigan 15 | final AP top 10 | pass | https://www.ncaa.com/game/6305877 |
| 2024-11-09 | Maryland at Oregon | Oregon 39, Maryland 18 | Oregon 39, Maryland 18 | final AP top 10 | pass | https://www.ncaa.com/game/6306144 |
| 2024-11-09 | Purdue at Ohio State | Ohio State 45, Purdue 0 | Ohio State 45, Purdue 0 | final AP top 10 | pass | https://www.ncaa.com/game/6305888 |
| 2024-11-09 | Washington at Penn State | Penn State 35, Washington 6 | Penn State 35, Washington 6 | final AP top 10 | pass | https://www.ncaa.com/game/6306210 |
| 2024-11-09 | Florida State at Notre Dame | Notre Dame 52, Florida State 3 | Notre Dame 52, Florida State 3 | final AP top 10 | pass | https://www.ncaa.com/game/6306050 |
| 2024-11-09 | Nevada at Boise State | Boise State 28, Nevada 21 | Boise State 28, Nevada 21 | final AP top 10 | pass | https://www.ncaa.com/game/6306586 |
| 2024-11-12 | Ball State at Buffalo | Buffalo 51, Ball State 48 | Buffalo 51, Ball State 48 | random draw | pass | https://www.ncaa.com/game/6306097 |
| 2024-11-14 | East Carolina at Tulsa | East Carolina 38, Tulsa 31 | East Carolina 38, Tulsa 31 | random draw | pass | https://www.ncaa.com/game/6306695 |
| 2024-11-16 | Texas at Arkansas | Texas 20, Arkansas 10 | Texas 20, Arkansas 10 | final AP top 10 | pass | https://www.ncaa.com/game/6305954 |
| 2024-11-16 | Tennessee at Georgia | Georgia 31, Tennessee 17 | Georgia 31, Tennessee 17 | final AP top 10 | pass | https://www.ncaa.com/game/6306367 |
| 2024-11-16 | Ohio State at Northwestern | Ohio State 31, Northwestern 7 | Ohio State 31, Northwestern 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305899 |
| 2024-11-16 | Oregon at Wisconsin | Oregon 16, Wisconsin 13 | Oregon 16, Wisconsin 13 | final AP top 10 | pass | https://www.ncaa.com/game/6306165 |
| 2024-11-16 | Penn State at Purdue | Penn State 49, Purdue 10 | Penn State 49, Purdue 10 | final AP top 10 | pass | https://www.ncaa.com/game/6305889 |
| 2024-11-16 | Virginia at Notre Dame | Notre Dame 35, Virginia 14 | Notre Dame 35, Virginia 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306307 |
| 2024-11-16 | Boston College at SMU | SMU 38, Boston College 28 | SMU 38, Boston College 28 | final AP top 10 | pass | https://www.ncaa.com/game/6305910 |
| 2024-11-16 | Boise State at San José State | Boise State 42, San José State 21 | Boise State 42, San José State 21 | final AP top 10 | pass | https://www.ncaa.com/game/6306437 |
| 2024-11-19 | Northern Illinois at Miami (OH) | Miami (OH) 20, Northern Illinois 9 | Miami (OH) 20, Northern Illinois 9 | random draw | pass | https://www.ncaa.com/game/6306284 |
| 2024-11-23 | Massachusetts at Georgia | Georgia 59, Massachusetts 21 | Georgia 59, Massachusetts 21 | final AP top 10 | pass | https://www.ncaa.com/game/6306301 |
| 2024-11-23 | UTEP at Tennessee | Tennessee 56, UTEP 0 | Tennessee 56, UTEP 0 | final AP top 10 | pass | https://www.ncaa.com/game/6306368 |
| 2024-11-23 | Kentucky at Texas | Texas 31, Kentucky 14 | Texas 31, Kentucky 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306220 |
| 2024-11-23 | Indiana at Ohio State | Ohio State 38, Indiana 15 | Ohio State 38, Indiana 15 | final AP top 10 | pass | https://www.ncaa.com/game/6305878 |
| 2024-11-23 | Penn State at Minnesota | Penn State 26, Minnesota 25 | Penn State 26, Minnesota 25 | final AP top 10 | pass | https://www.ncaa.com/game/6306011 |
| 2024-11-23 | Washington State at Oregon State | Oregon State 41, Washington State 38 | Oregon State 41, Washington State 38 | random draw | pass | https://www.ncaa.com/game/6306244 |
| 2024-11-23 | SMU at Virginia | SMU 33, Virginia 7 | SMU 33, Virginia 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305911 |
| 2024-11-23 | Cincinnati at Kansas State | Kansas State 41, Cincinnati 15 | Kansas State 41, Cincinnati 15 | random draw | pass | https://www.ncaa.com/game/6306521 |
| 2024-11-23 | Army at Notre Dame | Notre Dame 49, Army 14 | Notre Dame 49, Army 14 | final AP top 10 | pass | https://www.ncaa.com/game/6306308 |
| 2024-11-23 | Boise State at Wyoming | Boise State 17, Wyoming 13 | Boise State 17, Wyoming 13 | final AP top 10 | pass | https://www.ncaa.com/game/6306599 |
| 2024-11-29 | Georgia Tech at Georgia | Georgia 44, Georgia Tech 42 | Georgia 44, Georgia Tech 42 | final AP top 10 | pass | https://www.ncaa.com/game/6306373 |
| 2024-11-29 | Oregon State at Boise State | Boise State 34, Oregon State 18 | Boise State 34, Oregon State 18 | final AP top 10 | pass | https://www.ncaa.com/game/6306245 |
| 2024-11-29 | Navy at East Carolina | Navy 34, East Carolina 20 | Navy 34, East Carolina 20 | random draw | pass | https://www.ncaa.com/game/6306701 |
| 2024-11-30 | Texas at Texas A&M | Texas 17, Texas A&M 7 | Texas 17, Texas A&M 7 | final AP top 10 | pass | https://www.ncaa.com/game/6305935 |
| 2024-11-30 | Tennessee at Vanderbilt | Tennessee 36, Vanderbilt 23 | Tennessee 36, Vanderbilt 23 | final AP top 10 | pass | https://www.ncaa.com/game/6306358 |
| 2024-11-30 | Purdue at Indiana | Indiana 66, Purdue 0 | Indiana 66, Purdue 0 | final AP top 10 | pass | https://www.ncaa.com/game/6305879 |
| 2024-11-30 | Maryland at Penn State | Penn State 44, Maryland 7 | Penn State 44, Maryland 7 | final AP top 10 | pass | https://www.ncaa.com/game/6306146 |
| 2024-11-30 | Michigan at Ohio State | Michigan 13, Ohio State 10 | Michigan 13, Ohio State 10 | final AP top 10 | pass | https://www.ncaa.com/game/6305900 |
| 2024-11-30 | Washington at Oregon | Oregon 49, Washington 21 | Oregon 49, Washington 21 | final AP top 10 | pass | https://www.ncaa.com/game/6306166 |
| 2024-11-30 | Notre Dame at USC | Notre Dame 49, USC 35 | Notre Dame 49, USC 35 | final AP top 10 | pass | https://www.ncaa.com/game/6306202 |
| 2024-11-30 | California at SMU | SMU 38, California 6 | SMU 38, California 6 | final AP top 10 | pass | https://www.ncaa.com/game/6305912 |

## Polls

ap_poll.csv: 15 polls from 2024-08-12 to 2024-12-01, 376 rows. Polls without exactly 25 teams: 2024-09-29 (26 teams).

coaches_poll.csv: 15 polls from 2024-08-05 to 2024-12-01, 375 rows. Every poll lists exactly 25 teams.

cfp_rankings.csv: 5 polls from 2024-11-05 to 2024-12-03, 125 rows. Every poll lists exactly 25 teams.

- Build note: AP Top 25 released 2024-09-29 lists 26 teams

AP polls checked against College Poll Archive (rank, team, points, and first-place votes for every ranked team):

| poll date | archive page | teams compared | check | URL |
| --- | --- | --- | --- | --- |
| 2024-08-12 | 2024 Preseason AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1234 |
| 2024-09-03 | September 3, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1235 |
| 2024-09-08 | September 8, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1236 |
| 2024-09-15 | September 15, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1237 |
| 2024-09-22 | September 22, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1238 |
| 2024-09-29 | September 29, 2024 AP Football Poll | 26 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1239 |
| 2024-10-06 | October 6, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1240 |
| 2024-10-13 | October 13, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1241 |
| 2024-10-20 | October 20, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1242 |
| 2024-10-27 | October 27, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1243 |
| 2024-11-03 | November 3, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1244 |
| 2024-11-10 | November 10, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1245 |
| 2024-11-17 | November 17, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1246 |
| 2024-11-24 | November 24, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1247 |
| 2024-12-01 | December 1, 2024 AP Football Poll | 25 | pass | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1248 |
| 2024-12-08 | December 8, 2024 AP Football Poll |  | not in dataset | https://www.collegepollarchive.com/football/ap/seasons.cfm?appollid=1249 |

## Checksums

Regenerated after the last change and confirmed with `python3 datasets/checksums.py --season 2024 --check`:

```
dc35177507e005d2d343a0b9d6aad9568dd4d4f51b1c6712b6c9e6a416c91a75  ap_poll.csv
3300a97ed46c4e4d10fb9bba88ccc2df0d2f1118f3c30ac9d4c22d63539bad4d  cfp_rankings.csv
cd3ed1b7ec753787ecef9a3de824073ef2f533b93820bb32c998af0817e8912a  coaches_poll.csv
9cb39d0b7eb820fb82e507857c51be28b9408d79cc3ba8cc15e87bb24ff1831f  espn_games.csv
aec740e2f117db4f86c5b4e50e9379eec40d468cb243c549ce2875edf5ee499f  espn_polls.csv
d04b7eea8762a305903379ae313e65ba4437aef5dcea72ee3d13286d2bb7190e  games.csv
cfccfabbabadd89abbbdab5e40db987e565fbceae0add207d9324d09016aef74  teams.csv
```

## Notes

Three things in this season's record deserve a sentence of explanation.

1. The one game involving an FBS team that was scheduled and never played is App State at Liberty on September 28, cancelled because of Hurricane Helene. It is listed under the excluded games above.

2. Nineteen games carry a neutral-site flag in the primary source that ESPN does not carry. All of them are home games played away from the home team's usual stadium: Kansas played at Children's Mercy Park and Arrowhead Stadium while its stadium was rebuilt, Northwestern played at a temporary field on campus and once at Wrigley Field while its stadium was rebuilt, FIU played at its own stadium under a sponsor's name, and South Florida moved one game to Orlando because of Hurricane Milton. The Wikipedia season page for each school lists these as home games, so the neutral flag is false for each one. The full list is in the cross-check table above.

3. The AP poll released September 29 lists 26 teams because two teams tied for 25th. The primary source, ESPN, and College Poll Archive all list the same 26.
