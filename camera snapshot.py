'''This module can be used for logging'''

print("Initializing the libraries")
from cv2 import VideoCapture, imwrite
from time import sleep
##from datetime import datetime

import datetime

# initialize the objects needed
cam = VideoCapture(0)
filenameAndPath = "G:\\###python script\\daily log\\%s.jpg"

##x = 0
##
####wait for the camera to calibrate
##print("Calibrating sensor")
##while (x < 5):
##    x += 1
##    cam.read()
##    sleep(.3)
##
##s, img = cam.read()
##day = ""
##month = ""
##year = ""
##if s:    # frame captured without any errors
##    
##    if datetime.now().day > 9:
##        day = str(datetime.now().day)
##    else:
##        day = "0" + str(datetime.now().day)
##
##    if datetime.now().month > 9:
##        month = str(datetime.now().month)
##    else:
##        month = "0" + str(datetime.now().month)
##
##    year = str(datetime.now().year)
##    
##    m_fileNameandPath = ("G:\\###python script\\daily log\\%s%s%s.jpg" % (year, month, day))
##    imwrite(m_fileNameandPath,img)
##    print("shot taken")
##else:
##    print("Failed to capture")
##
##sleep(2)
##cam.release()

def takeSnapshot(pCamInstance, pDestination, pIsCamToBeReleased = False):
    '''Take a camera snapshot then save it to a destination
       As jpg file
       Param:
           pCamInstance -> The camera object
           pDestination -> The destination directory as well as the filename
                           (Format) <destination>\\<filename>%s.jpg
           pIsCamToBeReleased -> Closes the camera object if true otherwise do nothing '''

    ##wait for the camera to auto calibrate
    print("Calibrating the camera")
    for tIteration in range(5):
        
        pCamInstance.read()
        sleep(.3)

    retVal, capturedImage = pCamInstance.read()
    
    if retVal: ##If an image was captured without errors

        ##Get the system date and integrate to the filename and destination
        ##Then save the image
        dateCaptured = datetime.date.today().strftime("%Y%m%d")
        filenameAndPath = ( pDestination % (dateCaptured) )
        imwrite( filenameAndPath, capturedImage )
        print("shot taken")
        
    else:
        
        print("Failed to capture")

    ##Close the camera object
    if pIsCamToBeReleased:

        sleep(2)
        pCamInstance.release()

takeSnapshot(cam, filenameAndPath)
