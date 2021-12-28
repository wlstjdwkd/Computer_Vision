import cv2

i_image = cv2.imread('jinseong.jpg', cv2.IMREAD_GRAYSCALE)

f_image = cv2.medianBlur(i_image, 5)

cv2.imshow('Original image', i_image)
cv2.imshow('Median filtered image (5x5)', f_image)

cv2.waitKey(0)