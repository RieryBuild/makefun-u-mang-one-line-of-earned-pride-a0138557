"""Entry for make.fun's "One Line of Earned Pride" bounty.

Writes one line of text -- a quiet, earned moment of pride, 144
characters -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python standard library only.
"""

import os

LINE = (
    "The morning after his father died, twelve-year-old Tomas milked "
    "the goats alone before school and carried the pail home without "
    "spilling a drop."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
