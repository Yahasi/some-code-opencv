#LESSON 17

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', cv2.IMREAD_GRAYSCALE)
_, mask1 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation1 = cv2.dilate(mask1, kernal, iterations=2)
erosion1 = cv2.erode(mask1, kernal, iterations=2)
opening1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernal)
closing1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask1, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask1, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask1', 'dilation1', 'erosion1', 'opening1', 'closing1', 'mg','th']
images = [img, mask1, dilation1, erosion1, opening1, closing1, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()