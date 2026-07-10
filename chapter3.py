import cv2
import numpy as np

#----change color of image
img = np.zeros((512,512,3), np.uint8)
#img[:] = 255,0,0 #--BGR value for blue color
#img[:] = 255,0,255 # --BGR value for purple color
img[:]= 255,255,255 #--BGR value for WHITE color

#----draw shapes on image
#cv2.circle(img,(256,256),150,(0,69,255),5) #--draw circle on image with center at (256,256) and radius of 150 with color BGR(0,69,255) and thickness of 5

#----CIRCLE FILLED WITH COLOR FULLY
cv2.circle(img,(256,256),150,(0,69,255),cv2.FILLED)

#------DRAW RECTANGLE ON IMAGE
cv2.rectangle(img,(130,226),(382,286),(255,255,255),cv2.FILLED) #--draw rectangle on image with top left corner at (130,256) and bottom right corner at (382,286) with color BGR(0,69,255) and thickness of 5

#----DRAW LINE ON IMAGE
cv2.line(img,(130,296),(382,296),(255,255,255),2) #--draw line on image from point (130,256) to point (382,286) with color BGR(0,69,255) and thickness of 5

#-----put text on image
cv2.putText(img,"Smrutis Cake Boutique",(137,262),cv2.FONT_HERSHEY_DUPLEX,0.75,(0,69,255),1) #--put text on image at point (130,256) with font FONT_HERSHEY_COMPLEX and font scale of 1 with color BGR(0,69,255) and thickness of 2
cv2.imshow("Image",img)
cv2.waitKey(0)
