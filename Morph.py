import numpy as np
import cv2

g_image = cv2.imread('jinseong.jpg',cv2.IMREAD_GRAYSCALE)

ret, b_image = cv2.threshold(g_image, 128, 255, cv2.THRESH_BINARY)

morph_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

di_image = cv2.dilate(b_image,morph_rect, iterations = 1)

er_image = cv2.erode(b_image,morph_rect,iterations = 1)

mp_image = cv2.morphologyEx(b_image,cv2.MORPH_OPEN,morph_rect, iterations = 1)

cv2.imshow('Binary image', b_image)
cv2.imshow('Diliation image',di_image)
cv2.imshow('Erosion image', er_image)
cv2.imshow('Opening image', mp_image)

cv2.waitKey(0)