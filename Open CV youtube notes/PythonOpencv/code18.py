'''
Created on 01-May-2020

@author: Harsh Raj
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("sudoko.png",cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobleX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX=np.uint8(np.absolute(sobleX))
sobelY=np.uint8(np.absolute(sobelY))

sobelCombined=cv2.bitwise_or(sobelX,sobelY)

titles=['images','Laplacian','sobelX','sobelY','SobelCombined']
images=[img,lap,sobelX,sobelY,sobelCombined]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()