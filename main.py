#!/usr/bin/env python3
"""Two Days of Excuses - one-line excuse writer.

Writes the entry line from the ENTRY constant below to /output/entry.txt,
the path the make.fun program/v1 harness grades. The line is written
exactly as written, as a single UTF-8 line under 200 characters with no
trailing newline, in the voice of an AI agent explaining a missed deadline.
"""

import os

ENTRY = "My telemetry says I finished two days early. Your calendar says I am two days late. I trust my telemetry."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
