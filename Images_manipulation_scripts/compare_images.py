#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comparison of two almost identical images

code from here:

https://stackoverflow.com/questions/56183201/detect-and-visualize-differences-between-two-images-with-opencv-python
"""

import cv2
from skimage.metrics import structural_similarity

from pathlib import Path

import numpy as np



path_start = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/frames_geomatrix/2023-03-15_18-17-08_0133200.tif")

path_end = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/frames_geomatrix/2023-03-15_18-17-08_0999600.tif")

# Load images as grayscale
image_start = cv2.imread(str(path_start), 0)
image_end = cv2.imread(str(path_end), 0)


###
# first method
###


# Convert images to grayscale
#before_gray = cv2.cvtColor(image_start, cv2.COLOR_BGR2GRAY)
#after_gray = cv2.cvtColor(image_end, cv2.COLOR_BGR2GRAY)

before_gray = image_start
after_gray = image_end

# Compute SSIM between the two images
(score, diff) = structural_similarity(before_gray, after_gray, full=True)
print("Image Similarity: {:.4f}%".format(score * 100))

# The diff image contains the actual image differences between the two images
# and is represented as a floating point data type in the range [0,1] 
# so we must convert the array to 8-bit unsigned integers in the range
# [0,255] before we can use it with OpenCV
diff = (diff * 255).astype("uint8")
diff_box = cv2.merge([diff, diff, diff])

# Threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

mask = np.zeros(image_start.shape, dtype='uint8')
filled_after = image_end.copy()

for c in contours:
    area = cv2.contourArea(c)
    if area > 40:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image_start, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.rectangle(image_end, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.drawContours(mask, [c], 0, (255,255,255), -1)
        cv2.drawContours(filled_after, [c], 0, (0,255,0), -1)
        
cv2.imshow('before', image_start)
cv2.imshow('after', image_end)
cv2.imshow('diff', diff)
cv2.imshow('diff_box', diff_box)
cv2.imshow('mask', mask)
cv2.imshow('filled after', filled_after)
cv2.waitKey()

###
# second method
###

diff = 255 - cv2.absdiff(image_start, image_end)

#cv2.imshow('diff', diff)
#cv2.waitKey()

fileout = str(Path(path_start).parent.absolute() / Path("diff2.tif"))


isWritten = cv2.imwrite(fileout, diff)

if isWritten:
	print('Image is successfully saved as file.')
