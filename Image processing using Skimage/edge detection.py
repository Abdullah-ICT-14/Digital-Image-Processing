# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:15:32 2021

@author: Md.Abdullah
"""
from skimage import io
import matplotlib.pyplot as plt
from skimage.filters import roberts,sobel,scharr,prewitt
img=io.imread('J:\Digital-Image-Processing\Images/test_image.jpg',as_gray=True)
plt.imshow(img)

# edge detection
edge_roberts=roberts(img)
edge_sobel=sobel(img)
edge_scharr=scharr(img)
edge_prewitt=prewitt(img)

fig,axes=plt.subplots(nrows=2,ncols=2,sharex=True,sharey=True,figsize=(8,8))
ax=axes.ravel()

#ax[0].imshow(img,cmap=plt.cm.gray)
#ax[0].set_title('Original image')

ax[0].imshow(edge_roberts,cmap=plt.cm.gray)
ax[0].set_title('Roberts edge detection')

ax[1].imshow(edge_sobel,cmap=plt.cm.gray)
ax[1].set_title('Sobel edge detection')

ax[2].imshow(edge_scharr,cmap=plt.cm.gray)
ax[2].set_title('scharr edge detection')

ax[3].imshow(edge_prewitt,cmap=plt.cm.gray)
ax[3].set_title('Prewitt edge detection')

for i in ax:
    i.axis('off')
    
plt.tight_layout()
plt.show()

