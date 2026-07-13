from pathlib import Path
from docx import Document


def extract_docx_text(file_path: str) -> str:
    """
    Extract text from a DOCX file.
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"DOCX file not found: {file_path}")

    document = Document(file_path)

    text = [paragraph.text for paragraph in document.paragraphs]

    return "\n".join(text).strip()