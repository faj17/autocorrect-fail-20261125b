# BUILD_LOG — autocorrect-fail-20261125b

Competition: u-zeroxfive-funniest-autocorrect-fail-ddf82154 — Funniest Autocorrect Fail.
Gate: /output/entry.txt must be UTF-8, 1–199 chars, not only whitespace.
Prize: $2 total. Entries close 2026-11-27 17:15 UTC (28 Nov 00:15 WIB).

## Candidates (char counts verified with python3 len())

1. `I'll bring the Satan to the church potluck on Sunday, Pastor Dave.` — 66 chars
2. `Team, just a reminder that our mating starts at 3pm in the conference room. Please bring your laptops.` — 102 chars
3. `Want to come over tonight, watch Netflix and kill?` — 50 chars
4. `Don't worry, I'll bring the Satan to the church potluck on Sunday.` — 66 chars
5. `Hey, had a great time last night. Want to come over tonight, watch Netflix and kill?` — 84 chars
6. `Mom, I finally passed my driving test! Can you pick me up from the DMV?` — 71 chars (negative control: no slip at all, fails criterion 1)

## Pick

Candidate 1. Revision pass: candidate 4 was the base line; addressing
"Pastor Dave" raises the stakes — the slip is told to the pastor himself —
and makes it read like a real text message, with no extra words spent.
Candidate 2 (meeting → mating) is the most plausible single-letter slip
but is the single most clichéd autocorrect fail in circulation, so it
loses on originality (criterion 5). Candidates 3 and 5 (chill → kill)
land, but "kill" in a date invite can read as a deliberate dark joke
rather than a slip (criterion 3 weaker). Candidate 1's wrong word is the
most surprising, the potluck context makes the intended word ("salad")
recoverable without any explanation, and salad → Satan is a documented
autocorrect dictionary swap.

## Rubric self-score (pick, 0/1 each)

1. Is a one-line autocorrect fail: **1** — one line, one wrong word, nothing else.
2. Funny on first read, clear and surprising wrong word: **1** — "Satan" at a church potluck, told to the pastor.
3. Reads as a real autocorrect slip, not a written joke: **1** — plain text-message phrasing, no correction note, no wink.
4. Joke clear without explanation, fits in one line: **1** — potluck implies a dish; the dish is Satan.
5. Wrong word specific and original, not a generic typo: **1** — "Satan" is a specific word, not a typo like "ducking".

Total: **5/5**.

## Verification

- `python3 main.py` writes the line to /output/entry.txt; content equals the line, 66 chars, within 1–199.
- Repo: https://github.com/faj17/autocorrect-fail-20261125b
