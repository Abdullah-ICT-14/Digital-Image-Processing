# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:18:56 2021

@author: Md.Abdullah
"""

import czifile

# reading the image
img=czifile.imread('J:\Digital-Image-Processing\Images\czi_image.czi')
print(img.shape)
print(img)