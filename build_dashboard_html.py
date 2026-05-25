import markdown
from pathlib import Path

md_path = Path("Accounting_Study_Dashboard.md")
html_out_path = Path("year1sem2accounting.html")

md_text = md_path.read_text(encoding="utf-8")

# Convert markdown to html with tables extension
html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

# Wrap everything in our standard beautifully styled HTML template
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accounting Study Dashboard | CS Hub</title>
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
            line-height: 1.7;
        }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        
        .nav-back {{ 
            display: inline-block; margin-bottom: 20px; color: var(--text-secondary); 
            text-decoration: none; font-family: var(--font-mono); 
        }}
        .nav-back:hover {{ color: var(--accent-color); }}
        
        /* Typography */
        h1 {{ font-size: 2.5rem; color: var(--accent-color); margin-top: 50px; border-bottom: 1px solid var(--border-color); padding-bottom: 15px; }}
        h1:first-of-type {{ margin-top: 0; }}
        h2 {{ font-size: 1.8rem; color: var(--text-primary); margin-top: 40px; border-left: 4px solid var(--accent-color); padding-left: 15px; }}
        h3 {{ font-size: 1.3rem; color: var(--text-secondary); font-family: var(--font-mono); margin-top: 30px; }}
        p {{ margin-bottom: 20px; }}
        
        strong {{ color: var(--accent-color); }}
        em {{ color: var(--text-secondary); }}
        
        /* Blockquote for callouts */
        blockquote {{
            background: var(--card-bg);
            border-left: 4px solid var(--accent-color);
            margin: 20px 0;
            padding: 15px 20px;
            border-radius: 0 8px 8px 0;
        }}
        
        /* Code blocks */
        pre {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: var(--font-mono);
            font-size: 0.9rem;
            color: var(--text-primary);
        }}
        code {{
            font-family: var(--font-mono);
            background: rgba(255,255,255,0.1);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9em;
            color: var(--accent-color);
        }}
        pre code {{
            background: none;
            padding: 0;
            color: inherit;
        }}

        /* Table Styling (crucial for ledgers) */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            background: var(--card-bg);
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }}
        thead {{
            background: rgba(0, 255, 136, 0.05);
            border-bottom: 2px solid var(--border-color);
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}
        th {{
            color: var(--accent-color);
            font-family: var(--font-mono);
            font-weight: 600;
            font-size: 0.9rem;
        }}
        td {{
            color: var(--text-primary);
        }}
        tr:last-child td {{
            border-bottom: none;
        }}
        tr:nth-child(even) {{
            background: rgba(255,255,255,0.02);
        }}
        
        /* Horizontal Rule */
        hr {{
            border: none;
            border-top: 1px dashed var(--border-color);
            margin: 40px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="year1.html" class="nav-back">← Back to Year 1</a>
        <div class="content">
            {html_content}
        </div>
    </div>
</body>
</html>
"""

final_html = TEMPLATE.format(html_content=html_content)
html_out_path.write_text(final_html, encoding="utf-8")
print(f"Successfully generated {html_out_path}")
