'''
Created on 29-Apr-2020
Image with coordinates
@author: Harsh Raj
'''
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('Harshcompress.jpg',-1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('image',img)

plt.imshow(img)
plt.show()
# plt.xticks([1]), plt.yticks([])
cv2.waitKey(0)
cv2.destroyAllWindows()