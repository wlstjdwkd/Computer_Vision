import numpy as np
import cv2

c_image=cv2.imread('coins.bmp', cv2.IMREAD_UNCHANGED)
g_image = cv2.cvtColor(c_image, cv2.COLOR_BGR2GRAY)

morph_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))

er_image = cv2.erode(g_image,morph_rect,iterations = 1)

ret, zz_image = cv2.threshold(er_image, 127, 255, cv2.THRESH_BINARY_INV)

l_image = np.zeros_like(c_image)

cnt,labels = cv2.connectedComponents(zz_image, connectivity=8)

print("Total objects = {}".format(cnt-1))

for i in range(cnt):
    l_image[labels==i] = [int(j) for j in np.random.randint(0,255,3)]
