# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:47:07 2021

@author: Md.Abdullah
"""


# Importing pillow
from PIL import Image

# reading the image
img=Image.open('J:\Digital-Image-Processing\Images\m.jpg')
cropped_img=img.crop((0,0,250,200))
cropped_img.save('J:\Digital-Image-Processing\Images\m_crop.jpg')