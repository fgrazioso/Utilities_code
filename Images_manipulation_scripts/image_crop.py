#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script with a collection of image manipulation functions
"""


from pathlib import Path

import cv2

import numpy as np
import matplotlib.pyplot as plt
import os




file_path = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-15_18-57-49_frames/2023-03-15_18-57-49_011000.png")



image_in = cv2.imread(str(file_path))



image_crop = image_in[44:1077, 200:1854]



    
plt.figure

fig, ax = plt.subplots()
plt.imshow(image_in)
plt.title('image_start_crp')

plt.figure

fig, ax = plt.subplots()
plt.imshow(image_crop)
plt.title('cropped')



    
plt.show()
