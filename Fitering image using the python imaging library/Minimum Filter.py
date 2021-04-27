# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:29:35 2021

@author: Md.Abdullah
"""

from PIL import Image,ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sc


img=Image.open("J:\Digital-Image-Processing\Images\m.jpg").convert("L")

b=sc.filters.minimum_filter(img,size=5,footprint=None,output=None,mode="reflect",cval=0.0,origin=0)
img_out=Image.fromarray(b)
img_out.show()