import cv2
import numpy as np

img = cv2.imread('image1.png')
lower = cv2.pyrDown(img)

#cv2.imshow('Original',img)

for i in range(4):
    name = 'lower ' + '1'*i
    cv2.imshow(name,lower)
    lower = cv2.pyrDown(lower)

cv2.waitKey(0)
cv2.destroyAllWindows()
