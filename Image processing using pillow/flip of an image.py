# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:24:35 2021

@author: Md.Abdullah
"""

from PIL import Image

# reading the image

img=Image.open('J:\Digital-Image-Processing\Images/m.jpg')
print(img.size)

# flip the image
flip_image=img.transpose(Image.FLIP_LEFT_RIGHT)
flip_image.save('J:\Digital-Image-Processing\Images/flip_img.jpg')
flip_image.show()

flip_image=img.transpose(Image.FLIP_TOP_BOTTOM)
flip_image.save('J:\Digital-Image-Processing\Images/flip_img1.jpg')
flip_image.show()