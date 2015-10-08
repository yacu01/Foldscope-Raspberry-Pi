import cv2
import os
import numpy as np

Folder = 'Videos' #Folder relative to the file of the video
File = 'HTAB_2mM_150ums_VaryConcentration_trial5.avi' #File Name of the video
SaveAs = 'testVidSave' #What to save the pictures as

play = False
reverse = False
numSaves = 0

cd = os.getcwd()
FilePath = os.path.join(cd, Folder, File)

Video = cv2.VideoCapture(FilePath)
num = 500
Video.set(1, num) #set the video to a certain frame, does not work #TODO fix
playBackSpeed = 4

#retVal is a boolean that is true on a succesful read of the next frame
retVal, frame = Video.read()

while retVal == True:
    cv2.imshow('pic', frame)

    if play:
        num += playBackSpeed
        key = cv2.waitKey(1) & 0xFF #waits a minimum of one millisecond
    elif reverse:
        num -= playBackSpeed
        key = cv2.waitKey(1) & 0xFF
    else:        
        key = cv2.waitKey(0) & 0xFF #waits indefinitely
        
    if key == ord('p'):
        play = not play
    if key == ord('r'):
        reverse = not reverse
    elif key == ord('q'):
        Video.release()
        cv2.destroyAllWindows()
    elif key == ord('a'): #key a      
        num -= 1 #goes to previous frame
    elif key == ord('d'): #key d
        num += 1 #goes to the next frame
    elif key == ord('s'): #saves the image
        if numSaves == 0:
            addon = ''
        else:
            addon = '_'+str(numSaves)
        cv2.imwrite(SaveAs+addon+'.png', frame)
        numSaves += 1
    
    Video.set(1, num)
    retVal, frame = Video.read() #read the next frame

Video.release()
cv2.destroyAllWindows() #closes all the windows.. does not seem to work