import os
from pathlib import Path
import re

# Configuration
SOURCE_DIR = Path("output_pdfplumber/markdown_cache/INTRODUCTION TO CS&IT")
OUTPUT_HTML = "year1sem1introcs.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction to CS | CS Hub</title>
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
            padding: 0;
            line-height: 1.6;
        }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 40px 20px; }}
        
        header {{ margin-bottom: 40px; border-bottom: 1px solid var(--border-color); padding-bottom: 20px; }}
        h1 {{ margin: 0; font-size: 2.5rem; color: var(--accent-color); font-weight: 800; }}
        .subtitle {{ color: var(--text-secondary); font-family: var(--font-mono); margin-top: 10px; }}
        
        .nav-back {{ display: inline-block; margin-bottom: 20px; color: var(--text-secondary); text-decoration: none; font-family: var(--font-mono); }}
        .nav-back:hover {{ color: var(--accent-color); }}

        /* Tabs */
        .tabs {{ display: flex; gap: 10px; margin-bottom: 30px; border-bottom: 1px solid var(--border-color); }}
        .tab-btn {{
            background: none; border: none; color: var(--text-secondary); 
            padding: 10px 20px; font-family: var(--font-mono); font-size: 1rem; cursor: pointer;
            border-bottom: 2px solid transparent; transition: all 0.2s;
        }}
        .tab-btn:hover {{ color: var(--text-primary); }}
        .tab-btn.active {{ color: var(--accent-color); border-bottom-color: var(--accent-color); }}

        .tab-content {{ display: none; animation: fadeIn 0.3s ease; }}
        .tab-content.active {{ display: block; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}

        /* Content Styles */
        h2 {{ color: var(--text-primary); border-left: 4px solid var(--accent-color); padding-left: 15px; margin-top: 40px; }}
        h3 {{ color: var(--accent-color); margin-top: 30px; font-family: var(--font-mono); }}
        h4 {{ color: var(--text-primary); margin-top: 20px; text-decoration: underline; }}
        
        .card {{
            background: var(--card-bg); border: 1px solid var(--border-color);
            border-radius: 8px; padding: 20px; margin-bottom: 15px;
        }}
        .definition {{ display: grid; grid-template-columns: 200px 1fr; gap: 20px; }}
        .term {{ color: var(--accent-color); font-weight: bold; font-family: var(--font-mono); }}
        
        .question-card {{ background: var(--card-bg); padding: 20px; border-radius: 8px; margin-bottom: 15px; border: 1px solid var(--border-color); }}
        .question-text {{ font-weight: 600; margin-bottom: 10px; }}
        .options {{ list-style: none; padding: 0; }}
        .options li {{ margin-bottom: 5px; color: var(--text-secondary); }}
        
        blockquote {{ border-left: 2px solid var(--border-color); margin: 0; padding-left: 15px; color: var(--text-secondary); }}
        
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; color: var(--text-secondary); }}
        td {{ padding: 8px; border-bottom: 1px solid #333; }}
        tr:last-child td {{ border-bottom: none; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="year1.html" class="nav-back">← Back to Year 1</a>
        <header>
            <h1>Introduction to CS</h1>
            <div class="subtitle">COM115 Resources & Study Guide</div>
        </header>

        <div class="tabs">
            <button class="tab-btn active" onclick="openTab('definitions')">Definitions</button>
            <button class="tab-btn" onclick="openTab('exam')">Mock Exam</button>
        </div>

        <!-- Definitions Tab -->
        <div id="definitions" class="tab-content active">
            {definitions_content}
        </div>

        <!-- Exam Tab -->
        <div id="exam" class="tab-content">
            {exam_content}
        </div>

    </div>

    <script>
        function openTab(tabName) {{
            // Hide all
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            
            // Show target
            document.getElementById(tabName).classList.add('active');
            
            // Highlight button (simple logic for now)
            const buttons = document.querySelectorAll('.tab-btn');
            if(tabName === 'definitions') buttons[0].classList.add('active');
            if(tabName === 'exam') buttons[1].classList.add('active');
        }}
    </script>
</body>
</html>
"""

def parse_definitions(md_text):
    html = ""
    # Split by double newline to get blocks
    blocks = md_text.split('\\n\\n')
    
    current_term = None
    
    for block in blocks:
        block = block.strip()
        if not block: continue
        
        if block.startswith('#'): continue # Skip headers
        
        # Assume format: **Term**\\nDefinition
        if block.startswith('**'):
            parts = block.split('\\n', 1)
            term = parts[0].replace('**', '').strip()
            desc = parts[1].strip() if len(parts) > 1 else ""
            
            html += f"""
            <div class="card definition">
                <div class="term">{term}</div>
                <div class="desc">{desc}</div>
            </div>
            """
    return html

def parse_exam(md_text):
    html = ""
    lines = md_text.split('\\n')
    
    in_matching_section = False
    in_question_block = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Detect Sections
        if line.startswith("## Part 3"):
            in_matching_section = True
            html += f"<h2>{line.replace('## ', '')}</h2>"
            continue
        elif line.startswith("## "):
            if in_matching_section and "table" in html: html += "</table>"
            in_matching_section = False
            html += f"<h2>{line.replace('## ', '')}</h2>"
            continue
            
        # Matching Section Handling
        if in_matching_section:
            if line.startswith("**Group"):
                if "table" in html and "Group" not in line: html += "</table>"
                html += f"<h4>{line.replace('**', '')}</h4>"
                html += '<table style="width:100%; border-collapse: collapse; margin-bottom: 20px;">'
                continue
            
            # Check if it's a matching line "31. Item ....... A. Description"
            match = re.search(r'^(\d+\..*?)(\.{2,})\s*([A-Z]\..*)', line)
            if match:
                col1 = match.group(1).strip()
                col2 = match.group(3).strip()
                html += f'<tr><td style="width: 50%;">{col1}</td><td style="width: 50%;">{col2}</td></tr>'
            elif line.startswith("*Match") or line.startswith("*Indicate") or line.startswith("Answer") or line.startswith("Part"):
                 if "table" in html: html += "</table>"
                 html += f"<p><i>{line.replace('*','')}</i></p>"
            elif "Answer Key" in line:
                 if "table" in html: html += "</table>"
                 in_matching_section = False
                 html += f"<h2>{line.replace('# ', '')}</h2>"
            else:
                html += f"<div>{line}</div>"
            continue

        # Normal Questions
        if line.startswith("###"):
            html += f"<h3>{line.replace('###', '')}</h3>"
            continue
            
        if re.match(r'^\d+\.', line):
            if in_question_block: html += "</div>"
            html += f'<div class="question-card"><div class="question-text">{line}</div>'
            in_question_block = True
        elif re.match(r'^[a-z]\)', line, re.IGNORECASE): # MCQ option
            html += f'<div style="margin-left: 20px; color: #a0a0a0;">{line}</div>'
        else:
             if in_question_block:
                 html += f'<div>{line}</div>'
             else:
                 html += f'<p>{line}</p>'

    if in_question_block: html += "</div>"
    if in_matching_section and "table" in html: html += "</table>"
    
    return html

def main():
    if not SOURCE_DIR.exists():
        print(f"Source dir {SOURCE_DIR} not found!")
        return

    # 1. Definitions
    def_path = SOURCE_DIR / "IntroCS_Definitions.md"
    def_content = "Terms not found."
    if def_path.exists():
        with open(def_path, "r", encoding="utf-8") as f:
            def_content = parse_definitions(f.read())
            
    # 2. Exam
    exam_path = SOURCE_DIR / "IntroCS_MockExam.md"
    exam_content = "Exam not found."
    if exam_path.exists():
        with open(exam_path, "r", encoding="utf-8") as f:
            exam_content = parse_exam(f.read())
            
            
    final_html = TEMPLATE.format(
        definitions_content=def_content,
        exam_content=exam_content
    )
    
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Built {OUTPUT_HTML}")
