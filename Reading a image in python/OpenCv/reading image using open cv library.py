# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 21:07:20 2021

@author: Md.Abdullah
"""

import cv2

# reading a image
gray_image=cv2.imread('J:\Digital-Image-Processing\Images\m.jpg',0)
img=cv2.imread('J:\Digital-Image-Processing\Images\m.jpg',1)

# Visualizing image
cv2.imshow('Color-image',img)
cv2.imshow('Gray-image',gray_image)

# Need to initialize in every open_cv program
cv2.waitKey(0)
cv2.destroyAllWindows()