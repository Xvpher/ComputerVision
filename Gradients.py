import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    lap = cv2.Laplacian(frame, cv2.CV_64F)
    sobx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    soby = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

    cv2.imshow('Laplacian',lap)
    cv2.imshow('Sobel X',sobx)
    cv2.imshow('Sobel Y',soby)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
