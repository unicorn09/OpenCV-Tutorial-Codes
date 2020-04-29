'''
Created on 29-Apr-2020

@author: Harsh Raj
'''
import cv2 as cv
import numpy as np

img=cv.imread('gradient.png',0)
_, th1=cv.threshold(img,50,255,cv.THRESH_BINARY)
_,th2=cv.threshold(img,200,255,cv.THRESH_BINARY_INV)

cv.imshow('image',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
# cv.resizeWindow('image',600,400)
# cv.resizeWindow('th1',600,400)
cv.waitKey(0)
cv.destroyAllWindows()