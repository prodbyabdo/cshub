import pdfplumber
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Define the input PDF paths
pdf_files = [
    r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\data\Calculus 1 lecnote6_202512281307_52093.pdf",
    r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\data\Calculus 1 lecnote7_202512281308_09617.pdf",
    r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\data\Calculus 1 lecnote8_202512281308_49361.pdf"
]

output_dir = Path(r"C:\Users\abdel\OneDrive\Desktop\PDFOCR\output_pdfplumber")
output_dir.mkdir(exist_ok=True)

for pdf_path in pdf_files:
    try:
        print(f"Processing {Path(pdf_path).name}...")
        with pdfplumber.open(pdf_path) as pdf:
            markdown = []
            for i, page in enumerate(pdf.pages, 1):
                text = page.extract_text() or f"[Could not extract text from page {i}]"
                markdown.append(f"## Page {i}\n\n{text}\n\n")
        
        # Determine output filename (replace .pdf with .md)
        output_filename = Path(pdf_path).with_suffix('.md').name
        output_file = output_dir / output_filename
        
        output_file.write_text("\n".join(markdown), encoding='utf-8')
        print(f"[OK] Done! Saved to {output_file}")
        print(f"[OK] Processed {len(pdf.pages)} pages")
        
    except Exception as e:
        print(f"[ERROR] processing {pdf_path}: {e}")
