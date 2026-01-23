from math_doc_tool.core import ExtractedItem
import pdfplumber

class TextExtractor:
    def extract(self, pdf_path):
        items = []
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    # Clean up basic issues
                    text = text.strip()
                    if len(text) > 50: # Skip empty/header-only pages
                        items.append(ExtractedItem(
                            item_type="Page Content",
                            category="Raw Text",
                            content=text,
                            page_number=i+1
                        ))
        return items
