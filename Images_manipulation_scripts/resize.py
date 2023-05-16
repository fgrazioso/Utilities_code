#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script to resize images
"""
from pathlib import Path
from PIL import Image
import numpy as np

dirpath = Path("/media/fabio/X-Bio_Data/HED-Unet_train_test/images")

factor = 0.3


for filepath in dirpath.rglob("*.tif" ):
    
    print(filepath)

    loaded_img = Image.open(filepath)
    
    width = loaded_img.size[0]
    height = loaded_img.size[1]
    
    new_width = int(np.floor(width * factor))
    new_height = int(np.floor(height * factor))

    converted_img = loaded_img.resize((new_width,new_height), Image.Resampling.LANCZOS)

    converted_img.save(filepath)
        


