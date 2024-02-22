Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import numpy as np
>>> img=cv2.VideoCapture("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\video socks.mp4")
>>> p1=np.float32([[120,30],[230,300],[300,234],[234,20]])
>>> p2=np.float32([[100,130],[30,30],[30,34],[34,20]])
>>> c=cv2.getPerspectiveTransform(p1,p2)
>>> while True:
	r,v=img.read()
	t=cv2.warpPerspective(v,c,(600,600))
	cv2.imshow("perspective",t)

