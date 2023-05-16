#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to select and change areas of images based on color range
"""


import cv2

import matplotlib.pyplot as plt

from matplotlib.colors import hsv_to_rgb

import numpy as np


image_path = "/media/fabio/Data_X-Bio/X-Bio_documents/Microchannel_propagation_experiment/2022-04-29_30_03-05_good_data/2022-05-04_OP10_4_CMC_80_mb/ready_images/2022-05-04_13-56-27_053867.png"


image = cv2.imread(image_path)

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# create a mask for the "dark-blue edge only"
low_edge = (75, 0, 0)
up_edge = (190, 255, 255)

mask = cv2.inRange(hsv_image, low_edge, up_edge)

# obtain a "masked result" (result1) for the "dark-blue edge only"
rgb_masked_result1 = cv2.bitwise_and(rgb_image, rgb_image, mask=mask)


# obtain a "brightened result" (result2) changing brightness and contrast
rgb_masked_result2 = cv2.convertScaleAbs(rgb_masked_result1, alpha=0, beta=200)
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
