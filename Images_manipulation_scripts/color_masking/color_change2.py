#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to select and change areas of images based on color range
"""


import cv2

import matplotlib.pyplot as plt

from matplotlib.colors import hsv_to_rgb

import numpy as np

import sys


image_path = "/media/fabio/Data_X-Bio/X-Bio_documents/Microchannel_propagation_experiment/2022-04-29_water_80_mb/2022-04-29_20-41-43_frames/2022-04-29_20-41-43_014933.png"


image = cv2.imread(image_path)

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# create a mask for the "orange oil"
low_edge = (0, 50, 50)
up_edge = (24, 255, 255)
mask1 = cv2.inRange(hsv_image, low_edge, up_edge)


# create a second mask because red has two parts in the hue range
low_edge = np.array([170, 50, 50])
up_edge = np.array([180,255,255])
mask2 = cv2.inRange(hsv_image,low_edge,up_edge)

mask = mask1 + mask2

# obtain a "masked result" (result1) for the "orange oil only"
rgb_masked_result1 = cv2.bitwise_and(rgb_image, rgb_image, mask=mask)
#plt.imshow(rgb_masked_result1)
#plt.show()

#sys.exit()

# obtain a "brightened result" (result2) changing brightness and contrast
rgb_masked_result2 = cv2.convertScaleAbs(rgb_masked_result1, alpha=0.3, beta=-10)
# this changes the brightness (alpha [1.0-3.0]) and contrast (beta [0-100]) 


# create an inverted mask, for the "original image minus the "dark-blue edge "
inverse_mask = cv2.bitwise_not(mask)
rgb_inverse_result = cv2.bitwise_and(rgb_image, rgb_image, mask=inverse_mask)


# create a masked version of the brightened result
rgb_masked_result3 = cv2.bitwise_and(rgb_masked_result2, rgb_masked_result2, mask=mask)


# merge the inverted masked original image with the 
rgb_finalresult = cv2.addWeighted(rgb_inverse_result,1,rgb_masked_result3,1,0)




plt.imshow(rgb_finalresult)
plt.show()


# cv2.inRange()
