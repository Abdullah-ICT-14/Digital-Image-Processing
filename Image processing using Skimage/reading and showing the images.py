# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:28:05 2021

@author: Md.Abdullah
"""
from skimage import io
import matplotlib.pyplot as plt

img=io.imread('J:\Digital-Image-Processing\Images/t.jpg')
plt.imshow(img)

gray_img=io.imread('J:\Digital-Image-Processing\Images/t.jpg',as_gray=True)
plt.imshow(gray_img)