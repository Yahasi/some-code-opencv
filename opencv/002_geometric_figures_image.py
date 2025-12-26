#LESSON 6

import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread('lena.jpg', 1)
#foto = np.zeros([512,512, 3], np.uint8)

foto = cv2.line(foto, (0,0), (255,255), (255,0,255), 5)
foto = cv2.arrowedLine(foto, (0,255), (255,255), (120,100,155), 5)

foto = cv2.rectangle(foto, (384,0), (510,128), (0,0,255), 5)
foto = cv2.circle(foto, (447,63), 63, (0,255,15), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
foto = cv2.putText(foto,'OpenCV', (10,500),font,4, (132,23,95),10,cv2.LINE_AA)
foto = cv2.ellipse(foto,  (120,100), (100,50), 45, 0, 360, (0, 0, 255), 5)
cv2.imshow('foto', foto)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', foto)
    cv2.destroyAllWindows()