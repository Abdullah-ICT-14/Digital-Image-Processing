# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:02:43 2021

@author: Md.Abdullah
"""

import cv2
from skimage import img_as_ubyte,img_as_int
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np

messi=cv2.imread('J:\Digital-Image-Processing\Images\m.jpg',0)
plt.imshow(messi)
plt.show()
img=img_as_int(messi)

prewitt_vertical=np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype='float64')
prewitt_vertical_out=img_as_ubyte(ndimage.convolve(img,prewitt_vertical,mode='constant',cval=0.0))

plt.imshow(prewitt_vertical_out,cmap='gray')
plt.show()