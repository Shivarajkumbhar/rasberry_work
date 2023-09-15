import numpy as np
import cv2 #import open cv library
from skimage import io
import os
import matplotlib.pyplot as plt
print("open cv version :",cv2.__version__)

# read the image
image = io.imread('Cristiano_Ronaldo.jpg')
plt.axis('off')
plt.imshow(image)

# face detection model : HAAR cascade
face = cv2.CascadeClassifier(cv2.samples.findFile
 (cv2.data.haarcascades+'haarcascade_frontalface_default.xml'))

# Apply face detection model on photo
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
FaceDetect = face.detectMultiScale(gray)

# to draw rectangle arround the face
for(x,y,w,h) in FaceDetect:
  image = cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 3)
  plt.imshow(image)
  
