import cv2
from matplotlib import pyplot as plt

g_image = cv2.imread('jinseong.jpg',cv2.IMREAD_GRAYSCALE)

# stretching
n_image = cv2.normalize(g_image, None, 0, 255, cv2.NORM_MINMAX)

g_hist = cv2.calcHist([g_image], [0], None, [256], [0, 256])
n_hist = cv2.calcHist([n_image], [0], None, [256], [0, 256])

plt.title('Histogram')
plt.plot(g_hist, color='gray')
plt.plot(n_hist, color='blue')

cv2.imshow('Gray image', g_image)
cv2.imshow('Stretch image', n_image)
plt.show()

cv2.waitKey(0)