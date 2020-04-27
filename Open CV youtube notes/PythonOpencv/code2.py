'''
Created on 25-Apr-2020

@author: Harsh
'''
import cv2

img=cv2.imread('Harshcompress.jpg',1)
img=cv2.line(img,(0,0),(255,255),(255,255,0),10)

img=cv2.arrowedLine(img,(0,255),(255,255),(255,255,0),10)

img=cv2.rectangle(img,(384,0),(310,120),(0,0,255),-1)
img=cv2.circle(img,(347,63),63,(0,255,0),-1)
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
img=cv2.putText(img,'Prashu',(10,400),font,4,(0,0,0),10,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
