import cv2
import numpy as np
cap = cv2.VideoCapture(0)
if(cap.isOpened()==False):
    print("Error Opening File")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        if(cv2.waitKey(25) == ord('q')):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
