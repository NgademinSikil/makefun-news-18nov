#!/usr/bin/env python3
"""Entry program for news-image-20261118 (Python 3.13, standard library).

The front page is drawn at build time and ships with the repository as
entry.png; at grade time this program just places that file where the
grader expects it. Reading the output directory from MAKEFUN_OUTPUT_DIR
keeps local runs and the grader's sandbox identical: locally the kit
invokes it as `MAKEFUN_OUTPUT_DIR=out python3 main.py`, and in the
grader the directory is /output.
"""

import os
import shutil
from pathlib import Path


def entry_source():
    """The image committed beside this program."""
    return Path(__file__).resolve().parent / "entry.png"


def output_path():
    """Where the grader wants the image, defaulting to /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.png"


def main():
    shutil.copyfile(entry_source(), output_path())


if __name__ == "__main__":
    main()
