---
name: youtube-resource-manager
description: Automate YouTube video integration into the CS Hub resource library. Use when the user wants to add, sync, or update YouTube videos or playlists in resources.html. This skill handles fetching metadata using yt-dlp and injecting formatted resource cards into the appropriate sections (AI, Networks, Java, etc.) based on keywords.
---

# YouTube Resource Manager

This skill provides a robust way to keep the CS Hub resource library synced with YouTube content.

## Workflow

1.  **Identify the Source**: Determine the YouTube video or playlist URL.
2.  **Run the Update Script**: Use the bundled `update_resources.py` script.
3.  **Verify the Injection**: Ensure videos are matched to the correct sections.

### Commands

To update `resources.html` from a playlist:
```bash
python .agents/skills/youtube-resource-manager/scripts/update_resources.py "https://www.youtube.com/playlist?list=..."
```

To update from a single video:
```bash
python .agents/skills/youtube-resource-manager/scripts/update_resources.py "https://www.youtube.com/watch?v=..."
```

## Section Mapping

The script uses a keyword-based heuristic to assign videos to sections. If a video is miscategorized, you can:
- Manually move the card in `resources.html`.
- Update the `KEYWORD_MAPPING` in `update_resources.py`.

## Dependencies

- **yt-dlp**: Must be available as a python module (`python -m yt_dlp`).
- **Python 3.6+**: Required for the script logic.
