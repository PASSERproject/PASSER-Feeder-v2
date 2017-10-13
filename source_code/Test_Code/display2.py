import cv2
import random
import os
import threading
import time

## This program continuously chooses a random picture in the DisplayPictures
## folder and displays it for 5 seconds
def func():
    time.sleep(1)
    cv2.destroyAllWindows()

while(1):
    #Choose a random file in 'DisplayPictures' folder
    filename = 'DisplayPictures/' +  random.choice(os.listdir('DisplayPictures'))
    
    #Debug print file name
    #print(filename)

    #Create an 'image' from the filename
    image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    
    #Open a fullscrean window to display the image
    cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("test",cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    
    t = threading.Thread(target = func)
    t.daemon = True
    t.start()

    #Show the image on screen
    cv2.imshow("test", image)
 
    #Wait for 5 seconds
    cv2.waitKey(0)

    t.join()
