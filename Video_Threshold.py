import cv2
import numpy

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):
    ret, frame = cap.read()
    #frame = cv2.medianBlur(frame,5)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #ret, thresh = cv2.threshold(frame,127, 255,cv2.THRESH_BINARY)
    thresh = cv2.adaptiveThreshold(frame,128,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imshow('Gaussian',thresh)
    #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    #out.write(thresh)
    if(cv2.waitKey(1) == ord('q')):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
