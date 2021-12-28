import numpy as np
import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('hough_transform.avi', fourcc, 30.0, (1280, 480), True)

while cv2.waitKey(32) < 0:
    ret, color = capture.read()
    ret, frame = capture.read()    # Read 결과와 frame

    if not ret :
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (3,3))

    c_image = cv2.Canny(gray,50, 150, apertureSize=3)

    #addh = cv2.hconcat([gray,c_image])



    lines = cv2.HoughLines(c_image, 1, np.pi/180, 100)

    scale = frame.shape[0] + frame.shape[1]

    if lines is None: continue

    for line in lines:
        rho, theta = line[0]

        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + scale*(-b))
        y1 = int(y0 + scale*(a))
        x2 = int(x0 - scale*(-b))
        y2 = int(y0 - scale*(a))

        cv2.line(frame, (x1,y1), (x2,y2), (255,0,255), 1)

    #cv2.imshow("Line image", frame)

    addh = np.hstack((color, frame))

    cv2.imshow('hough_tramsform', addh)

    video.write(addh)

capture.release()
video.release()