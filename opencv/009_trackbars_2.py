#LESSON 12

import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150),font, 4, (0,0, 255), 3)

    k = cv.waitKey(1) & 0xFF
    # ESC - 27; Backspace - 8; Enter - 13;
    if k == 27:
        break

    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image', img)


cv.destroyAllWindows()