from utils.history import save_json


def test_save_json(tmp_path, monkeypatch):
    from utils import history

    monkeypatch.setattr(history, "OUTPUT_DIR", tmp_path)

    history.save_json("{}")

    files = list(tmp_path.iterdir())

    assert len(files) == 1
    assert files[0].suffix == ".json"