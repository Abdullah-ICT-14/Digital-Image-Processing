# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:27:45 2021

@author: Md.Abdullah
"""

from skimage import io,restoration
import matplotlib.pyplot as plt

img=io.imread('J:\Digital-Image-Processing\Images/t.jpg',as_gray=True)
# plt.imshow(img)

import numpy as np
psf=np.ones((3,3))/9

deconvolution_img,_=restoration.unsupervised_wiener(img,psf)
plt.imshow(deconvolution_img,cmap='gray')
plt.imsave('J:\Digital-Image-Processing\Images/t_deconvolution.jpg',deconvolution_img,cmap='gray')