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

# How to use this file
#
#   make all        rebuild everything downstream of datasets/ (no network needed)
#   make data       collect and verify the raw datasets (needs the network)
#   make graph      translate datasets into the graph model and verify it
#   make pagerank   run PageRank week by week for every season and mode
#   make analysis   compare PageRank to the human polls and write the prediction
#   make viz        build the interactive pages from the PageRank snapshots
#   make test       run the test suite
#   make schema-png rasterize graph_model/schema.svg (needs Playwright, see graph_model/README.md)

PYTHON ?= python3
SEASONS ?= 2023 2024 2025 2026
MODES ?= unweighted weighted

.PHONY: all data graph pagerank analysis viz test schema-png

all: graph pagerank analysis viz

data:
	@for season in $(SEASONS); do \
		$(PYTHON) datasets/collect.py --season $$season || exit 1; \
		$(PYTHON) datasets/build_datasets.py --season $$season || exit 1; \
		$(PYTHON) datasets/cross_check.py --season $$season || exit 1; \
		$(PYTHON) datasets/checksums.py --season $$season || exit 1; \
	done

graph:
	@for season in $(SEASONS); do \
		$(PYTHON) graph_model/build_graph.py --season $$season || exit 1; \
		$(PYTHON) graph_model/verify_graph.py --season $$season || exit 1; \
	done

pagerank:
	@for season in $(SEASONS); do \
		for mode in $(MODES); do \
			$(PYTHON) pagerank/run_pagerank.py --season $$season --mode $$mode || exit 1; \
		done; \
	done

analysis:
	@for season in $(SEASONS); do \
		$(PYTHON) analysis/compare_to_polls.py --season $$season || exit 1; \
	done
	$(PYTHON) analysis/build_prediction.py --season 2026

viz:
	@for season in $(SEASONS); do \
		$(PYTHON) visualization/build_pages.py --season $$season || exit 1; \
	done

test:
	$(PYTHON) -m pytest -q tests

schema-png:
	$(PYTHON) graph_model/render_schema.py
