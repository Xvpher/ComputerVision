import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient_2.png',0)
h = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(h, color = 'r')
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
