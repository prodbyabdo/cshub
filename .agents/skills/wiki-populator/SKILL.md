---
name: wiki-populator
description: >
  Manages, executes, and tracks the population of the CS Hub Wikipedia-sourced wiki.
  Use this skill whenever the user wants to add pages to the CS Hub wiki, run the
  fetch script, check or update population progress, add new topics to the fetch backlog,
  stop and resume fetching, or understand how the wiki population system works.
  Also triggers when the user asks about PROGRESS.md, TASK_FETCH.md, fetch_wiki.py,
  or anything related to automatically generating wiki HTML pages from Wikipedia.
---

# CS Hub Wiki Populator

This skill manages the automated process of populating the CS Hub wiki with
Wikipedia article summaries. It uses the **Wikipedia MediaWiki API** (not local HTML
dumps) to fetch only introductory summaries, ranks topics by importance, and generates
clean HTML pages into the `wiki/` directory.

## Files at a Glance

| File | Purpose |
|------|---------|
| `fetch_wiki.py` | Main script — fetches, ranks, and generates HTML pages |
| `PROGRESS.md` | Live tracker — auto-updated by the script as topics complete |
| `TASK_FETCH.md` | Backlog — 200 planned topics organized by category |
| `WIKI_POPULATION_GUIDE.md` | Human-readable guide for adding topics and running the script |

All four files live in the **project root** (`cshub-main/`).

## How to Run

```bash
# From cshub-main/
python fetch_wiki.py
```

- The script **skips** any topic whose HTML file already exists → safe to stop (`Ctrl+C`) and re-run at any time.
- `PROGRESS.md` is updated **live** after each topic is processed.

## Importance Ranking (1–6)

The script queries Wikipedia for **incoming link count** and assigns a rank:

| Rank | Inlinks | Action |
|------|---------|--------|
| 1 | > 1,000 | ✅ Downloaded |
| 2 | 501–1,000 | ✅ Downloaded |
| 3 | 251–500 | ✅ Downloaded |
| 4 | 101–250 | ⏭ Skipped |
| 5 | 51–100 | ⏭ Skipped |
| 6 | < 50 | ⏭ Skipped |

Change `RANK_THRESHOLD` at the top of `fetch_wiki.py` to pull deeper (e.g., `4`).

## Adding New Topics

1. Open `fetch_wiki.py`
2. Find `WIKI_PAGES` dictionary
3. Add the **exact Wikipedia article title** to the right category list
4. Add the same title to `PROGRESS.md` as `- [ ] Title` under the matching section
5. Add it to `TASK_FETCH.md` as a checklist item under the right category
6. Run `python fetch_wiki.py` — it fetches only the new items

## Progress Tracking

`PROGRESS.md` uses these status markers, automatically written by the script:

- `[ ]` — Pending
- `[x]` — Completed (Rank 1–3, page generated)
- `[s]` — Skipped (rank too low)
- `[e]` — Error (Wikipedia page not found or wrong title)

`TASK_FETCH.md` is the **planning backlog** — tick items manually when desired to indicate intent, or let the script auto-sync through `PROGRESS.md`.

## Stop and Continue

```
Press Ctrl+C at any time to stop.
Run `python fetch_wiki.py` again to continue — already-generated files are skipped instantly.
```

## Reference Files

- See [PROGRESS.md](../../../PROGRESS.md) — current live state of all topics
- See [TASK_FETCH.md](../../../TASK_FETCH.md) — full backlog of 200 planned topics
- See [WIKI_POPULATION_GUIDE.md](../../../WIKI_POPULATION_GUIDE.md) — complete human guide
