from unittest.mock import mock_open, patch

from openeditor.lib import write_file


def test_empty_file_created(monkeypatch):
    fake_open = mock_open()
    with patch('openeditor.lib.open', fake_open):
        write_file('/tmp/nosuchfile.txt', contents="")
        fake_open.assert_called_once()
