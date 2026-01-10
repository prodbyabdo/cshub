import pdfplumber
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

pdf_path = r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\data\CALC QUESTIONS ONLY.pdf"
output_dir = Path(r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\output_pdfplumber")
output_dir.mkdir(exist_ok=True)

try:
    with pdfplumber.open(pdf_path) as pdf:
        markdown = []
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text() or f"[Could not extract text from page {i}]"
            markdown.append(f"## Page {i}\n\n{text}\n\n")
        
    output_file = output_dir / "CALC_QUESTIONS_ONLY.md"
    output_file.write_text("\n".join(markdown), encoding='utf-8')
    print(f"✓ Done! Saved to {output_file}")
    print(f"✓ Processed {len(pdf.pages)} pages")
except Exception as e:
    print(f"✗ Error: {e}")