# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:41:37 2021

@author: Md.Abdullah
"""
"""
Scaling is just resizing of the image.
OpenCV comes with a function of cv2.resize() for this purpose.
The size of the image can be specified manually, 
or you can specify the scaling factor
"""



import cv2
import matplotlib.pyplot as plt

img=cv2.imread('J:\Digital-Image-Processing\Images\m.jpg')
plt.imshow(img)
plt.title("Original Image")
resized_image=cv2.resize(img,(300,300))
plt.imshow(resized_image)
plt.title('Resized Image')
print("Size of an orginal image",img.shape)
print("Size of the resized image",resized_image.shape)
