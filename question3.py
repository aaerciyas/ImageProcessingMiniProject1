#!/usr/bin/python3
# -*- coding: ascii -*-
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

image = cv2.imread("soru3-ocr.tif")

for i in range(80, 121, 20):
	for j in range(2,5,1):
		avarage = cv2.blur(image, (j, j))
		(T, thresh) = cv2.threshold(avarage, i, 255, cv2.THRESH_BINARY)
		cv2.imwrite("blur"+str(j)+"-avarage-"+str(i)+".png",thresh)
