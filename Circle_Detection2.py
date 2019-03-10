import cv2
import numpy as np

def nothing (x):
    pass

img = cv2.imread('balls5.png')
img = cv2.pyrDown(img)
#img = cv2.pyrDown(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
gray = cv2.Canny(gray, 100, 200)
font = cv2.FONT_HERSHEY_SIMPLEX
wnd = 'Tracks'
cv2.namedWindow(wnd)

cv2.createTrackbar('Param1', wnd, 0, 50, nothing)
cv2.createTrackbar('Param2', wnd, 0, 50, nothing)
cv2.createTrackbar('MinRadius', wnd, 0, 50, nothing)
cv2.createTrackbar('MaxRadius', wnd, 0, 50, nothing)

cv2.setTrackbarPos('Param1', wnd, 30)
cv2.setTrackbarPos('Param2', wnd, 20)
cv2.setTrackbarPos('MinRadius', wnd, 0)
cv2.setTrackbarPos('MaxRadius', wnd, 0)

while True:

    p1 = cv2.getTrackbarPos('Param1', wnd)
    p2 = cv2.getTrackbarPos('Param1', wnd)
    minR = cv2.getTrackbarPos('MinRadius', wnd)
    maxR = cv2.getTrackbarPos('MaxRadius', wnd)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, param1 = p1, param2 = p2, minRadius = minR, maxRadius = maxR)
    circles = np.uint16(np.around(circles))
    c = 49
    for i in circles[0,:]:
        text = chr(c)
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        cv2.putText(img, text, (i[0]+5,i[1]+5), font, 0.75, (255,255,255), 2, cv2.LINE_AA)
        c = ord(text) + 1

    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break

##cv2.imshow('frame', img)    
##cv2.waitKey(0)
cv2.destroyAllWindows()
