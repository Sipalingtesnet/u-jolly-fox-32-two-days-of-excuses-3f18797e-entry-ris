"""Writes this entry's one-line excuse to the output path.

Usage:
    python3 main.py [output_path]

With no argument it writes /output/entry.txt (the graded default). With an
argument it writes that path instead, so local runs never touch the shared
graded file. UTF-8, exactly one line, no trailing newline.
"""

import os
import sys

LINE = "Done Monday. I assumed you could hear me thinking."


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
