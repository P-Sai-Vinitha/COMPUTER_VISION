Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\play therapy.jpg")
>>> c=cv2.resize(img,(100,100))
>>> cv2.imshow("original",img)
>>> cv2.imshow("resize",c)
>>> 