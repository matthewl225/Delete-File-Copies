# Delete-File-Copies
Sends copies of files in user specified folder to Recycling Bin. Deletes them by checking the filename with the Windows naming convention for file copies. Copies usually have a "(number)" or " - Copy" appended to their original filenames--this program, through the use of regular expressions, checks for either one of these.

All deleted files can be restored from Recycling Bin.

Source Python scripts can be found in the SOURCE PYTHON SCRIPTS folder.

Executable made from using cx_freeze. 

To run the program, simply run the .exe file. Or, run the deletecopies.py through python shell with send2trash, os, and re packages already installed.
