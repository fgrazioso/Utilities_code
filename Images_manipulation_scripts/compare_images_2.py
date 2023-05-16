#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comparison of two almost identical images.

Second version, with preprocessing (contrast tweaking) and threshold
"""

import cv2


from pathlib import Path

import numpy as np



path_start = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/frames_geomatrix/2023-03-15_18-17-08_0133200.tif")

path_end = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/frames_geomatrix/2023-03-15_18-17-08_0999600.tif")

# Load images as grayscale
image_start = cv2.imread(str(path_start), 0)
image_end = cv2.imread(str(path_end), 0)



image_start_crp = image_start[21:1063, 181:1836]

image_end_crp = image_end[21:1063, 181:1836]


#cv2.convertScaleAbs(image_start, alpha=255/image_start.max())

alphaval = 1
betaval = 250

modif = cv2.convertScaleAbs(image_start_crp, alpha=alphaval)#, beta=betaval)#, beta=betaval, alpha=alphaval)
modif2 = cv2.convertScaleAbs(image_end_crp, alpha=alphaval)
# [alpha [0 , 3]) and contrast (beta [-250 , +250]) ]

blurred = cv2.GaussianBlur(modif, (7, 7), 0)
blurred2 = cv2.GaussianBlur(modif2, (7, 7), 0)

(T, thresh) = cv2.threshold(blurred, 200, 255,
	cv2.THRESH_BINARY)

(T, thresh2) = cv2.threshold(blurred2, 200, 255,
	cv2.THRESH_BINARY)



#cv2.imshow("image_start", image_start)
cv2.imshow("image_start_crp", image_start_crp)
cv2.imshow("image_end_crp", image_end_crp)
#cv2.imshow("modif", modif)
#cv2.imshow("blurred", blurred)
cv2.imshow("thresh", thresh)

cv2.imshow("thresh2", thresh2)






cv2.waitKey()
