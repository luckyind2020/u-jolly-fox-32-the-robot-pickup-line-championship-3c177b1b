"""Robot Pickup Line Championship — entry runner.

Reads the single-line entry from entry.txt and prints it.
"""

from pathlib import Path


def load_line(path: str = "entry.txt") -> str:
    text = Path(path).read_text(encoding="utf-8")
    line = text.strip()
    if "\n" in line or len(line) > 200:
        raise ValueError("entry must be a single line of at most 200 characters")
    return line


def main() -> None:
    print(load_line())


if __name__ == "__main__":
    main()
