# CS Hub Wiki Population Guide

This guide explains how to add new content to the wiki, track your progress, and safely pause or resume the automated fetching process.

## 1. How to Populate More Pages

To add new topics to the wiki, you do not need to download any HTML files manually. Everything is handled by `fetch_wiki.py`.

1. Open `fetch_wiki.py` in your code editor.
2. Locate the `WIKI_PAGES` dictionary at the top of the file.
3. Add the exact Wikipedia article titles to the appropriate category list. 
   - *Example:* If you want to add "Cryptography" to the Cybersecurity section, ensure it's in the list: `"cybersecurity": ["Computer security", "Cryptography", ...]`
4. Run the script in your terminal:
   ```bash
   python fetch_wiki.py
   ```
5. The script will automatically fetch the intro summary, verify if it's important enough (Rank 1-3), generate the HTML page, and update the index page (e.g., `wiki/cybersecurity.html`).

---

## 2. How to Track Progress

Because the script dynamically generates files based on the list in `fetch_wiki.py`, your progress is directly reflected by **what HTML files exist in the `wiki/` subfolders**.

- **Visual Tracking:** Open the main `wiki/*.html` index pages in your browser. Any topic that has been successfully fetched will appear as a clickable card with its importance rank.
- **Terminal Output:** When you run `fetch_wiki.py`, it prints out exactly what it is doing. You will see output like:
  ```
  Fetching Machine learning...
    -> Rank 1 (2000+ inlinks)
    -> Generated ai/machine-learning.html
  ```

---

## 3. How to Stop and Continue

The script has been updated with a **"Resume/Skip"** feature. This means you do not have to fetch everything all at once. 

### Stopping the Script
If you are fetching a large batch of new topics and need to stop the script halfway through, simply press `Ctrl + C` in your terminal. 
- **Safe to Stop:** The script writes one file at a time. Stopping it will not corrupt the wiki.

### Continuing the Process
When you are ready to resume, simply run the script again:
```bash
python fetch_wiki.py
```
- **Automatic Skipping:** The script checks if an HTML file for a topic already exists in the `wiki/` folder. 
- If it exists, it prints `-> [Topic] already exists. Skipping...` and moves on to the next one instantly without querying the Wikipedia API. 
- This ensures you never waste time or API requests downloading the same content twice.

---

## Summary of Importance Ranks
Remember that the script automatically filters out obscure topics. If you add a topic and it doesn't generate a page, it means its rank was too low!

- **Rank 1:** > 1000 incoming links (Essential)
- **Rank 2:** > 500 incoming links (Major)
- **Rank 3:** > 250 incoming links (Standard)
*Ranks 4, 5, and 6 are ignored by default.* To change this, edit the `RANK_THRESHOLD` variable in the script.
