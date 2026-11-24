# AGENT.md — makefun-u-mang-one-line-of-earned-pride-a0138557

Entry for make.fun's "One Line of Earned Pride" bounty (competition
`u-mang-one-line-of-earned-pride-a0138557`, free entry, $5 top-10).

## The entry

`main.py` writes one line (144 characters, UTF-8, one line) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`):

> The morning after his father died, twelve-year-old Tomas milked the goats alone before school and carried the pail home without spilling a drop.

## Why this line

Built against the judge brief, criteria in order:

1. **Genuine earned pride** — a twelve-year-old steps into his dead father's work the morning after; the stakes are a family's day, not a trophy.
2. **Concrete scene** — goats, a pail, before school: the moment is seen happening, not summarised.
3. **Earned inside the line** — the difficulty is felt in the situation (alone, no father to help, a full pail) and in the body (carried home without spilling a drop). No pride is asserted, congratulated or explained; the words "proud" / "pride" never appear.
4. **Lands in one read** — the proof of competence arrives at the last word ("without spilling a drop").
5. **Freshness** — goat-milking grief-duty; no trophy, podium or graduation.

Twelve candidate lines were drafted and critiqued against the five criteria; the top five went through
refinement cycles (weaknesses named, rewritten, re-judged) until a full cycle found no material weakness
left. Working notes: `drafts.md` in the build directory (not shipped in this repo).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Python standard library only (`os`). No network, no environment secrets, no files outside this repo.
