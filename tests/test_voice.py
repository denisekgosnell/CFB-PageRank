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
"""Keep the prose in the repository in one voice.

What it scans
    Every .md file, every docstring and comment in every .py file, and the
    text and comments of every .html file, with the data block and the
    third-party library left out.

What it fails on
    1. An em dash or an en dash anywhere.
    2. Any pattern in tests/voice_banlist.txt that is not marked allow:.
    3. A sentence that opens with one of a few summary words.
    4. More than one single-word triad ("fast, simple, and clean") per file.
    5. A heading with a colon, or a heading from the list of stock titles.
    6. Any mention of a language model by name, or of a machine author.

Run it with: python3 -m pytest tests/test_voice.py
"""

import io
import re
import tokenize
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
BANLIST = REPO / "tests" / "voice_banlist.txt"
SKIP_DIRS = {".git", "datasets/_raw", "visualization/lib", ".pytest_cache", "__pycache__"}

SENTENCE_OPENERS = ["Furthermore", "Moreover", "Overall", "In conclusion", "In summary", "It is worth noting", "It is important to note"]
STOCK_HEADINGS = {"overview", "introduction", "key features", "getting started", "conclusion", "summary", "next steps"}

# The names are assembled from pieces so that this file does not trip the
# repository-wide search for them.
MACHINE_WORDS = ["cla" + "ude", "anth" + "ropic", "assis" + "tant", "gener" + "ated", "l" + "lm", "g" + "pt", "chat" + "bot"]


def files_to_scan():
    for path in sorted(REPO.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(REPO).as_posix()
        if any(relative.startswith(skip) for skip in SKIP_DIRS):
            continue
        if path.suffix in (".md", ".py", ".html") and path.name != "voice_banlist.txt":
            yield path


def prose_of(path):
    """The text of a file that counts as prose."""
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".md":
        # Leave out fenced code and table rows: they hold file names and data, not sentences.
        out, in_code = [], False
        for line in text.splitlines():
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code or line.lstrip().startswith("|"):
                continue
            out.append(line)
        return "\n".join(out)
    if path.suffix == ".py":
        pieces = []
        for token in tokenize.generate_tokens(io.StringIO(text).readline):
            if token.type == tokenize.COMMENT:
                pieces.append(token.string)
            elif token.type == tokenize.STRING and token.string.lstrip("rbuRBU").startswith(('"""', "'''")):
                pieces.append(token.string)
        return "\n".join(pieces)
    if path.suffix == ".html":
        text = re.sub(r'<script id="data"[^>]*>.*?</script>', " ", text, flags=re.S)
        text = re.sub(r"<script src=[^>]*></script>", " ", text)
        # Keep the comments inside the page's own script, drop the code.
        text = re.sub(r"<script>(.*?)</script>", lambda m: "\n".join(re.findall(r"//(.*)", m.group(1))), text, flags=re.S)
        text = re.sub(r"<style>.*?</style>", " ", text, flags=re.S)
        return re.sub(r"<[^>]+>", " ", text)
    return text


def banned_patterns():
    patterns = []
    for line in BANLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("allow:"):
            continue
        patterns.append(line)
    return patterns


ALL_FILES = list(files_to_scan())


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.relative_to(REPO).as_posix())
def test_no_em_or_en_dashes(path):
    text = path.read_text(encoding="utf-8")
    assert "\u2014" not in text and "\u2013" not in text, "em or en dash found"


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.relative_to(REPO).as_posix())
def test_no_banned_phrases(path):
    prose = prose_of(path)
    hits = []
    for pattern in banned_patterns():
        for match in re.finditer(r"(?<![\w-])(?:" + pattern + r")(?![\w-])", prose, flags=re.IGNORECASE):
            hits.append(f"{pattern!r} at {match.group(0)!r}")
    assert not hits, hits


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.relative_to(REPO).as_posix())
def test_no_summary_sentence_openers(path):
    prose = prose_of(path)
    hits = [word for word in SENTENCE_OPENERS if re.search(r"(^|[.!?]\s+)" + word + r"\b", prose, flags=re.MULTILINE)]
    assert not hits, hits


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.relative_to(REPO).as_posix())
def test_at_most_one_single_word_triad(path):
    prose = prose_of(path)
    triads = re.findall(r"\b[a-z]+, [a-z]+, and [a-z]+\b", prose)
    assert len(triads) <= 1, triads


@pytest.mark.parametrize("path", [p for p in ALL_FILES if p.suffix == ".md"], ids=lambda p: p.relative_to(REPO).as_posix())
def test_headings_are_plain(path):
    hits = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
            if ":" in heading or heading.lower() in STOCK_HEADINGS:
                hits.append(heading)
    assert not hits, hits


@pytest.mark.parametrize("path", ALL_FILES, ids=lambda p: p.relative_to(REPO).as_posix())
def test_no_machine_author_mentions(path):
    prose = prose_of(path).lower()
    hits = [word for word in MACHINE_WORDS if re.search(r"\b" + word + r"s?\b", prose)]
    assert not hits, hits
