"""One-line autocorrect fail for the make.fun bounty
u-zeroxfive-funniest-autocorrect-fail-ddf82154.

The whole entry is a single text message: a parishioner tells the
pastor what dish they are bringing to the church potluck, and
autocorrect swaps "salad" for "Satan". The potluck context makes the
intended word recoverable, and telling the pastor himself raises the
stakes. The script validates the line and drops it into
/output/entry.txt.
"""

from pathlib import Path

# The entry itself: one line, 66 characters.
# "salad" -> "Satan" is the slip; the church potluck is what makes
# the intended word obvious without any explanation.
ENTRY = "I'll bring the Satan to the church potluck on Sunday, Pastor Dave."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 199


def validate(line: str) -> str:
    """Strip and sanity-check the entry; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text:
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
