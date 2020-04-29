'''
Created on 29-Apr-2020
Adaptive Thresholding
@author: Harsh Raj
'''
import cv2 as cv
import numpy as np



img=cv.imread('sudoko.png',0)

_th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2);

cv.imshow('img',img)
cv.imshow('th2',th2)

cv.waitKey(0)
cv.destroyAllWindows()