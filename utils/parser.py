from pathlib import Path

from utils.pdf_parser import extract_pdf_text
from utils.docx_parser import extract_docx_text
from utils.txt_parser import extract_txt_text


def extract_text(file_path: str) -> str:
    """
    Automatically detects file type and extracts text.
    """

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    elif extension == ".txt":
        return extract_txt_text(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )