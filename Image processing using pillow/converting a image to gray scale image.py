# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:19:18 2021

@author: Md.Abdullah
"""

from PIL import Image

img=Image.open("J:\Digital-Image-Processing\Images\messi.jpg")
#img.show()
new_img=Image.open("J:\Digital-Image-Processing\Images\messi.jpg").convert("L")
new_img.show()