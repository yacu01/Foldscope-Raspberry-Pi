import cv2
import numpy as np
import os

Folder = 'Videos'
File = 'test.avi'
SaveAs = 'testVidSave'

play = False
numSaves = 0

cd = os.getcwd()
FilePath = os.path.join(cd, Folder, File)

Video = cv2.VideoCapture(FilePath)
num = 0
Video.set(1, 100)
retVal, frame = Video.read()
while retVal == True:
    cv2.imshow('pic', frame)
    if play:
        num += 1
        key = cv2.waitKey(1) & 0xFF #waits for one millisecond
    else:
        key = cv2.waitKey(0) & 0xFF #waits indefinitely

        
    if key == ord('p'):
        play = not play
    elif key == 81: #left arrow
        num -= 5 # goes to previous frame
    elif key == 83: #right arrow
        num += 1
    elif key == ord('s'):
        if numSaves == 0:
            addon = ''
        else:
            addon = '_'+str(numSaves)
        cv2.imwrite(SaveAs+addon+'.png', frame)
        numSaves += 1

    Video.set(1, num)
    retVal, frame = Video.read()

cv2.destroyAllWindows()
