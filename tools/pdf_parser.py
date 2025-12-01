from pypdf import PdfReader

def parse_pdf(pdf_path: str, max_pages=15) -> str:
    """
    Extracts text from the PDF (first 15 pages by default).
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages[:max_pages]:
            text += page.extract_text() or ""
        print(f"📄 Extracted {len(text)} characters from PDF.")
        return text
    except Exception as e:
        raise RuntimeError(f"Error parsing PDF: {e}")
