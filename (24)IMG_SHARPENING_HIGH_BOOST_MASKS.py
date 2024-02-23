Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import numpy as np
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\emotional regulation.png")
>>> g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
>>> b=cv2.GaussianBlur(g,(5,5),2)
>>> height=g-b
>>> s=g+7*height
>>> cv2.imshow("original",img)
>>> cv2.imshow("gray",g)
>>> cv2.imshow("blur",b)
>>> cv2.imshow("sharp",s)
>>> 