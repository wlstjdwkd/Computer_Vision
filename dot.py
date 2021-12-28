import cv2
import sys
# /usr/local/lib/python3.6/dist-packages/cv2/python-3.6/cv2.so

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#path = 'C:/Users/user/FaceDetection/Packages/FD/face.jpg'

img = cv2.imread(sys.argv[0])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    #cv2.circle(img, (x+int(w/2),y+int(h/2)), int(w/2), (0,0,255), 2)
    cropped = img[y: y+h, x:x+w]
    cropped = img[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]

height, width = cropped.shape[:2]
w, h = (64, 64)
temp = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
#cv2.imshow('Output', output)
cv2.imwrite("pixelArt.png", output)
cv2.waitKey(0)