#LESSON 36

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#img = cv2.imread('face1.jpg')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey) , (ex + ew, ey +eh), (0, 0, 255), 5)
        #smile = smile_cascade.detectMultiScale(roi_gray)
        #for (sx, sy, sw, eh) in smile:
        #    cv2.rectangle(roi_color, (sx, sy) , (sx + sw, sy + eh), (255, 0, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()