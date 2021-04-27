# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:32:59 2021

@author: Md.Abdullah
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('J:\Digital-Image-Processing\Images\m.jpg')
plt.imshow(img)
plt.show()

sobel_x= cv2.Sobel(img,-1,1,0,ksize=5)
sobel_y=cv2.Sobel(img,-1,0,1,ksize=5)

plt.imshow(sobel_x,cmap='gray')
plt.show()