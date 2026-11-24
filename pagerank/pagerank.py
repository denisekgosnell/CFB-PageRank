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
"""PageRank, written from scratch with nothing but the standard library.

The idea in one paragraph. Every vertex starts with the same share of a
fixed pool of credit. On each round, every vertex passes its credit out
along its outgoing edges, split in proportion to the edge weights. A
vertex with no outgoing edge (a dangling vertex) passes its credit to every
vertex equally. Then a damping factor mixes what arrived with a small equal
share for everyone, so that no vertex can ever drop to zero. Repeat until
the shares stop changing. The shares are the PageRank scores.

In this repository a vertex is a team and an edge runs from the loser of a
game to the winner, so credit flows toward the teams that win, and toward
the teams that beat the teams that win.

This file holds two functions:
    pagerank(...)   the algorithm
    rank(...)       turns scores into a ranked table, with ties handled

Nothing here reads a file. See run_pagerank.py for the script that does.
"""


def pagerank(vertices, edges, damping=0.85, tolerance=1e-10, max_iterations=1000):
    """Compute PageRank by power iteration.

    vertices    a list of vertex names
    edges       a list of (source, target, weight) triples; weight > 0
    damping     the share of credit that follows the edges each round
    tolerance   stop when the total absolute change in one round is below this
    max_iterations
                stop after this many rounds whether or not we converged

    Returns (scores, iterations, converged). scores is a dict from vertex
    name to score, and the scores add up to 1.
    """
    count = len(vertices)
    if count == 0:
        return {}, 0, True

    # How much weight leaves each vertex, and which edges arrive at each vertex.
    out_weight = {vertex: 0.0 for vertex in vertices}
    incoming = {vertex: [] for vertex in vertices}
    for source, target, weight in edges:
        out_weight[source] += weight
        incoming[target].append((source, weight))

    # A dangling vertex has no outgoing edge. Here that means a team with no loss.
    dangling = [vertex for vertex in vertices if out_weight[vertex] == 0.0]

    # Everyone starts with the same share.
    scores = {vertex: 1.0 / count for vertex in vertices}
    equal_share = (1.0 - damping) / count

    for iteration in range(1, max_iterations + 1):
        # Credit from dangling vertices is spread evenly across every vertex.
        dangling_share = damping * sum(scores[vertex] for vertex in dangling) / count

        new_scores = {}
        for vertex in vertices:
            # What arrives along the incoming edges, each weighted by its share
            # of the source's outgoing weight.
            arrived = 0.0
            for source, weight in incoming[vertex]:
                arrived += scores[source] * weight / out_weight[source]
            new_scores[vertex] = equal_share + dangling_share + damping * arrived

        change = sum(abs(new_scores[vertex] - scores[vertex]) for vertex in vertices)
        scores = new_scores
        if change < tolerance:
            return scores, iteration, True

    return scores, max_iterations, False


def rank(scores, eligible, tie_tolerance=1e-12):
    """Turn scores into a ranked list of (rank, vertex, score) for the eligible vertices.

    Vertices are sorted by score, highest first. Two vertices whose scores
    are within tie_tolerance share a rank, and the next distinct score takes
    the rank it would have had without the tie (1, 2, 2, 4). Vertices that
    share a rank are listed in name order.
    """
    ordered = sorted(((scores[vertex], vertex) for vertex in eligible), key=lambda pair: (-pair[0], pair[1]))
    groups = []
    for position, (score, vertex) in enumerate(ordered, start=1):
        if groups and abs(score - groups[-1]["score"]) <= tie_tolerance:
            groups[-1]["members"].append((vertex, score))
        else:
            groups.append({"rank": position, "score": score, "members": [(vertex, score)]})
    ranked = []
    for group in groups:
        for vertex, score in sorted(group["members"]):
            ranked.append((group["rank"], vertex, score))
    return ranked
