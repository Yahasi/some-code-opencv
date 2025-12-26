import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def process(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #img = cv2.imread('shapes.jpg')
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img


while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#cv2.imshow('img', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()