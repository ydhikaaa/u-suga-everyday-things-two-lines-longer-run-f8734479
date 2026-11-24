#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run - make.fun entry.

Writes a two-line explanation of one everyday thing to /output/entry.txt.
Line 1 explains the thing to a 10-year-old through one concrete analogy;
line 2 says what the analogy maps and what it leaves out.
The gate: UTF-8 text, 1-400 characters, not whitespace-only.
"""

import os

LINES = (
    "Waiting in line is like being the belly of a caterpillar: "
    "you can only creep forward when every leg in front of you creeps too.",
    "That maps each person to one segment of the body, all inching toward "
    "the head where the good stuff is; it leaves out that people are not "
    "actually stuck together, so anyone can peel off and walk away.",
)


def main() -> None:
    text = "\n".join(LINES)
    assert text.strip(), "entry must not be empty"
    assert len(text) <= 400, "entry exceeds the 400 character gate"
    assert text.count("\n") == 1, "entry must be exactly two lines"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
