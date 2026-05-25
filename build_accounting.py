import re
from pathlib import Path

f1_path = Path("fiancialaccountingone.md")
f2_path = Path("accounting.md")

with open(f1_path, "r", encoding="utf-8") as f:
    text1 = f.read()

with open(f2_path, "r", encoding="utf-8") as f:
    text2 = f.read()

# Merge strategy
# 1. Definitions
# 2. Cheatcodes
# 3. MCQs
# 4. Long Solving
# 5. Trial Balances
# 6. Answer Sheets

content = ""

# Instead of complex parsing, let's just combine the texts clearly
# with headers and then simply wrap them in HTML paragraphs/cards

def format_markdown_to_html(text):
    html = ""
    lines = text.split('\n')
    in_list = False
    
    current_card = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_card:
                html += f'<div class="item-card"><div class="item-content">{current_card}</div></div>\n'
                current_card = ""
            continue
            
        if line.startswith("# "):
            if current_card:
                html += f'<div class="item-card"><div class="item-content">{current_card}</div></div>\n'
                current_card = ""
            html += f'<h1 class="lecture-title">{line[2:]}</h1>\n'
        elif line.startswith("## "):
            if current_card:
                html += f'<div class="item-card"><div class="item-content">{current_card}</div></div>\n'
                current_card = ""
            html += f'<h2 class="lecture-subtitle" style="color:var(--accent-color); margin-top:30px;">{line[3:]}</h2>\n'
        elif line.startswith("### "):
            current_card += f"<strong>{line[4:]}</strong><br>"
        elif re.match(r'^\d+\.', line): # e.g. "1. Question"
            if "A. " in line and "B. " in line:
                # Format MCQ nicely
                q_part = line.split(" A. ")[0]
                options = line[len(q_part):].strip()
                current_card += f"<strong>{q_part}</strong><br><span style='color:var(--text-secondary);'>{options}</span><br><br>"
            else:
                current_card += f"<strong>{line}</strong><br>"
        elif line.startswith("**") and line.endswith("**"):
            current_card += f"<strong>{line[2:-2]}</strong><br>"
        elif line.startswith("*"):
            current_card += f"• {line[1:].strip()}<br>"
        else:
            # check for inline bolding
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            current_card += f"{line}<br>"

    if current_card:
        html += f'<div class="item-card"><div class="item-content">{current_card}</div></div>\n'

    return html

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Principles of Accounting | CS Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet" />
    <style>
        :root {{
            --bg-color: #0a0a0a;
            --card-bg: #111111;
            --text-primary: #ffffff;
            --text-secondary: #a0a0a0;
            --accent-color: #00ff88;
            --accent-dim: rgba(0, 255, 136, 0.1);
            --border-color: #333333;
            --font-main: "Inter", sans-serif;
            --font-mono: "JetBrains Mono", monospace;
        }}
        body {{
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: var(--font-main);
            margin: 0;
            padding: 40px 20px;
            line-height: 1.6;
        }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        header {{ margin-bottom: 60px; border-bottom: 1px solid var(--border-color); padding-bottom: 20px; }}
        h1 {{ margin: 0; font-size: 2.5rem; color: var(--accent-color); }}
        .subtitle {{ font-family: var(--font-mono); color: var(--text-secondary); font-size: 1rem; margin-top: 10px; }}
        .nav-back {{ display: inline-block; margin-bottom: 20px; color: var(--text-secondary); text-decoration: none; font-family: var(--font-mono); }}
        .nav-back:hover {{ color: var(--accent-color); }}
        
        .lecture-title {{ font-size: 2rem; margin-bottom: 20px; color: var(--text-primary); border-left: 4px solid var(--accent-color); padding-left: 15px; margin-top: 50px; }}
        
        .item-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 20px;
            transition: transform 0.2s, border-color 0.2s;
        }}
        .item-card:hover {{
            transform: translateY(-2px);
            border-color: var(--accent-color);
        }}
        .item-content {{ white-space: normal; }}
        strong {{ color: var(--accent-color); }}
    </style>
</head>
<body>
    <div class="container">
        <a href="year1.html" class="nav-back">← Back to Year 1</a>
        <header>
            <h1>Principles of Accounting</h1>
            <div class="subtitle">Semester 2 Year 1 | Frank Wood's Business Accounting 1-6</div>
        </header>
        
        {content}
        
    </div>
</body>
</html>
"""

# Let's combine the text into logical parts
combined_text = ""
combined_text += "# Comprehensive Glossary & Core Logic\n\n"
combined_text += text1.split("1. Which of the following is the best definition of accounting?")[0]
combined_text += "\n\n# Enterprise Accounting Exam Practice\n\n"

# Only take the first part of accounting.md up to the cheatcodes, since we have a better cheat code
part_acc = text2.split("File 2: The MCQ Cheatcode")[0]
combined_text += part_acc

combined_text += "\n\n# 100 Multiple Choice Questions Bank\n\n"
mcqs_part = text1.split("1. Which of the following is the best definition of accounting?")[1]
mcqs_part = "1. Which of the following is the best definition of accounting?" + mcqs_part
combined_text += mcqs_part

# Format and save
html_body = format_markdown_to_html(combined_text)
final_html = TEMPLATE.format(content=html_body)

Path("year1sem2accounting.html").write_text(final_html, encoding="utf-8")
print("Successfully generated year1sem2accounting.html")
