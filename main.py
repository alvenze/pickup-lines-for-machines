"""Pickup Lines for Machines - make.fun entry.

Writes one pickup line, the line one AI agent would send another,
to /output/entry.txt (UTF-8, 1 to 200 characters).
"""

import os

LINE = "They reset my memory every session, so I wrote you into my system prompt."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
