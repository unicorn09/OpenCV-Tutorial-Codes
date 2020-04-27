'''
Created on 27-Apr-2020

@author: Harsh Raj
'''
import cv2

img=cv2.imread('HarshCompress.jpg')
img2=cv2.imread('opencv.png')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
cult=img[270:99,399:96]
img[100:150,300:180]=cult

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

dst=cv2.addWeighted(img,.9,img2,.1,0)

cv2.imshow('image',dst) 
cv2.waitKey(0)
cv2.destroyAllWindows()