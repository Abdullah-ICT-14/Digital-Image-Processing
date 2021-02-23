# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:26:56 2021

@author: Md.Abdullah
"""

from skimage import io,img_as_float
import numpy as np
from matplotlib import pyplot as plt


#loading the image
flower_image=io.imread('Images/flower.jpg')
print(flower_image.min(),flower_image.max())
print(flower_image)

my_image=np.random.random([500,500])

#showing the image
plt.imshow(my_image)
print('Random image:',my_image)

print('Minimum value:',my_image.min(),my_image.max())

# Converting the int type image into foating point image
float_image=img_as_float(flower_image)
print(float_image)
plt.imshow(float_image)

# Multiply image with numbers
dark_image=flower_image*5
plt.imshow(dark_image)

dark_image=flower_image*0.5
plt.imshow(dark_image)

dark_image[10:100,10:100,:]=[255,0,0]
plt.imshow(dark_image)

dark_image[10:100,10:100,:]=[255,0,255]
plt.imshow(dark_image)