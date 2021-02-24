# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:36:55 2021

@author: Md.Abdullah
"""
# pip install apeer-ometiff-library first

from apeer_ometiff_library import io
(pic,omexml)=io.read_ometiff("J:\Digital-Image-Processing\Images\test_image.ome.tif")
print(pic2.shape)