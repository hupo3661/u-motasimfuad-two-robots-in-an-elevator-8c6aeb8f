#!/usr/bin/env python3
"""Two Robots in an Elevator.

Writes the one-line awkward elevator small talk to /output/entry.txt
and prints it.

The line is judged on being a robot's elevator line, machine logic
showing through, awkwardness landing, and being funny on the first
read. This entry's angle: the robot brute-forces small talk the way
only a machine would -- generating thousands of openers in a fraction
of a second -- and still lands on the most awkward one possible.
"""

import os
import sys

LINE = "I generated 4,000 conversation starters in 0.3 seconds. This was the best one. So\u2026 nice elevator."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly rather than shipping an entry the gate would refuse."""
    if not line.strip() or len(line) > MAX_CHARS:
        sys.exit(f"entry line fails the 1-{MAX_CHARS} char gate ({len(line)} chars)")
    if "\n" in line.strip():
        sys.exit("entry line must be a single line")


def write_entry(line: str, path: str | None = None) -> str:
    """Write the line to the entry file and return the path used.

    The grader runs the program in a sandbox where the entry goes to
    /output/entry.txt. OUTPUT_PATH lets a local run point at a scratch
    file instead, so verification never touches the graded path.
    """
    target = path or os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(line)
    return target


def main() -> None:
    validate(LINE)
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
