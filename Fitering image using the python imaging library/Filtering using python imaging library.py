# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:29:40 2021

@author: Md.Abdullah
"""

from PIL import Image,ImageFilter
import matplotlib.pyplot as plt
from pylab import *

img=Image.open("J:\Digital-Image-Processing\Images\m.jpg")

figure(figsize=(15,15))
subplot(3,4,1)

plt.imshow(img)
plt.title("Original")

subplot(3,4,2)
img2=img.filter(ImageFilter.CONTOUR)
plt.imshow(img2)
plt.title("Contour")

subplot(3,4,3)
img3=img.filter(ImageFilter.DETAIL)
plt.imshow(img3)
plt.title("Detail")

subplot(3,4,4)
img4=img.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(img4)
plt.title("Edge Enhance")

subplot(3,4,5)
img5=img.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.imshow(img5)
plt.title("Edge Enhance More")


subplot(3,4,6)
img6=img.filter(ImageFilter.EMBOSS)
plt.imshow(img6)
plt.title("Emboss")

subplot(3,4,7)
img7=img.filter(ImageFilter.FIND_EDGES)
plt.imshow(img7)
plt.title("Find Edges")

subplot(3,4,8)
img8=img.filter(ImageFilter.SMOOTH)
plt.imshow(img8)
plt.title("Low Pass 1")

subplot(3,4,9)
img8=img.filter(ImageFilter.SMOOTH)
plt.imshow(img8)
plt.title("Low Pass 2")


subplot(3,4,10)
img10=img.filter(ImageFilter.SHARPEN)
plt.imshow(img10)
plt.title("Sharpen")


# custom kernels

size=(3,3)
kernel1=[1,1,1,1,-1,1,-1,-1,-1]
ker1=ImageFilter.Kernel(size,kernel1,scale=None,offset=0)


subplot(3,4,11)
img11=img.filter(ker1)
plt.imshow(img11)
plt.title("Custom Filter 1")


kernel2=[1,0,-1,1,0,-1,0,0,-1]
ker2=ImageFilter.Kernel(size,kernel2,scale=None,offset=0)


subplot(3,4,12)
img12=img.filter(ker2)
plt.imshow(img12)
plt.title("Custom Filter 2")

plt.show()






