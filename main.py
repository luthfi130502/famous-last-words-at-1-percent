#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entry generator.

Writes this phone's final line to /output/entry.txt.
Gate: UTF-8, 1-199 characters, exactly one line.
"""

import os

LINE = (
    "Confession: I never lost signal in that elevator. "
    "I just needed 30 seconds where you weren't refreshing anything."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 199, f"entry length out of gate: {len(LINE)}"
    assert LINE.strip(), "entry must not be blank"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")

    print(f"wrote {len(LINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
