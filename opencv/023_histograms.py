import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)
#img = np.zeros((200, 200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#b, g, r = cv2.split(img)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
#cv2.imshow('img', img)
#cv2.imshow('b', b)
#cv2.imshow('g', g)
#cv2.imshow('r', r)


#plt.hist(b.ravel(), 256, [0, 256], color='b')
#plt.hist(g.ravel(), 256, [0, 256], color='g')
#plt.hist(r.ravel(), 256, [0, 256], color='r')

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()


