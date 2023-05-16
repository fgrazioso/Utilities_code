#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script to transform a greyscale image in rigorously "black and white only"
"""
from pathlib import Path
from PIL import Image

dirpath = Path("/media/fabio/X-Bio_Data/HED-UNet_train/gt")

thr = 127
fn = lambda x : 255 if x > thr else 0


for filepath in dirpath.rglob( "*.png" ):

    loaded_img = Image.open(filepath)

    converted_img = loaded_img.convert('L').point(fn, mode='1')

    converted_img.save(filepath)
        

###
#for x in range(H):
    #for y in range(W):
        #if data[x][y] > 127:
            #data[x][y] = 255
        #else: data[x][y] = 0
