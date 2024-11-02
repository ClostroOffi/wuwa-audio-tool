# Wuthering Waves audio tool
This Python script automates the process of copying and renaming `.wem` audio files based on references found in `.txtp` files. Each `.txtp` file contains a reference to a `.wem` file in the first line. 
The script reads this reference, copies the corresponding `.wem` file from a specified source directory, and renames it using the name of the `.txtp` file (without the extension). 
The renamed `.wem` file is then saved in a designated target folder.

## Features

- Reads `.txtp` files from a source directory.
- Extracts the referenced `.wem` file name from the first line of each `.txtp` file.
- Copies the corresponding `.wem` file from a source directory to a destination directory.
- Renames each copied `.wem` file to match the `.txtp` file name.

## Requirements

- Python 3.x
- `shutil` and `os` libraries (these are included in Python's standard library).

## Generating .txtp Files

To generate `.txtp` files, you can use [WWISER](https://github.com/bnnm/wwiser/), a tool that parses `.bnk` files from Wwise projects and creates `.txtp` files.
Follow the WWISER documentation for more details on installation and usage.
