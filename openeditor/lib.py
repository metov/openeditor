"""Internal functions."""

import os
import subprocess
import shlex


class EditorError(RuntimeError):
    """An error with editing a file with the editor."""

    pass


def edit(filepath):
    """Open the given file in an editor for the user to edit.

    Assumptions:
    1. The editor command is not too complex for shlex to handle.
    2. The path of the file to be edited is the final argument.

    :param filepath: Path to the file.
    :return: Contents of the file."""

    parts = shlex.split(editor(), posix=True) + [filepath]
    subprocess.call(parts, close_fds=True)

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


def write_file(path, contents=""):
    """Create a file. If contents are given, they will be written to it."""
    with open(path, 'w') as f:
        if contents:
            f.write(contents)
