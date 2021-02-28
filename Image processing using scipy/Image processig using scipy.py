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

# statistical information
mean=img.mean()
max=img.max()
min=img.min()
print('Min,Max and Mean :',min,max,mean)

# Geometrical transformation
# flip left right

from scipy import ndimage
import numpy as np

flip=np.fliplr(img)
plt.imshow(flip)

#flip up down
flipud=np.flipud(img)
plt.imshow(flipud)


# rotation
rot_img_45=ndimage.rotate(img, 45)
plt.imshow(rot_img_45)
rot_img_60=ndimage.rotate(img, 60)
plt.imshow(rot_img_60)








