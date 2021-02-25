# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:22:04 2021

@author: Md.Abdullah
"""

from PIL import Image

# reading the image

img=Image.open('J:\Digital-Image-Processing\Images/flower.jpg')
img.show()
print(img.size)

# color transforming
gray_image=img.convert("L")
gray_image.show()
gray_image.save('J:\Digital-Image-Processing\Images/gray_flower.jpg')