import cv2
import numpy as np

#captures frames from a camera
cap=cv2.VideoCapture(0)

#loop runs if capturing has been initialized.
while true:
    ret, frames=cap.read()  #read frames from video

    #convert bgr to hsv
    hsv= cv2.cvtColor(frames,cv2.COLOR_BGR2HSV)

    #define range of red color in HSV
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    #create a red HSV color boundary and threshold HSV image
    mask = cv2.inRange(hsv,lower_red,upper_red)

    #Bitwise-AND mask and original Image
    res = cv2.bitwise_and(frame,frame,mask=mask)

    #display an original image
    cv2.imshow('Original', frames)
    
    #find edges in the input image and mark them in the output map edges
    edges = cv2.Canny(frame,100,200)

    #Display edges in a frame
    cv2.imshow('Edges',edges)

    #wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

#de-allocate any associated memory usage
cap.release()
cv2.destroyAllWindows()
    

