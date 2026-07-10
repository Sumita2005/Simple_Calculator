import cv2
""" Object Detection Module 
    Viola Jhones Method for object detection using Haar Cascade Classifier

    References: Youtube : Murtaza's Workshop - Robotics and AI
"""
def findObjects(img, ObjectCascade, scaleF=1.1, minN=4):

# Function to find objects in an image using Haarcascade file
# Parameters: IMAGE -> in which the objects need to be found
# Parameters: ObjectCascade->  Object Cascade creadted with cascade classifier
# Parameters: scaleF->  how much the image size is reduced at each image scale
# Parameters: minN-> how many neighbors each candidate rectangle should have to ACCEPT it as valid
# Parameters: return -> image with the rectangles draw and bounding box info 

    imgObjects = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    objects = ObjectCascade.detectMultiScale(imgGray, scaleF, minN)

    for (x, y, w, h) in objects:
        cv2.rectangle(imgObjects, (x, y), (x+w, y+h), (255, 0, 255), 2)

    return imgObjects, objects


def main():
    img = cv2.imread("../img.jpg")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgObjects , objects = findObjects(img, faceCascade)
    cv2.imshow("Image",imgObjects)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()