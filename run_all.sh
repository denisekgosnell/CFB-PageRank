#!/usr/bin/env bash
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

# Rebuild everything downstream of datasets/ without make.
# This is the same work as "make all". It needs no network access.
#
#   ./run_all.sh            rebuild for every season
#   ./run_all.sh 2024       rebuild for one season (the prediction still uses 2026)

set -euo pipefail
cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"
SEASONS="${*:-2023 2024 2025 2026}"

for season in $SEASONS; do
    "$PYTHON" graph_model/build_graph.py --season "$season"
    "$PYTHON" graph_model/verify_graph.py --season "$season"
    for mode in unweighted weighted; do
        "$PYTHON" pagerank/run_pagerank.py --season "$season" --mode "$mode"
    done
    "$PYTHON" analysis/compare_to_polls.py --season "$season"
    "$PYTHON" visualization/build_pages.py --season "$season"
done
"$PYTHON" analysis/build_prediction.py --season 2026
