# Implementation Plan - CSV Batch Import for YouTube Resource Manager

The goal is to process `newtempcsv.csv` and inject the YouTube resources into `resources.html` using the `youtube-resource-manager` skill logic, while ensuring videos are placed in the correct sections as specified in the CSV.

## User Review Required

> [!IMPORTANT]
> The script will use the `Category` column from the CSV to determine the section in `resources.html`. I will ensure these categories match the existing section IDs in the HTML.

## Proposed Changes

### [youtube-resource-manager](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/.agents/skills/youtube-resource-manager)

#### [MODIFY] [update_resources.py](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/.agents/skills/youtube-resource-manager/scripts/update_resources.py)
- Add `csv` module import.
- Update `main()` to detect if the argument is a `.csv` file.
- Add a `process_csv(filepath)` function to iterate through the CSV and call the card creation and injection logic.
- Ensure the CSV processing uses the `Category` column for section assignment.

## Verification Plan

### Automated Tests
- Run `python .agents/skills/youtube-resource-manager/scripts/update_resources.py newtempcsv.csv`.
- Verify that `resources.html` contains the new video cards.
- Use the existing `verify.py` script to check counts if applicable.

### Manual Verification
- Open `resources.html` and check a few sections (e.g., Intro to CS, Networks) to ensure cards are rendered correctly with thumbnails and channel links.
