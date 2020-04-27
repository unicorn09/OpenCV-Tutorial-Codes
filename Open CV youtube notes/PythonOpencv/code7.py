'''
Created on 28-Apr-2020

@author: Harsh Raj
'''
import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread("Harshcompress.jpg")

bitAnd=cv2.bitwise_and(img2,img1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow('bitAnd',bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()