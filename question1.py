#!/usr/bin/python3
# -*- coding: ascii -*-
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

image1 = cv2.imread("soru1-chest.tif",0)

image2 = cv2.imread("soru1-lena.tif")

image3 = cv2.imread("soru1-pepper.tif")

cv2.imshow("Original", image1)
hist = cv2.calcHist([image1], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.savefig("soru1-chest-histogram.png")
#plt.show()

minmax_img = np.zeros((image1.shape[0],image1.shape[1]),dtype = 'uint8')
 
# Loop over the image and apply Min-Max formulae
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        minmax_img[i,j] = 255*(image1[i,j]-np.min(image1))/(np.max(image1)-np.min(image1))

#cv2.imshow('Minmax',minmax_img)
eq = cv2.equalizeHist(image1)
#cv2.imshow("Histogram Equalization", eq)

cv2.imwrite("soru1-chest-final-image.tif",eq)
hist = cv2.calcHist([image1], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.savefig("soru1-chest-final-image-histogram.png")
#plt.show()

