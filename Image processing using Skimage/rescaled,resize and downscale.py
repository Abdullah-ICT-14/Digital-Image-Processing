# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:37:13 2021

@author: Md.Abdullah
"""

from skimage import io
import matplotlib.pyplot as plt

img=io.imread('J:\Digital-Image-Processing\Images/test_image.jpg')
plt.imshow(img)

from skimage.transform import rescale,resize,downscale_local_mean

# rescaling
rescaled_img=rescale(img, 1/4,anti_aliasing=True) 

# resize
resize_img=resize(img, (200,200))
plt.imshow(resize_img)

#downscaling
down_scale_img=downscale_local_mean(img, (4,3))