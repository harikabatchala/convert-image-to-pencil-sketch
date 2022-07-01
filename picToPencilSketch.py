#we use CV2 python package here for this.
#OpenCV stands for Open Source Computer Vision Library, which is widely used for image recognition or identification.
#it mainly focuses on image processing, video capture and analysis including features like face detection and object detection

#pip install opencv-python in terminal

import cv2
image= cv2.imread("E:/Python-Projects/convert image to pencil sketch/sunflower.jpg") #this includes location + / + name + .jpg or whatever mentioned in the properties
grey_filter=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)    #cvt converts colour  #BGR2GRAY means blue green red to gray
invert=cv2.bitwise_not(grey_filter)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedBlur=cv2.bitwise_not(blur)
sketch_filter=cv2.divide(grey_filter,invertedBlur,scale=200.0)
cv2.imwrite("output.png",sketch_filter)  #the name you want for your output + .png is must no matter if input is jpg or anything



