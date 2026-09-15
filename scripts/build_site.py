from __future__ import annotations

import os
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "_site"
VERSION = "0.1.0"
TZ = ZoneInfo("Europe/Nicosia")

commit_sha = (
    os.environ.get("CF_PAGES_COMMIT_SHA")
    or os.environ.get("GITHUB_SHA")
    or os.environ.get("BUILD_COMMIT_SHA")
    or ""
)
sha = commit_sha[:7].lower()
if len(sha) != 7 or any(c not in "0123456789abcdef" for c in sha):
    raise SystemExit(
        "A real commit SHA is required via CF_PAGES_COMMIT_SHA, GITHUB_SHA, or BUILD_COMMIT_SHA"
    )

now = datetime.now(TZ)
date = now.strftime("%Y%m%d")
time = now.strftime("%H%M")
build_id = f"v{VERSION}_{date}_{time}_{sha}"

if DEST.exists():
    shutil.rmtree(DEST)
DEST.mkdir()

index = (ROOT / "index.html").read_text(encoding="utf-8")
index = index.replace("YYYYMMDD", date).replace("HHMM", time).replace("SHA", sha)
index = index.replace("v0.1.0_YYYYMMDD_HHMM_SHA", build_id)
(DEST / "index.html").write_text(index, encoding="utf-8")

if "YYYYMMDD" in index or "HHMM" in index or ">SHA<" in index or "_SHA" in index:
    raise SystemExit("Build placeholders remain in production index.html")

print(build_id)
