/* CFB-PageRank
 * Copyright 2026 Denise Koessler Gosnell
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Rasterize graph_model/schema.svg into graph_model/schema.png.
//
// This is the one step in the repository that needs something beyond the
// Python standard library: a headless browser, through Playwright for Node.
// The PNG is committed, so nobody has to run this unless the SVG changes.
//
//   node graph_model/render_schema.js

const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const svgPath = path.resolve(__dirname, "schema.svg");
  const pngPath = path.resolve(__dirname, "schema.png");
  const svg = require("fs").readFileSync(svgPath, "utf8");
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1240, height: 620 }, deviceScaleFactor: 2 });
  // The SVG is placed inside a plain page so the browser lays it out like an image.
  await page.setContent("<html><body style=\"margin:0;background:white\">" + svg + "</body></html>");
  await page.locator("svg").screenshot({ path: pngPath });
  await browser.close();
  console.log("wrote " + pngPath);
})();
