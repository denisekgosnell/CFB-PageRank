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
"""Draw the schema figure, graph_model/schema.svg, by hand.

The left panel is the schema: one Team vertex label with a self-referencing
loses_to edge label. The right panel is one piece of data that follows the
schema, taken from datasets/2023/games.csv so that every value in the
drawing is a real value.

What it reads
    datasets/2023/games.csv   for the one game drawn on the right

What it writes
    graph_model/schema.svg

How to run it
    python3 graph_model/draw_schema.py

The drawing follows the figures in The Practitioner's Guide to Graph Data:
white background, a thin black frame, circles with a colored stroke and a
white fill, black arrows, bold labels, and property keys in regular weight.
"""

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# The game drawn on the right. Rivalry week, 2023: Michigan 30, Ohio State 24.
INSTANCE_DATE = "2023-11-25"
INSTANCE_HOME = "Michigan"
INSTANCE_AWAY = "Ohio State"

BLUE = "#1F4ADE"
FONT = "Helvetica, Arial, sans-serif"


def find_instance():
    """Read the one game that the right panel draws."""
    with (REPO / "datasets" / "2023" / "games.csv").open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["game_date"] == INSTANCE_DATE and row["home_team"] == INSTANCE_HOME and row["away_team"] == INSTANCE_AWAY:
                return row
    raise SystemExit("the instance game is not in datasets/2023/games.csv")


def circle(cx, cy, r, title, lines, title_size=20, line_size=14):
    """A vertex: a circle with a bold title and property keys beneath it."""
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{BLUE}" stroke-width="3"/>']
    top = cy - (len(lines) * line_size) / 2 - 4
    out.append(f'<text x="{cx}" y="{top}" text-anchor="middle" font-family="{FONT}" font-size="{title_size}" font-weight="bold">{title}</text>')
    for i, line in enumerate(lines):
        out.append(f'<text x="{cx}" y="{top + 20 + i * (line_size + 3)}" text-anchor="middle" font-family="{FONT}" font-size="{line_size}">{line}</text>')
    return out


def label(x, y, title, lines, anchor="middle", title_size=16, line_size=13):
    """An edge label: bold title with property keys beneath it."""
    out = [f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}" font-size="{title_size}" font-weight="bold">{title}</text>']
    for i, line in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + 18 + i * (line_size + 3)}" text-anchor="{anchor}" font-family="{FONT}" font-size="{line_size}">{line}</text>')
    return out


def main():
    game = find_instance()
    winner_score = max(int(game["home_score"]), int(game["away_score"]))
    loser_score = min(int(game["home_score"]), int(game["away_score"]))

    width, height = 1240, 560
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height + 60}" viewBox="0 0 {width} {height + 60}">',
             '<!-- CFB-PageRank. Copyright 2026 Denise Koessler Gosnell. Licensed under the Apache License, Version 2.0 (the "License"); '
             'you may not use this file except in compliance with the License. You may obtain a copy of the License at '
             'http://www.apache.org/licenses/LICENSE-2.0. Unless required by applicable law or agreed to in writing, software '
             'distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, '
             'either express or implied. See the License for the specific language governing permissions and limitations under the License. -->',
             '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
             '<path d="M 0 0 L 10 5 L 0 10 z" fill="black"/></marker></defs>',
             f'<rect x="0" y="0" width="{width}" height="{height + 60}" fill="white"/>',
             f'<rect x="20" y="20" width="{width - 40}" height="{height - 40}" fill="white" stroke="black" stroke-width="1"/>',
             f'<line x1="{width // 2}" y1="40" x2="{width // 2}" y2="{height - 40}" stroke="black" stroke-width="1"/>',
             f'<text x="{width // 4}" y="70" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="bold">Graph Schema</text>',
             f'<text x="{3 * width // 4}" y="70" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="bold">Graph Data</text>']

    # Left panel: the schema. One Team circle with a self-referencing loses_to edge.
    cx, cy, r = 250, 330, 85
    parts += circle(cx, cy, r, "Team", ["team", "conference", "division"])
    # The loop leaves the circle at the upper right, swings out, and comes back in on the right.
    parts.append(f'<path d="M {cx + 55} {cy - 65} C {cx + 150} {cy - 190}, {cx + 300} {cy - 60}, {cx + 88} {cy - 5}" '
                 'fill="none" stroke="black" stroke-width="1.5" marker-end="url(#arrow)"/>')
    parts += label(cx + 215, cy - 20, "loses_to",
                   ["game_id", "game_date", "week", "winner_score", "loser_score", "margin", "neutral_site"], anchor="start")

    # Right panel: the data. The loser points to the winner.
    lx, rx, y, r2 = 760, 1110, 330, 80
    parts += circle(lx, y, r2, game["loser"], [f"{game['loser']} lost"], title_size=18, line_size=13)
    parts += circle(rx, y, r2, game["winner"], [f"{game['winner']} won"], title_size=18, line_size=13)
    parts.append(f'<line x1="{lx + r2 + 2}" y1="{y}" x2="{rx - r2 - 2}" y2="{y}" stroke="black" stroke-width="1.5" marker-end="url(#arrow)"/>')
    parts += label((lx + rx) // 2, y - 95, "loses_to",
                   [f"game_id: {game['game_id']}", f"game_date: {game['game_date']}", f"week: {game['week']}"])
    parts += label((lx + rx) // 2, y + 30, "", [f"winner_score: {winner_score}", f"loser_score: {loser_score}",
                                                 f"margin: {game['margin']}", f"neutral_site: {game['neutral_site']}"])

    parts.append(f'<text x="20" y="{height + 10}" font-family="Georgia, Times, serif" font-size="17" font-style="italic">'
                 'Figure 1. The CFB-PageRank schema: a team that loses a game points to the team that beat it.</text>')
    parts.append("</svg>\n")
    (REPO / "graph_model" / "schema.svg").write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote graph_model/schema.svg with {game['loser']} loses_to {game['winner']} ({winner_score}-{loser_score}, {game['game_date']})")


if __name__ == "__main__":
    main()
