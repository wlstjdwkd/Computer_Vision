import cv2
import numpy as np

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('circular_hough_transform.avi', fourcc, 30.0, (640, 480), True)

while cv2.waitKey(32) < 0:
    ret, frame = capture.read()    # Read 결과와 frame

    if not ret :
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.blur(gray, (3,3))

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 500,
                               param1 = 250, param2 = 10,
                               minRadius = 30, maxRadius = 80)
    circles = np.uint16(np.around(circles))

    for circle in circles[0]:
        cv2.circle(frame, (circle[0], circle[1]), 2, (255,0,0), 2)
        cv2.circle(frame, (circle[0], circle[1]), int(circle[2]), (0,0,255), 2)



    cv2.imshow('asfd', frame)

    video.write(frame)

capture.release()
video.release()