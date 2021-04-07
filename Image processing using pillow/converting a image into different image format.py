# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:35:26 2021

@author: Md.Abdullah
"""

from PIL import Image
import os
img=["J:\Digital-Image-Processing\Images/t.jpg","J:\Digital-Image-Processing\Images/messi.jpg"]
for i in img:
    out_img=os.path.splitext(i)[0]+".png"
    if i !=out_img:
        try:
            Image.open(i).save(out_img)
        except IOError:
            print("Can't Convert",i)
    