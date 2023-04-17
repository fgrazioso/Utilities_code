#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script with a collection of image manipulation functions
"""


from pathlib import Path
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import os
import glob



inputDir = "/home/fabio/Dropbox/Leaves_wet_paper/figs/leaves_imgs/untitled folder"

for index, file_path in enumerate(glob.iglob(
                            os.path.join(inputDir, "*.png"))):
                            #os.path.join(inputDir, "Лист огурца 9-10 о1 старый_09533.png"))):

    f = file_path


    og_image = Image.open(f)


    og_image.crop((143, 58, 513, 428)).save(f)
    
    

    
    #(left, upper, right, lower)
    #(308, 59, 2154, 1540) this cuts the "real" image
    #(491, 60, 1971, 1540) 
    #(489, 59, 1971, 1541)
