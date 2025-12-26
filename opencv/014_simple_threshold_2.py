#LESSON 16

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png', cv2.IMREAD_GRAYSCALE)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


kernal = np.ones((2, 2), np.uint8)

dilation1 = cv2.dilate(th1, kernal)
dilation2 = cv2.dilate(th2, kernal)

titles = ['image', 'th1', 'th2', 'th3', 'th4', 'th5', 'dilation1', 'dilation2']
images = [img, th1, th2, th3, th4, th5, dilation1, dilation2]

for i in range(8):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()