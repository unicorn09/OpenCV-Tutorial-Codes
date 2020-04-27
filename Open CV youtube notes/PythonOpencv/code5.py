'''
Created on 27-Apr-2020
More on Mouse Click events
@author: Harsh Raj
'''
import numpy as np
import cv2

# events=[i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        
        '''
        Draws Line between two points
        '''
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img,points[-1],points[-2],(255,255,0,0))
        
        '''
        Open BGR color in new image
        '''
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,255,0),-1)
        mycolorIMage=np.zeros((512,512,3),np.uint8)    
        mycolorIMage[:]=[blue,green,red]    
        
        
        cv2.imshow('color',mycolorIMage)
        
#             
# img=np.zeros((512,512,3),np.uint8) 
img=cv2.imread('HarshCompress.jpg')
points=[]
cv2.imshow('image',img) 
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()