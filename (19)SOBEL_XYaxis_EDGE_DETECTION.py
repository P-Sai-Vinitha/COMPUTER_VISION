Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\conversation skills.png")
>>> c=cv2.Sobel(img,ddepth=cv2.CV_64F,dx=1,dy=1)
>>> cv2.imshow("original",img)
>>> cv2.imshow("sobel",c)
>>> 