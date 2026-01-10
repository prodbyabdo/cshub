import re
import os
from pathlib import Path

# Configuration
INPUT_DIR = Path(r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\output_pdfplumber")
SOLUTIONS_HTML_PATH = INPUT_DIR / "calculus_solutions.html"

def extract_solutions(md_content):
    """
    Extracts 'Examples' and 'Exercises' from Markdown content.
    Returns a list of dictionaries with 'type', 'number', 'statement', and 'solution'.
    """
    problems = []
    lines = md_content.split('\n')
    current_problem = None
    capture_mode = "NONE" # NONE, STATEMENT, SOLUTION, SKIP
    
    # Regex patterns
    # Example 1.2.1 Find ...
    # Exercise 2.2.2 Find ...
    start_pattern = re.compile(r'^(Example|Exercise)\s+(\d+(\.\d+)+)\s*(.*)', re.IGNORECASE)
    sol_pattern = re.compile(r'^Sol\s*$', re.IGNORECASE)
    page_pattern = re.compile(r'^## Page|^Semester 1|^Faculty of', re.IGNORECASE)
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for new problem start
        match = start_pattern.match(line)
        if match:
            # Save previous problem if valid
            if current_problem:
                problems.append(current_problem)
            
            p_type = match.group(1)   # Example or Exercise
            p_num = match.group(2)    # 1.2.1
            p_rest = match.group(4)   # Remainder of line (start of statement)
            
            current_problem = {
                'type': p_type,
                'number': p_num,
                'statement': [p_rest] if p_rest else [],
                'solution': []
            }
            capture_mode = "STATEMENT"
            continue
            
        # Check for Solution start marker
        if current_problem and sol_pattern.match(line):
            capture_mode = "SOLUTION"
            continue
            
        # Check for page breaks or interruptions
        if page_pattern.match(line):
             # Don't close the problem yet, just ignore the page header lines
             # But if we are in STATEMENT mode and hit a definition, maybe stop?
             # For simplicity, we just ignore these lines and continue capturing
             continue

        # Capture content based on mode
        if current_problem:
            if capture_mode == "STATEMENT":
                current_problem['statement'].append(line)
            elif capture_mode == "SOLUTION":
                current_problem['solution'].append(line)
    
    # Append the last one
    if current_problem:
        problems.append(current_problem)
        
    return problems

def generate_problem_card(problem):
    """Generates an HTML problem card."""
    kind = problem['type'] # Example or Exercise
    num = problem['number']
    
    statement_text = " ".join(problem['statement'])
    solution_lines = problem['solution']
    
    # If no solution found (e.g. Exercise without Sol), handle gracefully
    if not solution_lines:
        solution_lines = ["(Solution not provided in lecture notes)"]
    
    # Wrap solution steps in divs
    formatted_steps = ""
    for step in solution_lines:
        # Heuristic: if line contains math or looks concise, treat as step
        # Ideally we'd split by period or logic, but line-by-line is safe for now
        formatted_steps += f'<div class="solution-step">{step}</div>\n'
        
    return f"""
    <div class="problem-card">
      <div class="problem-header"><span class="problem-number">{kind} {num}</span></div>
      <div class="problem-statement">
        {statement_text}
      </div>
      <div class="solution-details">
        {formatted_steps}
      </div>
    </div>
    """

def update_solutions_html():
    print("Scanning for new solutions...")
    
    new_html_blocks = []
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
            extracted = extract_solutions(content)
            print(f"  Found {len(extracted)} problems.")
            
            # Group by lecture/file? Or just dump them? 
            # Let's add a header for the file to categorize them visually
            if extracted:
                new_html_blocks.append(f'<div class="section"><h3>Extracted from {filename}</h3>')
                for p in extracted:
                    new_html_blocks.append(generate_problem_card(p))
                new_html_blocks.append('</div>')

    if not new_html_blocks:
        print("No new solutions found.")
        return

    # Append to HTML
    if SOLUTIONS_HTML_PATH.exists():
        html_content = SOLUTIONS_HTML_PATH.read_text(encoding='utf-8')
        
        # Insert before footer, similar to laws script
        # Look for the footer opening tag or the last container div
        marker_start = "<!-- END_AUTOMATED_SOLUTIONS -->"
        
        if marker_start not in html_content:
            insert_point = html_content.find("<footer>")
            if insert_point == -1:
                # Fallback to last div closing of main container
                insert_point = html_content.rfind("</div>")
                insert_point = html_content.rfind("</div>", 0, insert_point) # Go back one level to stay inside container
            
            if insert_point != -1:
                new_content = "\n<!-- START AUTOMATED SECTIONS -->\n" + "\n".join(new_html_blocks) + f"\n{marker_start}\n"
                final_html = html_content[:insert_point] + new_content + html_content[insert_point:]
                SOLUTIONS_HTML_PATH.write_text(final_html, encoding='utf-8')
                print("Successfully appended new solutions to HTML.")
            else:
                print("Error: Could not find insertion point.")
        else:
            print("Marker exists, skipping (logic to replace not implemented yet).")

if __name__ == "__main__":
    update_solutions_html()
