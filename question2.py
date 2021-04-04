#!/usr/bin/python3
# -*- coding: ascii -*-
from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

image = cv2.imread("soru2-fingerprint.tif")

kernel = np.ones((5,5),np.float32)/35
dst = cv2.filter2D(image,-1,kernel,borderType=cv2.BORDER_CONSTANT)

cv2.imshow("linearfilter", dst)
blurred1 = cv2.medianBlur(image, 3)
blurred2 = cv2.medianBlur(image, 5)
blurred3 = cv2.medianBlur(image, 7)
cv2.imwrite("soru2-linearfiler.png",dst)
cv2.imwrite("soru2-blurredWith3.png",blurred1)
cv2.imwrite("soru2-blurredWith5.png",blurred2)
cv2.imwrite("soru2-blurredWith7.png",blurred3)

