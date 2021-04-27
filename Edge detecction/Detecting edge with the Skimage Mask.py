# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:18:38 2021

@author: Md.Abdullah
"""

from PIL import Image
from skimage import filters
import scipy

img=Image.open("J:\Digital-Image-Processing\Images\m.jpg").convert("L")
img.show()

img_array=filters.sobel(img)
img_out=Image.fromarray(img_array)
img_out.show()