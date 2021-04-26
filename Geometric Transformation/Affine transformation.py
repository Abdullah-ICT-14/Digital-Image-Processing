# -*- coding: utf-8 -*-
"""
In affine transformation, all parallel lines in the original image will
still be parallel in the output image. To find the transformation matrix, 
we need three points from the input image and their corresponding locations in
the output image. Then cv.getAffineTransform will create a 2x3 matrix which is 
to be passed to cv.warpAffine.
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('J:\Digital-Image-Processing\Images\m.jpg')

rows,cols,ch=img.shape

pst1=np.float32([[50,50],[200,10],[10,400]])
pst2=np.float32([[10,100],[200,100],[100,400]])

affine_matrix=cv2.getAffineTransform(pst1,pst2)

affine_transformed_image=cv2.warpAffine(img,affine_matrix,(cols,rows))
plt.imshow(affine_transformed_image)