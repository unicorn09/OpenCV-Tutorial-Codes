'''
Created on 01-May-2020
Face Recognition
@author: Harsh Raj
'''
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img=cv2.imread('Harshcompress.jpg')
cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, img = cap.read()

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)

    cv2.imshow('frame',gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('img',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()