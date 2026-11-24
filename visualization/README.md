# Visualization

The tables in `pagerank/` tell you where a team stands in a given week. The pages here let you watch it move. Each season has one page with a week slider: drag it from the preseason to the last week and the graph grows one week of games at a time while the circles swell and shrink with their PageRank points.

The page builder is licensed under Apache 2.0 and the pages under CC BY 4.0. Copyright 2026 Denise Koessler Gosnell. The pages load D3, which is included under its own ISC license in `lib/`.

## Opening a Page

Open `visualization/<season>/index.html` in a browser. No server and no build step. The season's vertices, its edges, and its weekly snapshots are written into the page, so it works from a local folder or from GitHub Pages. The one file it loads is `../lib/d3.v7.min.js`, so keep the folder layout as it is.

## What Is on the Page

Two views, and a table that follows both.

The graph view draws every `Team` vertex as a circle with a white fill and a stroke colored by conference, the way the figures in the book draw vertices. The circle's size is the team's PageRank points in the selected week, on one scale for the whole season. At the preseason position every team holds 100 points, every circle is the same size, and every team is tied for first; the first week of games is where they start to separate. Every `loses_to` edge played on or before the selected week is drawn as a thin black arrow from the team that lost to the team that won. Teams in the top 25 carry a label; hover over any other circle to see its name with its rank and score. Click a circle, or type a name in the search box, to highlight a team and its edges in orange.

The rank-over-time view is a bump chart. It takes the top 25 teams of the selected week and draws one line per team across every week of the season, so you can see when a team climbed into the top 25 and whether it stayed there. Ranks past 60 are pinned to the bottom edge of the chart.

The table on the right lists the top 25 of the selected week in the selected mode, with each team's points and its change in rank from the week before.

The two radio buttons switch between the unweighted graph and the weighted graph (margin capped at 28). Everything on the page reads the precomputed snapshots from `pagerank/<season>/snapshots/`. Moving the slider recomputes nothing.

The positions of the circles come from one force layout run over the whole season's graph when the page loads, so a team stays put while you slide through the weeks. Only the edges shown and the circle sizes change.

## Colors

The four stroke colors that appear most are sampled from the figures in The Practitioner's Guide to Graph Data: royal blue and orange, plus teal and sky blue. The remaining conferences take darker or lighter steps of those four, and FCS opponents are drawn in gray. The legend under the controls maps each color to its conference. Orange is also the highlight color, as it is in the book's figures.

## Rebuilding the Pages

```
python3 visualization/build_pages.py --season 2024
```

`make viz` rebuilds every season. The builder reads the graph files and the PageRank snapshots, fills in `page_template.html`, and writes `<season>/index.html`. Nothing in the pages is typed by hand except the template.
