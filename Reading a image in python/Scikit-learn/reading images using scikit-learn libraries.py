# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:24:30 2021

@author: Md.Abdullah
"""

from skimage import io,img_as_float,img_as_ubyte

# Reading the image
img=io.imread('J:\Digital-Image-Processing\Images\m.jpg')
print(img)

# showing the image
io.imshow(img)

print(type(img))
print(img.shape)

# Convert the image into float type image
img_float=img_as_float(img)
print(type(img_float))
print(img_float)

# Convert the image into unsigned integer type image
img_ubyte=img_as_ubyte(img)
print(type(img_ubyte))
print(img_ubyte)