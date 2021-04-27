# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 22:55:19 2021

@author: Md.Abdullah
"""

import math,numpy 
import scipy.misc
from PIL import Image

img=Image.open('J:\Digital-Image-Processing\Images\m.jpg')
b=numpy.asarray(img)

gamma=0.5

b1=b.astype(float)
b3=numpy.max(b1)

b2=b1/b3

b3=numpy.log(b2)*gamma
c=numpy.exp(b3)*255.0

c1=c.astype(int)
d=Image.fromarray(c1)
d.show()