# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:09:33 2021

@author: Md.Abdullah
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Reading the image
img=mpimg.imread('J:\Digital-Image-Processing\Images\m.jpg')
print(img)

# showing the image
plt.imshow(img)

print(type(img))
print(img.shape)
plt.colorbar()