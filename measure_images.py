#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple script to check the size (and possible other features) of all the images in a folder

"""

from pathlib import Path
from PIL import Image

dirpath = Path("/media/fabio/X-Bio_Data/HED-UNet_train_Apr_2023/gt")



for filepath in dirpath.rglob( "*.tif" ):

    loaded_img = Image.open(filepath)
    
    
    width = loaded_img.size[0]
    height = loaded_img.size[1]    
    
    
    # print("file = {}, dimensions = {} x {}".format(filepath.stem, width, height))
    
    #print("dimensions = {} x {}".format(width, height))
    
    
    if width != 1482 or height != 1482:
        print("**** difference! **** - file {}".format(filepath.stem))
    
    
