"""
Cleanup HTML Script
Removes the sections added by the previous update run.
"""
from pathlib import Path
from bs4 import BeautifulSoup

def main():
    base_dir = Path(__file__).parent.parent
    laws_path = base_dir / "output_pdfplumber" / "calculus_laws.html"
    sols_path = base_dir / "output_pdfplumber" / "calculus_solutions.html"
    
    # Clean Laws
    if laws_path.exists():
        soup = BeautifulSoup(laws_path.read_text(encoding='utf-8'), 'html.parser')
        # Find the section "8. Additional Lecture Notes"
        for section in soup.find_all('div', class_='section'):
            h2 = section.find('h2')
            if h2 and "8. Additional Lecture Notes" in h2.get_text():
                section.decompose()
                print(f"Removed 'Additional Lecture Notes' from {laws_path.name}")
                
        laws_path.write_text(str(soup.prettify()), encoding='utf-8')

    # Clean Solutions
    if sols_path.exists():
        soup = BeautifulSoup(sols_path.read_text(encoding='utf-8'), 'html.parser')
        # Find the section "Additional Practice Problems"
        for section in soup.find_all('div', class_='section'):
            h2 = section.find('h2')
            if h2 and "Additional Practice Problems" in h2.get_text():
                section.decompose()
                print(f"Removed 'Additional Practice Problems' from {sols_path.name}")
                
        sols_path.write_text(str(soup.prettify()), encoding='utf-8')

if __name__ == "__main__":
    main()
