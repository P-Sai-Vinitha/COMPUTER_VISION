Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import numpy as np
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\eye contact.jpg")
>>> x=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=1,dy=0)
>>> y=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=0,dy=1)
>>> g=np.sqrt((x**2)+(y**2))
>>> c=img+1+g
>>> cv2.imshow("sharp",c)
>>> cv2.imshow("original",img)
>>> 