from pathlib import Path
import pymupdf


def extract_pdf_text(file_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a string.
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    text = ""

    with pymupdf.open(file_path) as document:
        for page in document:
            text += page.get_text()

    return text.strip()