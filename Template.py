import cv2
import numpy as np
from matplotlib import pyplot as plt

main = cv2.imread('main.png')
main_gr = cv2.cvtColor(main, cv2.COLOR_BGR2GRAY)

port = cv2.imread('port.png',0)
#port = cv2.cvtColor(port, cv2.COLOR_BGR2GRAY)
r,c = port.shape[::-1]
#print(r,c)
res = cv2.matchTemplate(main_gr, port, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(main, pt, (pt[0]+r,pt[1]+c), (0,255,255), 2)

cv2.imshow('detected', main)

cv2.waitKey(0)
cv2.destroyAllWindows()
