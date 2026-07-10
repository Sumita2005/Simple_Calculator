import cv2
import numpy as np
#------image size and rescale

img = cv2.imread('img.jpg') #--read img
print(img.shape)
imgResize1 = cv2.resize(img,(500,200)) #--resize img
imgResize2 = cv2.resize(img,(0,0),None,0.5,0.5) #--resize img with scale factor img is scale down to 50 % of og version of image
print(imgResize2.shape)

#-------image crop
imgCrop = img[50:375,220:520] #--crop image from 0 to 200 in y axis and 200 to 500 in x axis
cv2.imshow("Image",img)
cv2.imshow("Image Resize 1",imgResize1)
cv2.imshow("Image Resize 2",imgResize2)
cv2.imshow("Image Cropped",imgCrop)

cv2.waitKey(0)