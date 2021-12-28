import numpy as np
import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('harris_corner.avi', fourcc, 30.0, (640, 480),True)

while cv2.waitKey(32) < 0:
    ret, frame = capture.read()    # Read 결과와 frame

    if not ret :
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corner = cv2.cornerHarris(gray, 2, 3, 0.04)

    coord = np.where(corner > 0.05 * corner.max())
    coord = np.stack((coord[1], coord[0]), axis =-1)

    for(x, y) in coord:
        cv2.circle(frame, (x, y), 5, (0,0,255), 1, cv2.LINE_AA)

    cn_image = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    cv2.imshow("Harris corner image", frame)

    video.write(frame)

capture.release()
video.release()