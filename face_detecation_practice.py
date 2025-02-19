# -*- coding: utf-8 -*-
"""face_detecation_practice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JF09FM-fMejY2bbuPmQ3-qOpwPcvVpo9
"""

import cv2
import os

from google.colab.patches import cv2_imshow

import matplotlib.pyplot as plt

image1 = cv2.imread("/content/r1.jpg")

cv2_imshow(image1)

gray_image = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier('/content/haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray_image, 1.1,5)

cv2_imshow(gray_image)

for (x,y,w,h) in faces:
  cv2.rectangle(image1,(x,y),(x+w,y+h),(255,0,0),2)

cv2_imshow(image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

