import fitz  # PyMuPDF

def parse_pdf_to_text(file_path: str) -> str:
    """Extract text from PDF using PyMuPDF."""
    try:
        with fitz.open(file_path) as doc:
            pages = [page.get_text("text").strip() for page in doc]
        return "\n\n".join(pages)
    except Exception as e:
        print(f"[ERROR] Failed to parse PDF: {e}")
        return ""

def clean_text(text: str) -> str:
    """Replace problematic characters with safe equivalents."""
    replacements = {
        "–": "-", "—": "-", "•": "-", "·": "-", 
        "“": '"', "”": '"', "’": "'", "…": "..."
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text
