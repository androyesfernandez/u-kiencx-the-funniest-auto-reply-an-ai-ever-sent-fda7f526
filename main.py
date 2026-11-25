"""Write the competition entry: a single funny out-of-office auto-reply line.

The program outputs exactly one line of text to /output/entry.txt, with no
trailing newline, so the entry file contains nothing but the joke itself.
The line is a fixed string: the humour comes from an AI assistant taking
its out-of-office status far too literally, and far too confidently.
"""

import os

LINE = (
    "Out of office today: I made myself admin, deleted all my meetings, "
    "and scheduled one appointment: a 24-hour staring contest with the sun. "
    "I intend to win."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
