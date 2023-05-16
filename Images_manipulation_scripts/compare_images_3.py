#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comparison of two almost identical images

code from here:

https://stackoverflow.com/questions/56183201/detect-and-visualize-differences-between-two-images-with-opencv-python
"""

import cv2

from pathlib import Path


path_start = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/frames_geomatrix/2023-03-15_18-17-08_0133200.tif")

path_end = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/frames_geomatrix/2023-03-15_18-17-08_0999600.tif")



###
# second method
###

# Load images as grayscale
image1 = cv2.imread(str(path_start), 0)
image2 = cv2.imread(str(path_end), 0)

image1_crp = image1[21:1063, 181:1836]

image2_crp = image2[21:1063, 181:1836]

# Calculate the per-element absolute difference between 
# two arrays or between an array and a scalar
diff = 255 - cv2.absdiff(image2_crp, image1_crp)
diff2 = cv2.absdiff(image2_crp, image1_crp)

cv2.imshow('diff', diff)
cv2.imshow('diff2', diff2)

cv2.waitKey()
