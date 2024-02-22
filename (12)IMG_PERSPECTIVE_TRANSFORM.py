Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import numpy as np
>>> img=cv2.imread("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\emotional regulation.png")
>>> p1=np.float32([[340,60],[60,234],[234,234],[234,240]])
>>> p2=np.float32([[240,160],[160,204],[204,204],[334,340]])
>>> c=cv2.getPerspectiveTransform(p1,p2)
>>> v=cv2.warpPerspective(img,c,(600,600))
>>> cv2.imshow("image",v)
>>> cv2.imshow("original",img)
>>> 