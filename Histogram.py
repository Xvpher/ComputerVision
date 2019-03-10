import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image1.png')
color = ('b','g','r')
for i,col in enumerate(color):
    h = cv2.calcHist([img],[i],None,[16],[0,256])
    plt.plot(h, color = col)
    plt.xlim([0,16])
plt.show()

#cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


