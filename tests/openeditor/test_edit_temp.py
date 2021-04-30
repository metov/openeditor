import tempfile
from pathlib import Path
from unittest.mock import mock_open

import openeditor


class MockDir:
    name = "/fake/temp/dir"


class Recorder:
    """A class for recording calls."""

    last_arg = None

    def record(self, arg):
        self.last_arg = arg


def test_default_name_on_empty_name(monkeypatch):
    # Don't actually create a temp dir
    monkeypatch.setattr(tempfile, "TemporaryDirectory", MockDir)
    mock_open()
    fake_edit = Recorder()
    monkeypatch.setattr(openeditor, "edit", fake_edit.record)

    openeditor.edit_temp(name="")
    exp_args = str(Path(MockDir.name) / openeditor.DEFAULT_TEMPFILE)
    obs_args = str(fake_edit.last_arg)
    assert exp_args == obs_args
