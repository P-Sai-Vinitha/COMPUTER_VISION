Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\conflict resolution.png")
>>> x,y=100,100
>>> height,width=200,100
>>> c=img[y:y+height,x:x+width]
>>> cv2.imshow('ROI',c)
>>> cv2.imshow("original",img)
>>> 