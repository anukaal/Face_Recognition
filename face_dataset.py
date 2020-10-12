import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")

count = 0


