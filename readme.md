# `openeditor`
Edit files with your `$EDITOR`, like git commit does.

## Usage
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

If none of these provide a useful editor, an exception will be thrown.
