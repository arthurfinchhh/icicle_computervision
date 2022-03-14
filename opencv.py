import cv2 
import time

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  #adjusted for new webcam
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

i = 0
while (True):
 
    (ret, frame) = capture.read()
 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    """we want to Remove black and white and do this in the analysis code"""
    (thresh, blackAndWhiteFrame) = cv2.threshold(grayFrame, 127, 255, cv2.THRESH_BINARY)
 
 
    cv2.imshow('video bw', blackAndWhiteFrame)
    cv2.imshow('frame', frame)

    out = cv2.imwrite('capture{}.jpg'.format(i), frame) #savng original frame
    time.sleep(60)

    i = i+1
    

    if cv2.waitKey(1) == 27:
        break
 
capture.release()
cv2.destroyAllWindows()
