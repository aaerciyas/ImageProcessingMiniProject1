#!/usr/bin/python3
# -*- coding: ascii -*-
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

def FindHistogram(image, text):
	cv2.imshow("Original", image)
	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	plt.figure()
	plt.title("Grayscale Histogram")
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	plt.plot(hist)
	plt.xlim([0, 256])
	plt.savefig(text + "-histogram.png")

def ContrastStreching(image, text):
	minmax_img = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')
	 
	# Loop over the image and apply Min-Max formulae
	for i in range(image.shape[0]):
	    for j in range(image.shape[1]):
	        minmax_img[i,j] = 255*(image[i,j]-np.min(image))/(np.max(image)-np.min(image))

	eq = cv2.equalizeHist(minmax_img)

	cv2.imwrite(text+".png",eq)
	FindHistogram(eq, text)


def main():
	images = ["soru1-chest.tif", "soru1-lena.bmp", "soru1-pepper.bmp"]
	for i in images:
		image = cv2.imread(i, 0)
		imageName = i.split(".")
		FindHistogram(image, imageName[0])
		ContrastStreching(image, imageName[0]+"-final-image")

if __name__ == "__main__":
    main()	