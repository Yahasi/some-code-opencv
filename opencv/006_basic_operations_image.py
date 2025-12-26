import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge([b,g,r])

ball = img[290:340, 335:390]
print(ball.shape)
img[283:333, 105:160] = ball
print(img[283:333, 105:160].shape)

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
cv2.imshow('image', img)

#dst = cv2.add(img, img2);
dst = cv2.addWeighted(img, .9, img2, .1, 0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()