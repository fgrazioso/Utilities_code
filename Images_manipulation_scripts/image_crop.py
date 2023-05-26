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


file_path = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-15_18-17-08_frames_1_sec/2023-03-15_18-17-08_0272400.png")


image_in = cv2.imread(str(file_path), 0)

image_crop = image_in[25:1060, 180:1841]

    
plt.figure

fig, ax = plt.subplots()
plt.imshow(image_in, cmap = 'gray')
plt.title('image_start_crp')

plt.figure

fig, ax = plt.subplots()
plt.imshow(image_crop, cmap = 'gray')
plt.title('cropped')


plt.show()
