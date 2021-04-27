# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:16:34 2021

@author: Md.Abdullah
"""

from PIL import Image
from pylab import *

img=array(Image.open('J:\Digital-Image-Processing\Images\m.jpg').convert('L'))

gray()
img2=255-img

img3=(100.0/255)*img+100
img4=255.0*(img/255.0)**2

imshow(img)
imshow(img2)