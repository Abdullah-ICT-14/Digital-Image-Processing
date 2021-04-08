# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:58:03 2021

@author: Md.Abdullah
"""

from PIL import Image
from pylab import *

img=Image.open("J:\Digital-Image-Processing\Images/m.jpg").convert("L")
img_array=array(img)
#img.show()
figure()
hist(img_array.flatten(),bins=300)
show()