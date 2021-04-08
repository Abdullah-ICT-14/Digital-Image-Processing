# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:14:53 2021

@author: Md.Abdullah
"""
import cv2
import numpy as np
from PIL import Image
img=cv2.imread('J:\Digital-Image-Processing\Images/m.jpg',0)

equ=cv2.equalizeHist(img)

result=np.hstack((img,equ)) #tacking images side-by-side

cv2.imwrite('J:\Digital-Image-Processing\Images/result.png',result)