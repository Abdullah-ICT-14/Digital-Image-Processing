# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:43:43 2021

@author: Md.Abdullah
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("J:\Digital-Image-Processing\Images\m.jpg")
plt.imshow(img)
plt.show()

output_img=cv2.Laplacian(img,-1)
plt.imshow(output_img)
plt.show()