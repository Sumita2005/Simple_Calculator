import cv2
#print(cv2.__version__)
import numpy as np
img = cv2.imread('img.jpg')


imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),5)
imgCanny = cv2.Canny(img,100,150)

kernel = np.ones((5,5),np.uint8)
imgDia = cv2.dilate(imgCanny,(7,7),iterations=1)
imgErode = cv2.erode(imgDia,(7,7),iterations=2)

cv2.imshow("Image",img)
#cv2.imshow("Image Gray",imgGray)
#cv2.imshow("Image Blur",imgBlur)
#cv2.imshow("Image Canny",imgCanny)   #------- 5main functions of image processing 
cv2.imshow("Image Dilation",imgDia)
cv2.imshow("Image Erode",imgErode)


cv2.waitKey(0)
