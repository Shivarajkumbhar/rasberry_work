import numpy as np
import cv2 #import open cv library
from skimage import io
import os
import matplotlib.pyplot as plt
print("open cv version :",cv2.__version__)

#to import the image in our code
image = io.imread('IMG_20230911_163327.jpg')
image = io.imread('licensed-image.jpg')
plt.imshow(image)
plt.imshow(image1)

#to measure the height and width of the image
h,w = image.shape[:2]
print('width = ',w)
print('height = ',h)

h,w = image1.shape[:2]
print('width = ',w)
print('height = ',h)
