import cv2

i_image = cv2.imread('jinseong.jpg', cv2.IMREAD_GRAYSCALE)

f_image = cv2.GaussianBlur(i_image, (7,7),0)

cv2.imshow('Original image', i_image)
cv2.imshow('High filtered image (7x7, 0)', i_image-f_image)

cv2.waitKey(0)