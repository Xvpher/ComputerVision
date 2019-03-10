import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('Threshold')
cv2.createTrackbar('Value','Threshold',0,255,nothing)
cv2.setTrackbarPos('Value', 'Threshold', 127)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    value = cv2.getTrackbarPos('Value','Threshold')
    _, thresh = cv2.threshold(gray, value, 255, cv2.THRESH_BINARY)
    cv2.imshow('Window',thresh)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
