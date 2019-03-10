import cv2
import numpy as np

img1 = cv2.imread('image_1.png')
img2 = cv2.imread('logo1.png')

r,c,channel = img2.shape
roi = img1[0:r,0:c]

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask = mask)
img2_fg = cv2.bitwise_and(img2, img2, mask = mask_inv)
dst = cv2.add(img1_bg, img2_fg)
img1[0:r,0:c] = dst

cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1',img1)
cv2.imshow('dst',dst)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)

cv2.waitKey(0)
cv2.destroyAllWindows()
