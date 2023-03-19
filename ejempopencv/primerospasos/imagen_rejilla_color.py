import cv2
import numpy as np

ancho = alto = 300

img = np.ones((alto,ancho, 3),np.uint8)*255
img[:] = (255, 255, 255)

for x in range(ancho):
    for y in range(alto):
        if x%50 == 0 or  y%50 == 0:
            img[y, x] = (0, 0, 255)

cv2.imshow('Rejilla ', img)

cv2.waitKey(0)
cv2.destroyAllWindows()