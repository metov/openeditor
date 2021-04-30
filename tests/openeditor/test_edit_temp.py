import tempfile
from pathlib import Path

import openeditor


class MockDir:
    name = "/fake/temp/dir"


class MockWrite:
    def record(self, path, contents):
        self.path = path


def test_default_name_on_empty_name(monkeypatch):
    monkeypatch.setattr(tempfile, "TemporaryDirectory", MockDir)
    fake_write = MockWrite()
    monkeypatch.setattr(openeditor, "write_file", fake_write.record)
    monkeypatch.setattr(openeditor, "edit", lambda fn: None)

    openeditor.edit_temp(name="")
    exp = str(Path(MockDir.name) / openeditor.DEFAULT_TEMPFILE)
    assert exp == str(fake_write.path)
