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
"""Check that every source file in the repository carries the ownership header.

What this test reads: every .py, .sh, .html, .svg, and .js file in the
repository, plus the Makefile.
What it checks: the first twenty lines of each file name the copyright
holder and the Apache License.
What it skips: the vendored D3 library under visualization/lib, which
carries its own license.

Run it with: python3 -m pytest tests/test_headers.py
"""

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Every file with one of these suffixes must carry the header.
SUFFIXES = {".py", ".sh", ".html", ".svg", ".js"}

# Directories that hold third-party code or scratch files.
SKIP_DIRS = {"visualization/lib", ".git", "datasets/_raw", ".pytest_cache", "__pycache__"}

COPYRIGHT_LINE = "Copyright 2026 Denise Koessler Gosnell"
LICENSE_LINE = "Licensed under the Apache License, Version 2.0"


def files_that_need_a_header():
    """Walk the repository and return every file that must carry the header."""
    found = []
    for path in REPO.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(REPO).as_posix()
        if any(relative.startswith(skip) for skip in SKIP_DIRS):
            continue
        if path.suffix in SUFFIXES or path.name == "Makefile":
            found.append(path)
    return found


def test_every_source_file_has_the_header():
    """Fail with the list of files that are missing either header line."""
    missing = []
    for path in files_that_need_a_header():
        head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:20])
        if COPYRIGHT_LINE not in head or LICENSE_LINE not in head:
            missing.append(path.relative_to(REPO).as_posix())
    assert not missing, "Files missing the ownership header: " + ", ".join(missing)


def test_the_license_files_name_the_owner():
    """LICENSE, NOTICE, and CITATION.cff all have to name the owner."""
    assert COPYRIGHT_LINE in (REPO / "LICENSE").read_text(encoding="utf-8")
    assert COPYRIGHT_LINE in (REPO / "NOTICE").read_text(encoding="utf-8")
    citation = (REPO / "CITATION.cff").read_text(encoding="utf-8")
    assert "family-names: Gosnell" in citation
    assert "given-names: Denise Koessler" in citation
    assert (REPO / "LICENSE-DATA").read_text(encoding="utf-8").startswith("Attribution 4.0 International")
