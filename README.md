# `openeditor`
Edit files with your `$EDITOR`, like git commit does.

## Usage
```
# Let user edit file
s = openeditor.edit_file("path/to/my/file.txt")
print("The file now contains:\n" + s)

# Use a temp file
s = openeditor.edit_file("path/to/my/file.txt")
print("The file now contains:\n" + s) 
```

`openeditor.edit_file("path/to/my/file.txt")` to let user edit `path/to/my/file.txt` in the configured editor and return 