# SPDX-License-Identifier: MIT
"""News-image entry for make.fun competition news-image-20261117.

Writes one image summing up the world news of Tuesday, 17 November 2026
to /output/entry.png. The image is baked into the repository
(assets/entry.png, 1024x1024 PNG) and this program copies it byte-for-byte, so the two
grading runs produce identical output. Standard library only, no network.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
