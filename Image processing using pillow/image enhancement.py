# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:00:40 2021

@author: Md.Abdullah
"""

from PIL import Image,ImageFilter,ImageEnhance

img=Image.open('J:\Digital-Image-Processing\Images/m.jpg')

# Filters
out=img.filter(ImageFilter.DETAIL)
print(out)
out.show()

# point operations
# multiply each pixel by 1.2
point_img=img.point( lambda x: x*2)
print(point_img)
point_img.show()

# Enchancement
contrast=ImageEnhance.Contrast(img)
contrast.enhance(1.6).show()

brightness=ImageEnhance.Brightness(img)
brightness.enhance(5).show()
