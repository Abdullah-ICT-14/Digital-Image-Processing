# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:04:28 2021

@author: Md.Abdullah
"""

import glob
import cv2

path='J:\Digital-Image-Processing\Images\*'
for file in glob.glob(path):
    print(file)
    a=cv2.imread(file)
    print(a)
    
    cv2.imshow('color image',a)
    
    c=cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow('Gray image',c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()