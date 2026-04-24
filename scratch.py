import os
import re
import json

folder = "contentforwiki"
categories = {}
pattern = re.compile(r'<li><a href="[^"]+" title="([^"]+)">')
for f in os.listdir(folder):
    if f.endswith(".html"):
        with open(os.path.join(folder, f), "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
            group_sections = re.findall(r'<div class="mw-category-group">(.*?)</div>', content, re.DOTALL)
            links = []
            for sec in group_sections:
                for match in pattern.findall(sec):
                    if not match.startswith("Category:") and not match.startswith("Wikipedia:"):
                        links.append(match)
            categories[f] = links

with open("scratch_topics.json", "w", encoding="utf-8") as out:
    json.dump(categories, out, indent=2)
