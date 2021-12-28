import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('capture.avi', fourcc, 30.0, (640, 480),False)

while cv2.waitKey(32) < 0:
    ret, frame = capture.read()    # Read 결과와 frame

    if not ret :
        gray = cv2.imread(frame,  cv2.IMREAD_GRAYSCALE)

        s_imageXY = cv2.Sobel(gray, cv2.CV_8U, 1, 1, ksize = 3)

        cv2.imshow('Sobel X-Y direction image', s_imageXY)

        video.write(frame)

        break





capture.release()
video.release()