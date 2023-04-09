##
##from SimpleCV import Image, Camera
##
##cam = Camera()
##img = cam.getImage()
##img.save("filename.jpg")
##using OpenCV:

####from cv2 import *
##from cv2 import VideoCapture, imwrite
### initialize the camera
##cam = VideoCapture(0)   # 0 -> index of camera
##s, img = cam.read()
##if s:    # frame captured without any errors
####    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
####    imshow("cam-test",img)
####    waitKey(0)
####    destroyWindow("cam-test")
##    imwrite("G:\\filename.jpg",img)
##    cam.release()



##from cv2 import VideoCapture, imwrite
##from time import sleep
##from os import popen
##from datetime import datetime
##
### initialize the camera
##cam = VideoCapture(0)
##c_blnCapturing = False
##c_blnIsTaskMgrOnline = popen('tasklist /FI "IMAGENAME eq taskmgr.exe"').read().strip().split('\n')
##while(len(c_blnIsTaskMgrOnline) == 1):
##
##    s, img = cam.read()
##    if s:    # frame captured without any errors
##        imwrite("G:\\python script\\daily log\\filename.jpg",img)
##
##        ##print while we're still capturing
##        if not c_blnCapturing:
##            print("Rendered and written")
##            c_blnCapturing = True
##        
##    else:
##        print("Capture failed Exiting...")
##        break
##
##    c_blnIsTaskMgrOnline = popen('tasklist /FI "IMAGENAME eq taskmgr.exe"').read().strip().split('\n')
##    sleep(1)
##
##cam.release()

from cv2 import VideoCapture, imwrite
from time import sleep
from datetime import datetime

# initialize the camera
cam = VideoCapture(0)
x = 0

##wait for the camera to calibrate
while (x < 5):
    x += 1
    cam.read()
    sleep(.3)

s, img = cam.read()
day = ""
month = ""
year = ""
if s:    # frame captured without any errors
    
    if datetime.now().day > 9:
        day = str(datetime.now().day)
    else:
        day = "0" + str(datetime.now().day)

    if datetime.now().month > 9:
        month = str(datetime.now().month)
    else:
        month = "0" + str(datetime.now().month)

    year = str(datetime.now().year)
    
    m_fileNameandPath = ("G:\\python script\\daily log\\%s%s%s.jpg" % (year, month, day))
    imwrite(m_fileNameandPath,img)
    print("Mugshot taken")
else:
    print("Failed to capture")

sleep(2)
cam.release()
    
