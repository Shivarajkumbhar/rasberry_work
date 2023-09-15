import numpy as np
import cv2 #import open cv library
from skimage import io
import os
import matplotlib.pyplot as plt
print("open cv version :",cv2.__version__)

image1 = io.imread('IMG_20230911_163327.jpg')
plt.axis('off')
plt.imshow(image1)

image = io.imread('licensed-image.jpg')
plt.imshow(image)
h,w = image.shape[:2]
print('width = ',w)
print('height = ',h)

# conversion to grayscale
gray =cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap = 'gray')
