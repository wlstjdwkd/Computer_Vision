import numpy as np
import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('sift.avi', fourcc, 30.0, (640, 480),True)

while cv2.waitKey(32) < 0:
    ret, frame = capture.read()    # Read 결과와 frame

    if not ret :
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sift_detector = cv2.xfeatures2d.SIFT_create()

    keypoints, descriptor = sift_detector.detectAndCompute(gray, None)
    print('Keypoint: ', len(keypoints), 'Descriptor: ', descriptor.shape)
    print(descriptor)

    ov_image = cv2.drawKeypoints(frame, keypoints, None,
                                 flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("SIFT detector keypoint image", ov_image)

    video.write(ov_image)

capture.release()
video.release()