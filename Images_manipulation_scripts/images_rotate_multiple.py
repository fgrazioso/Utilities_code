#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script with a collection of image manipulation functions
crop and rotations
"""


from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import glob



inputDir = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Leaves_wetting/Листья Огурец Растекание/NN_leaves_train_January_all/masks")

for  file_path in inputDir.rglob( "*.png" ):

    filename = file_path.stem
    parent_path = file_path.parent

    #print(filename)

    og_image = Image.open(file_path)


    angle = 90
    out_img = og_image.rotate(angle)
    out_name = filename + "_rot" + str(angle) + ".png"
    out_img.save(Path(parent_path/out_name))

    
    angle = 180
    out_img = og_image.rotate(angle)
    out_name = filename + "_rot" + str(angle) + ".png"
    out_img.save(Path(parent_path/out_name))


    angle = 270
    out_img = og_image.rotate(angle)
    out_name = filename + "_rot" + str(angle) + ".png"
    out_img.save(Path(parent_path/out_name))



    flip_img = og_image.transpose(Image.FLIP_LEFT_RIGHT)
    out_name = filename + "_flip_hor.png"
    flip_img.save(Path(parent_path/out_name))


    flip_img = og_image.transpose(Image.FLIP_TOP_BOTTOM)
    out_name = filename + "_flip_ver.png"
    flip_img.save(Path(parent_path/out_name))


