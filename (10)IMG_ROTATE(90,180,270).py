Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\self soothing.png")
>>> c=cv2.rotate(img,cv2.ROTATE_180)
>>> v=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
>>> x=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
>>> cv2.imshow("original",img)
>>> cv2.imshow("180 degree",c)
>>> cv2.imshow("90 degree",v)
>>> cv2.imshow("270 degree",x)
>>> 