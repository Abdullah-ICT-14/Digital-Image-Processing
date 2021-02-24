# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:22:26 2021

@author: Md.Abdullah
"""

# Importing pillow
from PIL import Image

# reading the image
img=Image.open('J:\Digital-Image-Processing\Images\m.jpg')

# Find the size of the image
print('Size:',img.size)

# Find the type of the image
print(type(img))

# Find the format of the image
print(img.format)

# Find the mode of the image
print(img.mode)


# Resizing the image without aspect ratio.
resize_image=img.resize((200,300))

# Saving the resize image
resize_image.save('J:\Digital-Image-Processing\Images\m_resize.jpg')

# reading the resize image
img_resize=Image.open('J:\Digital-Image-Processing\Images\m_resize.jpg')

# Find the size of the resize image
print('Size:',img_resize.size)

# Find the type of the resize image
print(type(img_resize))

# Find the format of the resize image
print(img_resize.format)

# Find the mode of the resize image
print(img_resize.mode)

# Resizing the image by keeping the aspect ratio.
img.thumbnail((200,300))
img.save('J:\Digital-Image-Processing\Images\m_thumbnail.jpg')
print('Size:',img.size)

# thumbnail not working when the image size is lower than the thumbnail size.
img.thumbnail((1200,1300))
img.save('J:\Digital-Image-Processing\Images\m_thumbnail.jpg')
print('Size:',img.size)


# But resize will take the value whatever we provide.
resize_img=img.resize((1200,1300))
resize_img.save('J:\Digital-Image-Processing\Images\m_resize_2.jpg')

