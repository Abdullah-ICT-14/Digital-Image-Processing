# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:01:15 2021

@author: Md.Abdullah
"""

from skimage import io
import matplotlib.pyplot as plt
from skimage.feature import canny
img=io.imread('J:\Digital-Image-Processing\Images/t.jpg',as_gray=True)
plt.imshow(img)

# Canny edge detection
edge_canny=canny(img,sigma=3)
plt.imshow(edge_canny)

edge_canny=canny(img,sigma=7)
plt.imshow(edge_canny)

edge_canny=canny(img,sigma=1)
plt.imshow(edge_canny)