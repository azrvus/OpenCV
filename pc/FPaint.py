import cv2
import numpy as nm
import os
import time
import OpenCV as cv

fpath = "Header"
myList = os.listdir(fpath)
print(myList)
overlay = []
for imPath in  myList:
    image = cv2.imread(f"{fpath}/{imPath}")
    overlay.append(image)
print(len(overlay))

header = overlay[0]

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = cv.handDetector(detectionCon=0.85)
while True:
    #1.import Image
    success, img = cap.read(header)
    img = cv2.flip(img, 1)
    #2.find hand Land mark
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist)!= 0:
        print(lmlist)

        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]




    #Setting the header image
    img[0:125,0:1280] = header
    cv2.imshow("Image", img)
    cv2.waitKey(1)