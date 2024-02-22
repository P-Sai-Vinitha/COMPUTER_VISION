Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> v=cv2.VideoCapture("C:\\Users\\P Sai vinitha\\OneDrive\\Desktop\\app figma\\Socks mp4.mp4")
>>> i=0
>>> while True:
	r,c=v.read()
	cv2.imshow("video",c)
	if(i<1000):
		cv2.waitKey(50)
	else:
		cv2.waitKey(10)
	i+=1

