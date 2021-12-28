import numpy as np
import cv2

g_image = cv2.imread('jinseong.jpg',cv2.IMREAD_GRAYSCALE)

#ret, b_image = cv2.threshold(g_image, 128, 255, cv2.THRESH_BINARY)

morph_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

di_image = cv2.dilate(g_image,morph_rect, iterations = 1)

er_image = cv2.erode(g_image,morph_rect,iterations = 1)

mp_image = cv2.morphologyEx(g_image,cv2.MORPH_OPEN,morph_rect, iterations = 1)

cv2.imshow('Gray image', g_image)
cv2.imshow('Diliation image',di_image)
cv2.imshow('Erosion image', er_image)
cv2.imshow('Opening image', mp_image)

cv2.waitKey(0)