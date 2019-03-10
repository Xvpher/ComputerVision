import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    kernel = np.ones((5,5), np.float32)/25
    smooth = cv2.filter2D(frame, -1, kernel)
    g_blur = cv2.GaussianBlur(frame, (15,15), 0)
    m_blur = cv2.medianBlur(frame, 15)

    cv2.imshow('frame',frame)
    cv2.imshow('Smoothed',smooth)
    cv2.imshow('Gaussian Blur',g_blur)
    cv2.imshow('Median Blur',m_blur)

    if cv2.waitKey(1) == ord('q'):
        break
#print(kernel)    
cap.release()
cv2.destroyAllWindows()
