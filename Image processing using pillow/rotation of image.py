# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:10:42 2021

@author: Md.Abdullah
"""

from PIL import Image

# reading the image
img=Image.open('J:\Digital-Image-Processing\Images\m.jpg')
print(img.size)

rotate_img_90=img.rotate(90)
print(rotate_img_90)
rotate_img_90.save('J:\Digital-Image-Processing\Images/rotate_90.jpg')
rotate_img_90.show()

rotate_img_140=img.rotate(140)
print(rotate_img_140)
rotate_img_140.save('J:\Digital-Image-Processing\Images/rotate_140.jpg')
rotate_img_140.show()