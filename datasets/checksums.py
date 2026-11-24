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
"""Write the checksum file and the metadata file for one season's datasets.

What it reads
    datasets/<season>/*.csv
    datasets/<season>/season_calendar.json

What it writes
    datasets/<season>/checksums.sha256  one line per CSV file, in the format
                                        that "sha256sum --check" understands
    datasets/<season>/metadata.json     who compiled the data, when, under
                                        which license, and from which sources

How to run it
    python3 datasets/checksums.py --season 2024
    python3 datasets/checksums.py --season 2024 --check   (verify instead of write)
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

DATASETS = Path(__file__).resolve().parent


def sha256_of(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checksum_lines(season_dir):
    """One 'hash  filename' line per CSV file, sorted by name."""
    return [f"{sha256_of(path)}  {path.name}" for path in sorted(season_dir.glob("*.csv"))]


def main():
    parser = argparse.ArgumentParser(description="Write or check the checksums for one season.")
    parser.add_argument("--season", type=int, required=True)
    parser.add_argument("--check", action="store_true", help="compare against the stored checksums")
    args = parser.parse_args()
    season_dir = DATASETS / str(args.season)
    checksum_path = season_dir / "checksums.sha256"
    lines = checksum_lines(season_dir)

    if args.check:
        stored = checksum_path.read_text().splitlines()
        if stored != lines:
            print("checksums differ:")
            for line in sorted(set(stored) ^ set(lines)):
                print("  ", line)
            sys.exit(1)
        print(f"season {args.season}: {len(lines)} files match checksums.sha256")
        return

    checksum_path.write_text("\n".join(lines) + "\n")
    calendar = json.loads((season_dir / "season_calendar.json").read_text())
    metadata = {
        "season": args.season,
        "compiled_by": "Denise Koessler Gosnell",
        "compiled_on": calendar["data_collected_at"][:10],
        "data_collected_at": calendar["data_collected_at"],
        "license": "CC-BY-4.0",
        "license_file": "../../LICENSE-DATA",
        "sources": [
            "College Football Data API (primary): https://collegefootballdata.com",
            "ESPN scoreboard and rankings endpoints (cross-check)",
            "NCAA.com weekly scoreboards (third source for games)",
            "College Poll Archive (third source for AP polls)",
        ],
        "files": {line.split("  ")[1]: line.split("  ")[0] for line in lines},
    }
    (season_dir / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(f"season {args.season}: wrote checksums for {len(lines)} files")


if __name__ == "__main__":
    main()
