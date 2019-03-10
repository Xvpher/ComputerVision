import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('me1.jpg',0)
img2 = cv2.imread('me2.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = False)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2, matches[:10], None, flags = 2)

plt.imshow(img3)
#cv2.imshow('Image', img3)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
