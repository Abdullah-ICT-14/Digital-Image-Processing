# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:19:49 2021

@author: Md.Abdullah
"""


from PIL import Image,ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sc

img=Image.open("J:\Digital-Image-Processing\Images\m.jpg").convert("L")

k=np.ones((5,5))/25
b=sc.filters.convolve(img,k)

img_out=Image.fromarray(b)
img_out.save("J:\Digital-Image-Processing\Images\mean.jpg")
