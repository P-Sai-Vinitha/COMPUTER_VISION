Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import numpy as np
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\trauma and behav.jpg")
>>> p1=np.float32([[50,100],[100,150],[150,200],[200,50]])
>>> p2=np.float32([[20,40],[40,60],[60,80],[80,20]])
>>> h,_=cv2.findHomography(p1,p2)
>>> img2=cv2.warpPerspective(img,h,(600,600))
>>> cv2.imshow("original",img)
>>> cv2.imshow("linear",img2)
>>> 