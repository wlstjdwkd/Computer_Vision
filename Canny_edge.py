import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('canny_edge.avi', fourcc, 20.0, (1280, 480), False)

while cv2.waitKey(32) < 0:
    ret, frame = capture.read()    # Read 결과와 frame

    if not ret :
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    c_image = cv2.Canny(gray, 150, 300)

    addh = cv2.hconcat([gray, c_image])

    cv2.imshow('Canny image', addh)

    video.write(addh)

capture.release()
video.release()