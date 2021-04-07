# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:04:09 2021

@author: Md.Abdullah
"""


from PIL import Image
from pylab import *
im=array(Image.open('J:\Digital-Image-Processing\Images/t.jpg'))
imshow(im)

# select 4 points
pt=ginput(4)
print('You selected',pt)
show()