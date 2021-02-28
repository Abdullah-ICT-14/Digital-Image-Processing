# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:09:44 2021

@author: Md.Abdullah
"""

from scipy import misc
import imageio

# Reading the image
img=imageio.imread('J:\Digital-Image-Processing\Images/data science.jpg')
print(img)

# Find the type of the image
print(type(img))

# Find the data types of the image
print(img.dtype)

# Find the shape of the image
print(img.shape)


# Find the individual pixel value
print(img[0,0])

# Showing the image
import matplotlib.pyplot as plt
plt.imshow(img)

# slicing the pixel value
print(img[20:30,10:18])
