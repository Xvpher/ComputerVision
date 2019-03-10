import cv2
import numpy as np
cap = cv2.VideoCapture(0)
##frame_width = int(cap.get(3))
##frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outpy.avi', fourcc, 20.0,(640,480))
while(True):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if(cv2.waitKey(1) == ord('q')):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
