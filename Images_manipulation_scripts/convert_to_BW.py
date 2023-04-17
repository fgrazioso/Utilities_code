#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script to transform a greyscale image in rigorously "black and white only"
"""

from PIL import Image

filepath = "/media/fabio/X-Bio_Data/HED-Unet_train_test/gt_copy/test.tif"


with Image.open(filepath) as loaded_img:
    loaded_img = raster.read()
    #loaded_img = loaded_img.convert('RGB')


        thr = 127
        fn = lambda x : 255 if x > thr else 0
        converted_img = loaded_img.convert('L').point(fn, mode='1')
        ###
 
