from pathlib import Path


def extract_txt_text(file_path: str) -> str:
    """
    Extract text from a TXT file.
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"TXT file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()