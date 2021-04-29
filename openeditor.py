"""Public methods for library users."""

import tempfile
from pathlib import Path

from lib import edit


def edit_file(filepath):
    """
    Open an existing file in the system's default editor for the user to edit.
    The saved contents of the file will be returned when the editor is closed.

    :param filepath: Can be absolute or relative (including just a file name).
    :return: Contents of the file when the editor is closed.
    """

    return edit(filepath)


def edit_temp(contents="", name=""):
    """
    Create a temporary file and open it in the system's default editor for the
    user to edit. The saved contents of the file will be returned when the
    editor is closed.

    :param contents: Pre-fill the file with the given text.
    :param name: Ensure that the temp filename has the given name.
    :return: Contents of the file when the editor is closed.
    """

    # Create a temp file with requested name, if any
    td = tempfile.TemporaryDirectory()
    tfpath = Path(td.name) / name or "tempfile"

    # Populate contents if needed
    if contents:
        with tfpath.open("w") as f:
            f.write(contents)

    # Edit interactively
    return edit(tfpath)
