import os
from pathlib import Path

# Configuration
MARKDOWN_ROOT = Path("output_pdfplumber/markdown_cache")
HTML_OUTPUT_DIR = Path(".") # Root

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject} | Resources</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet" />
    <style>
        :root {{
            --bg-color: #0a0a0a;
            --card-bg: #111111;
            --text-primary: #ffffff;
            --text-secondary: #a0a0a0;
            --accent-color: #00ff88;
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
        .nav-back {{ display: inline-block; margin-bottom: 20px; color: var(--text-secondary); text-decoration: none; font-family: var(--font-mono); }}
        .nav-back:hover {{ color: var(--accent-color); }}
        
        .lecture-section {{ margin-bottom: 60px; }}
        .lecture-title {{ font-size: 1.5rem; margin-bottom: 20px; color: var(--text-primary); border-left: 4px solid var(--accent-color); padding-left: 15px; }}
        
        .item-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
        }}
        .item-type {{ 
            font-family: var(--font-mono); font-size: 0.8rem; color: var(--accent-color); 
            text-transform: uppercase; margin-bottom: 10px; display: block;
        }}
        .item-content {{ white-space: pre-wrap; }}
        blockquote {{ border-left: 2px solid var(--border-color); margin: 0; padding-left: 15px; color: var(--text-secondary); }}
    </style>
</head>
<body>
    <div class="container">
        <a href="year1.html" class="nav-back">← Back to Year 1</a>
        <header>
            <h1>{subject}</h1>
            <p>Extracted Resources & Notes</p>
        </header>
        
        {content}
        
    </div>
</body>
</html>
"""

def parse_markdown_file(md_path):
    """
    Parses a single markdown file and returns HTML string for its content.
    """
    content_html = ""
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    
    # Simple parsing: Split by "###" headers or just formatting
    # We want to identify items.
    
    # Split by "---" separator we used in batch_process
    chunks = md_text.split("\n---\n")
    
    # First chunk is usually header
    file_header = f'<div class="lecture-section"><div class="lecture-title">{md_path.stem}</div>'
    content_html += file_header
    
    has_items = False
    for chunk in chunks:
        if "###" in chunk:
            has_items = True
            # Extract type
            lines = chunk.strip().split('\n')
            item_type = "Note"
            item_body = []
            
            for line in lines:
                if line.startswith("###"):
                    item_type = line.replace("###", "").strip()
                elif line.startswith("**Category**"):
                    continue
                else:
                    item_body.append(line)
            
            body_html = "\n".join(item_body).replace(">", "") # Remove blockquote markers
            
            content_html += f"""
            <div class="item-card">
                <span class="item-type">{item_type}</span>
                <div class="item-content">{body_html}</div>
            </div>
            """
            
    if not has_items:
         content_html += """<div class="item-card"><div class="item-content">No specific definitions or examples extracted from this document.</div></div>"""

    content_html += "</div>" # Close lecture-section
    return content_html

def build_pages():
    subjects_map = {
        "Discrete Math New": "year1sem1discrete.html",
        "Econ": "year1sem1econ.html",
        "Information Systems": "year1sem1infosys.html",
        "Managment": "year1sem1management.html" # Note spelling in source dir
    }
    
    if not MARKDOWN_ROOT.exists():
        print("Markdown directory not found.")
        return

    for folder_name, out_filename in subjects_map.items():
        folder_path = MARKDOWN_ROOT / folder_name
        if not folder_path.exists():
            continue
            
        print(f"Building {out_filename} from {folder_name}...")
        
        all_content_html = ""
        # Sort files specifically? maybe by name
        files = sorted(list(folder_path.glob("*.md")))
        
        for md_file in files:
            all_content_html += parse_markdown_file(md_file)
            
        final_html = TEMPLATE.format(subject=folder_name, content=all_content_html)
        
        out_path = HTML_OUTPUT_DIR / out_filename
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_html)
            
        print(f"  Created {out_filename}")

if __name__ == "__main__":
    build_pages()
