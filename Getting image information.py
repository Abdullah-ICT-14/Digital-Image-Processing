# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:38:34 2021

@author: Md.Abdullah
"""

import numpy as np
import matplotlib.pyplot as plt

x=plt.imread("J:\Digital-Image-Processing\Images/t.jpg")
print(x)
print(np.shape(x))
print(type(x))
print(x.dtype)
plt.imshow(x)
plt.show()