import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    gray = cv2.Canny(gray, 100, 200)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1 = 30, param2 = 20, minRadius = 0, maxRadius = 0)
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
