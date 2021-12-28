import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('sobelXY.avi', fourcc, 30.0, (640, 480), False)

while cv2.waitKey(32) < 0:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fil = cv2.Sobel(gray, cv2.CV_8U, 1, 1, ksize=3)
    ret, fil = cv2.threshold(gray, 128, 255, cv2.THRESH_OTSU)
    if not ret:
        break

    cv2.imshow("Frame", fil)

    video.write(fil)

capture.release()
video.release()