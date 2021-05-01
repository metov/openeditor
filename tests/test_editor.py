from openeditor import lib
import pytest

MOCK_VISUAL = "some_visual"
MOCK_EDITOR = "some_editor"


@pytest.fixture
def mock_set_visual(monkeypatch):
    monkeypatch.setenv("VISUAL", MOCK_VISUAL)


@pytest.fixture
def mock_unset_visual(monkeypatch):
    try:
        monkeypatch.delenv("VISUAL")
    except KeyError:
        pass


@pytest.fixture
def mock_set_editor(monkeypatch):
    monkeypatch.setenv("EDITOR", MOCK_EDITOR)


@pytest.fixture
def mock_unset_editor(monkeypatch):
    try:
        monkeypatch.delenv("EDITOR")
    except KeyError:
        pass


def test_both_set(mock_set_visual, mock_set_editor):
    assert lib.editor() == MOCK_VISUAL


def test_visual_only(mock_set_visual, mock_unset_editor):
    assert lib.editor() == MOCK_VISUAL


def test_editor_only(mock_unset_visual, mock_set_editor):
    assert lib.editor() == MOCK_EDITOR


def test_neither_set_raises_EditorError(mock_unset_visual, mock_unset_editor):
    pytest.raises(lib.EditorError, lib.editor)
