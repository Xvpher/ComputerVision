##There are 6 types of Morphological transformations -
##    1. Erosion
##    2. Dialation
##    3. Opening
##    4. Closing
##    5. Tophat
##    6. Blackhat
##
##1. Erosion = Removes the odd pixel out in a specific region of the image.
##
##2. Dialation = opposite of Erosion, pushes out.
##
##3. Opening = Removes False-Positives.
##
##4. Closing = Removes False-Negatives.
##
##5. Tophat = Original Image - Opening Image.
##
##6. Blackhat = Closing Image - Opening Image.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,50])
    upper_red = np.array([179,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
