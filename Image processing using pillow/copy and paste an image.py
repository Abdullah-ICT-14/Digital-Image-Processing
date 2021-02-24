# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:47:01 2021

@author: Md.Abdullah
"""

# Importing pillow
from PIL import Image

# reading the image
img1=Image.open('J:\Digital-Image-Processing\Images\m.jpg')
print(img1.size)

img2=Image.open('J:\Digital-Image-Processing\Images\m2.jpg')
print(img2.size)

img2.thumbnail((150,200))
img1_copy=img1.copy()
img1_copy.paste(img2,(50,50))
img1_copy.save('J:\Digital-Image-Processing\Images\pasted_image.jpg')