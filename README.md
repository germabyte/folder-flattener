### README

The provided script is designed to simplify the process of copying files from one folder to another, especially when dealing with a large number of files scattered across various subdirectories. Its primary purpose is to flatten the directory structure during the copying process, ensuring that all files end up in a single target directory without maintaining the original folder hierarchy. Here's a brief overview of its functionality and usage:

#### Purpose
This script automates the process of copying all files from a selected source folder, including its subdirectories, into a single target folder. It flattens the directory structure, meaning that it does not recreate the subdirectories in the target folder. If there are files with duplicate names, it appends a unique number to the filename to prevent overwriting.

#### How to Use
1. Run the script.
2. A dialog box will prompt you to select the source folder from which the files will be copied.
3. After selecting the source, another dialog box will prompt you to select the target folder where the files will be copied.
4. The script then copies all files from the source folder and its subdirectories into the target folder. If a file with the same name exists, it appends a number to its name.
5. Upon successful completion, a message box will notify you that the files have been copied successfully.

#### Requirements
- Python environment with os, shutil, and tkinter libraries.
- A graphical user interface (GUI) environment for the dialog boxes to appear.

This script is particularly useful for consolidating files from various locations into a single, manageable location, such as when organizing photos, documents, or project files.
