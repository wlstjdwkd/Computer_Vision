import numpy as np
import cv2

c_image = cv2.imread('jinseong.jpg', cv2.IMREAD_UNCHANGED)
(hit, wth) = c_image.shape[0:2]

marker = np.zeros((hit,wth), np.int32)
marker_id = 1
colors = []

w_image = c_image.copy()

def onMouse(event, x, y, flafs, param):
    global marker
    global marker_id
    global w_image

    if event == cv2.EVENT_LBUTTONDOWN:
        marker[y, x] = marker_id
        colors.append((marker_id,c_image[y,x]))
        cv2.circle(w_image, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('Image', w_image)
        marker_id = marker_id + 1

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.watershed(c_image, marker)
        w_image[marker == -1] = (0, 0, 255)
        for m_id, color in colors:
            w_image[marker == m_id] = color
        cv2.imshow('Watershed', w_image)

cv2.imshow('Image', c_image)

cv2.setMouseCallback('Image', onMouse)

cv2.waitKey(0)