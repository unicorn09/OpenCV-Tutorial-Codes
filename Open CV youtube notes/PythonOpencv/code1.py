import cv2
cap=cv2.VideoCapture(0)
out=cv2.VideoWriter('code1OpenCv.avi')
fourcc=cv2.VideoWriter_fourcc(*'XVID') 
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame=cap.read()
    
    #cap.get(cv2.CAP_PROP)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()