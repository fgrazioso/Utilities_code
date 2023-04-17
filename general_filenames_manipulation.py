#!/usr/bin/env python
"""
Script to find and replace strings in the filenames of a folder
"""

#import glob, os
from pathlib import Path
import tkinter as tk

from tkinter import filedialog

import re





					
def search_rename(file_path):
        
    filename = file_path.stem
    filextension = file_path.suffix
    
    parentpath = file_path.parent
    
    
    pattern = "Buddha Bar Summer Of Chill - "
    
    replacement = ""

    
    newfilename = re.sub(pattern, replacement, filename)
    
    
    newfile_path = file_path.with_name(newfilename)
    
    
    file_path.rename(newfile_path)
    


	


###					
# main
###


root = tk.Tk()
root.withdraw()

print("\n\n*** choose folder to process ***\n\n")

folder_path = Path(filedialog.askdirectory())

for file_path in folder_path.rglob("*.*"):

    search_rename(file_path)

