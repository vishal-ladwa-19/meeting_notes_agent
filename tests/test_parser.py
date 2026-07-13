from pathlib import Path

from utils.txt_parser import extract_txt_text


def test_txt_parser(tmp_path):

    file = tmp_path / "sample.txt"

    file.write_text("Hello Meeting")

    result = extract_txt_text(str(file))

    assert result == "Hello Meeting"