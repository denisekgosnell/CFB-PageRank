# CFB-PageRank
# Copyright 2026 Denise Koessler Gosnell
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Download the raw records for one season and cache them on disk.

This is the only script in the repository that needs the network. Every
other script reads the files this one writes.

What it reads
    Nothing from the repository. It calls three public sources:
    1. The College Football Data API (games, FBS teams, and polls).
    2. ESPN's scoreboard and rankings endpoints (the cross-check source).
    3. NCAA.com's weekly scoreboard pages (the third source for game spot checks).
    4. College Poll Archive's AP poll pages (the third source for poll spot checks).

What it writes
    datasets/_raw/<season>/*.json and *.html, one file per request, plus
    datasets/_raw/<season>/manifest.json, which records the URL, the time,
    the size, and the SHA-256 of every file. The _raw folder is ignored by
    git because it is large and because every file in it can be rebuilt by
    running this script again.

How to run it
    python3 datasets/collect.py --season 2024
    python3 datasets/collect.py --season 2024 --refresh   (download again)

About the API key
    The College Football Data API needs a key. When this script runs in the
    cloud environment that built this repository, the proxy adds the key to
    each request. On your own machine, set the environment variable
    CFBD_API_KEY and this script will send it as a bearer token. The key is
    never written to disk.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

CFBD = "https://api.collegefootballdata.com"
ESPN_SITE = "https://site.api.espn.com/apis/site/v2/sports/football/college-football"
ESPN_CORE = "https://sports.core.api.espn.com/v2/sports/football/leagues/college-football"
NCAA = "https://www.ncaa.com/scoreboard/football/fbs"
POLL_ARCHIVE = "https://www.collegepollarchive.com/football/ap"

# ESPN numbers the polls. These three are the ones this repository keeps.
ESPN_POLL_IDS = {"1": "ap", "2": "coaches", "21": "cfp"}

# The regular season never runs past this many weeks in the sources.
MAX_WEEKS = 16

# A short pause between requests so we stay well inside every rate limit.
PAUSE_SECONDS = 0.4

RAW_ROOT = Path(__file__).resolve().parent / "_raw"


def fetch(url, needs_key=False):
    """Download one URL and return its bytes.

    A dropped connection is retried three times with a growing pause. An
    HTTP error is raised to the caller, which decides what to do with it.
    """
    request = urllib.request.Request(url, headers={"User-Agent": "CFB-PageRank/1.0"})
    key = os.environ.get("CFBD_API_KEY")
    if needs_key and key:
        request.add_header("Authorization", "Bearer " + key)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return response.read()
        except (urllib.error.URLError, ConnectionError, TimeoutError) as error:
            if isinstance(error, urllib.error.HTTPError) or attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


def save(raw_dir, name, url, needs_key, manifest, refresh):
    """Fetch one URL into raw_dir/name unless it is already there.

    The manifest is written after every download so that a run that stops
    partway leaves an accurate record of what it fetched.
    """
    path = raw_dir / name
    if path.exists() and not refresh and name in manifest:
        return path
    try:
        body = fetch(url, needs_key)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            # Some weeks do not exist yet (for example late weeks of a season
            # still in progress). Record the miss and move on.
            manifest[name] = {"url": url, "status": 404, "fetched_at": now()}
            return None
        raise
    path.write_bytes(body)
    manifest[name] = {
        "url": url,
        "status": 200,
        "fetched_at": now(),
        "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(),
    }
    (raw_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    time.sleep(PAUSE_SECONDS)
    return path


def now():
    """The current time in UTC as an ISO 8601 string."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def collect_cfbd(season, raw_dir, manifest, refresh):
    """The primary source: FBS teams, every regular-season game, every poll."""
    save(raw_dir, "cfbd_teams_fbs.json", f"{CFBD}/teams/fbs?year={season}", True, manifest, refresh)
    save(raw_dir, "cfbd_games_regular.json", f"{CFBD}/games?year={season}&seasonType=regular", True, manifest, refresh)
    save(raw_dir, "cfbd_rankings_regular.json", f"{CFBD}/rankings?year={season}&seasonType=regular", True, manifest, refresh)


def game_days(raw_dir):
    """Every Eastern calendar day with a game involving an FBS team, plus the day after.

    ESPN's scoreboard answers one day at a time, so we ask for each day that
    the primary source says a game was played. The day after is included
    because a late kickoff can be filed under the next day.
    """
    games = json.loads((raw_dir / "cfbd_games_regular.json").read_text())
    days = set()
    for game in games:
        if "fbs" not in (game.get("homeClassification"), game.get("awayClassification")):
            continue
        moment = datetime.fromisoformat(game["startDate"].replace("Z", "+00:00")).astimezone(ZoneInfo("America/New_York"))
        days.add(moment.date())
        days.add(moment.date() + timedelta(days=1))
    return sorted(days)


def collect_espn(season, raw_dir, manifest, refresh):
    """The cross-check source: one scoreboard per game day and the polls per week."""
    for day in game_days(raw_dir):
        url = f"{ESPN_SITE}/scoreboard?dates={day:%Y%m%d}&groups=80&limit=500"
        save(raw_dir, f"espn_scoreboard_{day:%Y%m%d}.json", url, False, manifest, refresh)
    # The preseason polls live under season type 1 in some seasons and under
    # week 1 of the regular season (type 2) in others, so we fetch both.
    weeks = [("preseason", f"{ESPN_CORE}/seasons/{season}/types/1/weeks/1/rankings")]
    weeks += [(f"{week:02d}", f"{ESPN_CORE}/seasons/{season}/types/2/weeks/{week}/rankings") for week in range(1, MAX_WEEKS + 1)]
    for label, url in weeks:
        listing = save(raw_dir, f"espn_rankings_week_{label}_list.json", url, False, manifest, refresh)
        if listing is None:
            continue
        for item in json.loads(listing.read_text())["items"]:
            ref = item["$ref"].replace("http://", "https://")
            poll_id = ref.split("/rankings/")[1].split("?")[0]
            if poll_id in ESPN_POLL_IDS:
                save(raw_dir, f"espn_rankings_week_{label}_{ESPN_POLL_IDS[poll_id]}.json", ref, False, manifest, refresh)


def collect_ncaa(season, raw_dir, manifest, refresh):
    """The third source: NCAA.com's weekly FBS scoreboard pages."""
    for week in range(1, MAX_WEEKS + 1):
        save(raw_dir, f"ncaa_scoreboard_week_{week:02d}.html", f"{NCAA}/{season}/{week:02d}", False, manifest, refresh)


def collect_poll_archive(season, raw_dir, manifest, refresh):
    """The third source for polls: College Poll Archive, one page per AP poll.

    The season index page links only to the newest poll and its neighbors,
    so we walk backward through the "previous poll" links until we reach a
    poll released before August of the season.
    """
    index = save(raw_dir, "cpa_index.html", f"{POLL_ARCHIVE}/seasons.cfm?seasonid={season}", False, manifest, refresh)
    if index is None:
        return
    text = index.read_text(encoding="utf-8", errors="replace")
    ids = sorted({int(i) for i in re.findall(r"seasons\.cfm\?appollid=(\d+)", text)})
    if not ids:
        return
    # The smaller id on the index page is the previous poll. The larger id is
    # the next season's first poll, which we do not need.
    poll_id = ids[0]
    for _ in range(40):
        page = save(raw_dir, f"cpa_poll_{poll_id}.html", f"{POLL_ARCHIVE}/seasons.cfm?appollid={poll_id}", False, manifest, refresh)
        if page is None:
            return
        body = page.read_text(encoding="utf-8", errors="replace")
        title = re.search(r"<title>(.*?)</title>", body, re.S)
        if title and str(season) not in title.group(1):
            page.unlink()
            del manifest[f"cpa_poll_{poll_id}.html"]
            return
        earlier = [int(i) for i in re.findall(r"seasons\.cfm\?appollid=(\d+)", body) if int(i) < poll_id]
        if not earlier:
            return
        poll_id = max(earlier)


def main():
    parser = argparse.ArgumentParser(description="Download the raw records for one season.")
    parser.add_argument("--season", type=int, required=True)
    parser.add_argument("--refresh", action="store_true", help="download every file again")
    args = parser.parse_args()

    raw_dir = RAW_ROOT / str(args.season)
    raw_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = raw_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

    try:
        collect_cfbd(args.season, raw_dir, manifest, args.refresh)
    except urllib.error.HTTPError as error:
        if error.code in (401, 403):
            sys.exit("The College Football Data API refused the request. "
                     "Check that the API key is in place (see the docstring at the top of this file).")
        raise
    collect_espn(args.season, raw_dir, manifest, args.refresh)
    collect_ncaa(args.season, raw_dir, manifest, args.refresh)
    collect_poll_archive(args.season, raw_dir, manifest, args.refresh)

    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    fetched = sum(1 for entry in manifest.values() if entry.get("status") == 200)
    print(f"season {args.season}: {fetched} files in {raw_dir}")


if __name__ == "__main__":
    main()
