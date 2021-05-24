# `openeditor`
Edit files with your `$EDITOR`, like git commit does.

## Usage
Install with: `pip install openeditor`

```
# Let user edit file
s = openeditor.edit_file("path/to/my/file.txt")
print("The file now contains:\n" + s)

# Use a temp file
s = openeditor.edit_file(
    "# Please edit this file, save and close editor when done", 
    "path/to/my/file.txt"
)
print("The file now contains:\n" + s) 
```

The editor is obtained from, in order of precedence:

* `$VISUAL`
* `$EDITOR`

If neither of these provide a useful editor, an exception will be thrown.

## Limitations
`openeditor` expects an editor string similar to `EDITOR=cmd` such that:

1. `cmd file.txt` (filename as the final argument) is a correct way of editing `file.txt`.
2. `cmd` is not too complex. Simple things like space-separated flags (eg. `EDITOR="vim -n"`) are fine but advanced shell magic may break.

If your `cmd` **does** need to be more complex, one possible workaround is to write a wrapper script that presents a compatible command-line interface to `openeditor` and invokes the full command as appopriate.