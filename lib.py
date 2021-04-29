"""Internal functions."""

import os
import subprocess


class EditorError(RuntimeError):
    """An error with editing a file with the editor."""

    pass


def edit(filepath):
    """Open the given file in an editor for the user to edit.

    :param filepath: Path to the file.
    :return: Contents of the file.
    """

    subprocess.call([editor(), filepath], close_fds=True)

    with open(filepath) as f:
        return f.read()


def editor() -> str:
    """Get system's editor."""

    # VISUAL is preferable to EDITOR on virtually all modern systems
    # See https://unix.stackexchange.com/q/4859
    editor_cmd = os.environ.get("VISUAL") or os.environ.get("EDITOR")

    if editor_cmd:
        return editor_cmd
    else:
        raise EditorError(
            "Both $VISUAL and $EDITOR are unset, could not pick "
            "an appropriate editor."
        )
