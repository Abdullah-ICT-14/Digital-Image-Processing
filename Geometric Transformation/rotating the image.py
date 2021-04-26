# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:56:25 2021

@author: Md.Abdullah
"""
"""
To find this transformation matrix, OpenCV provides a function, 
cv2.getRotationMatrix2D.
"""

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('J:\Digital-Image-Processing\Images\m.jpg')

rows,cols,ch=img.shape

rotated_matrix=cv2.getRotationMatrix2D((cols/2,rows/2), 90, 1)
rotated_image=cv2.warpAffine(img,rotated_matrix,(cols,rows))
plt.imshow(rotated_image)
