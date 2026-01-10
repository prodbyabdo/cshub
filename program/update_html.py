"""
Update HTML Docs with Extracted Content
Parses generated Markdown files and injects content into calculus_laws.html and calculus_solutions.html
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

def normalize_text(text):
    """Normalize text for fuzzy comparison (remove whitespace, case-insensitive)."""
    return re.sub(r'\s+', '', text).lower()

class HTMLUpdater:
    def __init__(self, laws_path: Path, solutions_path: Path):
        self.laws_path = laws_path
        self.solutions_path = solutions_path
        
        # Load existing content for duplicate checking
        self.existing_laws_fingerprints = set()
        self.existing_solutions_fingerprints = set()
        
        self._load_fingerprints()

    def _load_fingerprints(self):
        """Load fingerprints from existing HTML files."""
        if self.laws_path.exists():
            soup = BeautifulSoup(self.laws_path.read_text(encoding='utf-8'), 'html.parser')
            for box in soup.find_all(class_='formula-box'):
                self.existing_laws_fingerprints.add(normalize_text(box.get_text()))
        
        if self.solutions_path.exists():
            soup = BeautifulSoup(self.solutions_path.read_text(encoding='utf-8'), 'html.parser')
            for card in soup.find_all(class_='problem-card'):
                self.existing_solutions_fingerprints.add(normalize_text(card.get_text()))
                
    def parse_markdown(self, md_path: Path):
        """Parse MD file into list of items."""
        content = md_path.read_text(encoding='utf-8')
        items = []
        
        # Split by H3 headers (### Type (Page X))
        sections = re.split(r'^###\s+(.*?)\s+\(Page\s+(\d+)\)', content, flags=re.MULTILINE)
        
        for i in range(1, len(sections), 3):
            item_type = sections[i]
            page_num = sections[i+1]
            body_text = sections[i+2]
            
            # Extract Category
            cat_match = re.search(r'\*\*Category:\*\*\s+(\w+)', body_text)
            category = cat_match.group(1) if cat_match else "Unknown"
            
            # Parse Statement and Solution
            statement = ""
            solution = ""
            
            # Find Statement block
            stmt_match = re.search(r'\*\*Statement:\*\*(.*?)(?=\*\*Solution:\*\*|---|$)', body_text, re.DOTALL)
            if stmt_match:
                statement = self._clean_quote_block(stmt_match.group(1))
            
            # Find Solution block
            sol_match = re.search(r'\*\*Solution:\*\*(.*?)(?=---|$)', body_text, re.DOTALL)
            if sol_match:
                solution = self._clean_quote_block(sol_match.group(1))
            
            # Fallback for Laws or if no split found
            if not statement and not solution:
                # Treat everything after category as content
                raw_content = re.sub(r'\*\*Category:\*\*.*?\n', '', body_text, count=1, flags=re.DOTALL)
                statement = self._clean_quote_block(raw_content)

            items.append({
                'type': item_type,
                'page': page_num,
                'category': category,
                'content': statement, # For Laws, content is just the statement
                'solution': solution, # Only for Solutions
                'source': md_path.stem
            })
            
        return items

    def _clean_quote_block(self, text):
        lines = []
        for line in text.strip().split('\n'):
            line = line.strip()
            if line.startswith('> '):
                lines.append(line[2:])
            elif line.startswith('>'):
                lines.append(line[1:])
            elif line: # Keep non-quote lines too if any
                lines.append(line)
        return '\n'.join(lines).strip()

    def update_laws(self, new_items):
        if not self.laws_path.exists():
            print("Laws HTML not found!")
            return

        soup = BeautifulSoup(self.laws_path.read_text(encoding='utf-8'), 'html.parser')
        container = soup.find(class_='content')
        
        # Create a new section for the imports if not exists? 
        # Or just append to a general "Additional Notes" section?
        # Let's create a new section for each source file or just one "Additional Material" section.
        
        # Let's make a new section "8. Additional Lecture Notes"
        new_section = soup.new_tag('div', attrs={'class': 'section'})
        h2 = soup.new_tag('h2')
        h2.string = "8. Additional Lecture Notes"
        new_section.append(h2)
        
        count = 0
        for item in new_items:
            if item['category'] != 'Law':
                continue
                
            fingerprint = normalize_text(item['content'])
            if fingerprint in self.existing_laws_fingerprints:
                print(f"Skipping duplicate Law: {item['type']} (Page {item['page']})")
                continue
            
            # Add to HTML
            box = soup.new_tag('div', attrs={'class': 'formula-box'})
            
            # Header
            p_head = soup.new_tag('p')
            strong = soup.new_tag('strong')
            strong.string = f"{item['type']} (from {item['source']}, p{item['page']}):"
            p_head.append(strong)
            box.append(p_head)
            
            # Content (convert newlines to <br> or paragraphs)
            # Simple text node for now, allowing MathJax to parse LateX
            p_content = soup.new_tag('div')
            p_content.string = item['content'] 
            # Note: setting string escapes HTML. If content has HTML, use other methods.
            # But our content is Latex/Text.
            
            box.append(p_content)
            new_section.append(box)
            self.existing_laws_fingerprints.add(fingerprint)
            count += 1
            
        if count > 0:
            container.append(new_section)
            self.laws_path.write_text(str(soup.prettify()), encoding='utf-8')
            print(f"Added {count} new laws to HTML.")

    def update_solutions(self, new_items):
        if not self.solutions_path.exists():
            print("Solutions HTML not found!")
            return

        soup = BeautifulSoup(self.solutions_path.read_text(encoding='utf-8'), 'html.parser')
        main_container = soup.find(class_='container')
        
        new_section = soup.new_tag('div', attrs={'class': 'section'})
        h2 = soup.new_tag('h2', attrs={'class': 'section-title'})
        h2.string = "Additional Practice Problems"
        new_section.append(h2)
        
        count = 0
        for item in new_items:
            if item['category'] != 'Solution':
                continue
                
            fingerprint = normalize_text(item['content'])
            if fingerprint in self.existing_solutions_fingerprints:
                print(f"Skipping duplicate Solution: {item['type']} (Page {item['page']})")
                continue
                
            # Create Card
            card = soup.new_tag('div', attrs={'class': 'problem-card'})
            
            # Header
            header = soup.new_tag('div', attrs={'class': 'problem-header'})
            num = soup.new_tag('span', attrs={'class': 'problem-number'})
            num.string = f"{item['type']} - {item['source']} P{item['page']}"
            header.append(num)
            card.append(header)
            
            # Statement
            statement = soup.new_tag('div', attrs={'class': 'problem-statement'})
            for line in item['content'].split('\n'):
                div = soup.new_tag('div')
                div.string = line
                statement.append(div)
            card.append(statement)
            
            # Solution Details
            if item['solution']:
                details = soup.new_tag('div', attrs={'class': 'solution-details'})
                for line in item['solution'].split('\n'):
                    step = soup.new_tag('div', attrs={'class': 'solution-step'})
                    step.string = line
                    details.append(step)
                card.append(details)
                
            new_section.append(card)
            
            self.existing_solutions_fingerprints.add(fingerprint)
            count += 1
            
        if count > 0:
            main_container.append(new_section)
            self.solutions_path.write_text(str(soup.prettify()), encoding='utf-8')
            print(f"Added {count} new solutions to HTML.")


def main():
    base_dir = Path(__file__).parent.parent
    md_dir = base_dir / "output_pdfplumber"
    
    laws_html = md_dir / "calculus_laws.html"
    sols_html = md_dir / "calculus_solutions.html"
    
    updater = HTMLUpdater(laws_html, sols_html)
    
    # Process all generated MDs
    md_files = list(md_dir.glob("Calculus_1_lecnote*.md"))
    all_items = []
    
    for md_file in md_files:
        print(f"Parsing {md_file.name}...")
        items = updater.parse_markdown(md_file)
        all_items.extend(items)
        
    print(f"Total items found: {len(all_items)}")
    
    updater.update_laws(all_items)
    updater.update_solutions(all_items)

if __name__ == "__main__":
    main()
