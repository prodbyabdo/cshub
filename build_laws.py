import re
import os
from pathlib import Path

# Configuration
INPUT_DIR = Path(r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\output_pdfplumber")
LAWS_HTML_PATH = INPUT_DIR / "year1sem1calclaws.html"

def extract_laws(md_content):
    """
    Extracts 'Definitions', 'Properties', and 'Identities' from Markdown content.
    Returns a list of dictionaries with 'title' and 'content'.
    """
    laws = []
    lines = md_content.split('\n')
    current_law = None
    capture_mode = False
    
    # Regex for "Equation-like" lines (heuristic)
    # Contains =, >, <, or common math functions
    math_pattern = re.compile(r'[=><+]|\\|lim|sinh|cosh|tanh|coth|sech|csch', re.IGNORECASE)
    # Regex for "Explanation-like" start words
    explanation_start = re.compile(r'^(We|The|Consider|Proof|Since|This|For|Now|Clearly|To|If|Also|In|Note)', re.IGNORECASE)
    
    # Simple heuristic regexes for headers in this specific MD format
    # "1.1 Hyperbolic Sine Function", "1.1.1 Properties", "Definition:", etc.
    header_pattern = re.compile(r'^(\d+(\.\d+)+)\s+(.*)|^(Properties)|^(Definition)$', re.IGNORECASE)

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        match = header_pattern.match(line)
        if match:
            # If we were capturing, save the previous law
            if current_law:
                laws.append(current_law)
            
            # Start new law
            title = match.group(0)
            current_law = {'title': title, 'content': []}
            capture_mode = True
        elif capture_mode:
            # Stop capturing if we hit a page break
            if line.startswith("## Page") or "Semester 1" in line:
                # pause capture, don't close yet in case it continues next page? 
                # actually, simpler to close and reopen if new header found.
                # For now, just skip these lines.
                continue
            
            # FILTERING LOGIC:
            # 1. Skip obvious explanations or page numbers
            if explanation_start.match(line) or "HYPERBOLIC FUNCTIONS" in line or "(pg" in line:
                continue
            # 2. Skip formatting junk (single/double chars that aren't math)
            if len(line) < 3 and not math_pattern.search(line):
                 continue
            # 3. Skip lines that look like loose OCR chars (e.g. "a b c")
            if re.match(r'^[\w\s]{1,5}$', line):
                 continue
            
            # 3. Check if it looks like math
            if math_pattern.search(line) or len(line) < 60:
                current_law['content'].append(line)
    
    if current_law:
        laws.append(current_law)
        
    return laws

def generate_law_html(law):
    """Converts a law dictionary to an HTML block."""
    title = law['title']
    raw_lines = law['content']
    
    # Basic LaTeXification
    formatted_lines = []
    for line in raw_lines:
        # Heuristic replacements
        clean_line = line.replace("sinh", r"\sinh ") \
                         .replace("cosh", r"\cosh ") \
                         .replace("tanh", r"\tanh ") \
                         .replace("lim", r"\lim ") \
                         .replace("cid:112", "sqrt") \
                         .replace("cid:18", "") \
                         .replace("(sqrt)", r"\sqrt{}") # Attempt to fix placeholder
        
        # Remove remaining garbage chars often found in OCR math
        # e.g. "a", "o", "z" at ends of lines
        clean_line = re.sub(r'\s+[a-z]\s*$', '', clean_line)
        
        # Determine if it should be block math
        if "=" in clean_line or "lim" in clean_line or "\\" in clean_line:
            formatted_lines.append(f"\\[ {clean_line} \\]")
        else:
            formatted_lines.append(f"{clean_line}<br>")

    content_text = "\n".join(formatted_lines)
    
    # Matches structure of other sections: h3 + formula-box (no nested .section)
    return f"""
        <h3>{title}</h3>
        <div class="formula-box">
            {content_text}
        </div>
    """

def update_laws_html():
    """Main function to update calculus_laws.html"""
    print("Scanning for new laws...")
    
    new_html_blocks = []
    
    # Scan specific files (or all .md files if generalized)
    target_files = [
        "Calculus 1 lecnote6_202512281307_52093.md",
        "Calculus 1 lecnote7_202512281308_09617.md",
        "Calculus 1 lecnote8_202512281308_49361.md"
    ]
    
    for filename in target_files:
        path = INPUT_DIR / filename
        if path.exists():
            print(f"Processing {filename}...")
            content = path.read_text(encoding='utf-8')
            extracted = extract_laws(content)
            print(f"  Found {len(extracted)} potential sections.")
            
            for law in extracted:
                # Filter out likely junk/short sections
                if len(law['content']) > 2: 
                    new_html_blocks.append(generate_law_html(law))
        else:
            print(f"Warning: {filename} not found.")

    if not new_html_blocks:
        print("No new laws found to append.")
        return

    # Append to HTML
    if LAWS_HTML_PATH.exists():
        html_content = LAWS_HTML_PATH.read_text(encoding='utf-8')
        
        # Insert before the last closing tags or "Additional Lecture Notes" section
        # We'll try to find a marker, or just append to end of container
        marker = "<!-- END_AUTOMATED_LAWS -->"
        
        if marker in html_content:
            # If marker exists, we assume we previously appended content ending with this marker.
            # We need to find where we started. Since we didn't use a start marker before, 
            # we'll look for the "8. Additional Lecture Notes" header again.
            start_search = "8. Additional Lecture Notes"
            start_index = html_content.find(start_search)
            
            if start_index != -1:
                # Find the end of the header
                header_end_index = html_content.find("</h2>", start_index) + 5
                # Find the marker
                marker_index = html_content.find(marker) + len(marker)
                
                # Construct new content
                new_content = "\n" + "\n".join(new_html_blocks) + f"\n{marker}\n"
                
                # Replace the chunk
                final_html = html_content[:header_end_index] + new_content + html_content[marker_index:]
                LAWS_HTML_PATH.write_text(final_html, encoding='utf-8')
                print("Successfully UPDATED laws in HTML.")
            else:
                 print("Error: Could not find start section to update.")
        
        else:
            # If marker starts doesn't exist, append as before
            insert_point = html_content.find("8. Additional Lecture Notes")
            if insert_point != -1:
                insert_point = html_content.find("</h2>", insert_point) + 5
                new_content = "\n" + "\n".join(new_html_blocks) + f"\n{marker}\n"
                final_html = html_content[:insert_point] + new_content + html_content[insert_point:]
                LAWS_HTML_PATH.write_text(final_html, encoding='utf-8')
                print("Successfully appended new laws to HTML.")

if __name__ == "__main__":
    update_laws_html()
