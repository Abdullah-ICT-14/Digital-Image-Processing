# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:25:17 2021

@author: Md.Abdullah
"""

from PIL import Image

img =Image.open('J:\Digital-Image-Processing\Images/t.jpg')
img.show()

# resize
resize_img=img.resize([200,250])
resize_img.show()

#Cropped Image
xrop=(10,10,100,100)
crop_img=img.crop(xrop)
crop_img.show()

# rotate
rot_img=img.rotate(45)
rot_img.show()