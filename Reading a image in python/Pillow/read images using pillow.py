# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:36:21 2021

@author: Md.Abdullah
"""

from PIL import Image
import numpy as np
# Opening the image
img=Image.open('J:\Digital-Image-Processing\Images\m.jpg') 

#Print the type of image.Pillow image is not numpy array.
print(type(img))

# Showing the images
img.show()

#print the format of the image
print(img.format)


# Converting the img into numpy array using numpy asarray
img1=np.asarray(img)
print(img1)
print(type(img1))