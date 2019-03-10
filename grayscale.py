import cv2
import numpy as np
cap = cv2.VideoCapture(0)
if(cap.isOpened()==False):
    print("Error Opening File")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10,(frame_width,frame_height))
while(True):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        out.write(gray)
        cv2.imshow('frame',gray)
        if(cv2.waitKey(1) == ord('q')):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
