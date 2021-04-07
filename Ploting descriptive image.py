# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:50:13 2021

@author: Md.Abdullah
"""

from PIL import Image
from pylab import *

im=array(Image.open('J:\Digital-Image-Processing\Images/t.jpg'))
imshow(im)

x=[500,100,200,250]
y=[200,100,150,200]
plot(x,y,'r*')
plot(x,y,'ks:')
title("Ploting descriptive image")
show()