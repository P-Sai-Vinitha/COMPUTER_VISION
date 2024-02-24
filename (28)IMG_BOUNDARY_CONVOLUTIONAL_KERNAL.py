Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import numpy as np
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\img1.jpg")
>>> dx=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=1,dy=0)
>>> dy=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=0,dy=1)
>>> edges=cv2.magnitude(dx,dy)
>>> thresh=100
>>> edges[edges<thresh]=0
>>> edges[edges>=thresh]=255
>>> cv2.imshow("edges",edges)
>>> cv2.imshow("original",img)
>>> 