from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

numPics = 0
numVids = 0
filename = 'test'
title = 'Test'
fileTypeChosen = False
video = False
picture = False
recording = False
pics = []
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

#allow the camera to warm up its sensor
time.sleep(0.1)

#capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
     #grab the NumPy array of pixels
    if not fileTypeChosen:
        camera.annotate_text = 'click v for video mode \nor p for image mode'
    else:
        camera.annotate_text = title

    image = frame.array

    #show the frame
    cv2.imshow(title, image)
    key = cv2.waitKey(1) & 0xFF

    #clear the stream
    rawCapture.truncate(0)

    if key == ord('q'):
        rawCapture.close()
        cv2.destroyAllWindows()
        break
    elif not fileTypeChosen:
        if key == ord('v'):
            print 'video'
            fileTypeChosen = True
            video = True
        elif key == ord('p'):
            print 'picture'
            fileTypeChosen = True
            picture = True
    elif key == ord('r'):
        pics = []
        print 'reset'
        video = False
        picture = False
        fileTypeChosen = False
    elif video == True:
        pics += [image]
        if key == 32: #spacebar
            if recording == True:
                print 'saving'
                if numVids == 0:
                    addon = ''
                else:
                    addon = '_'+str(numVids+1)
                height, width, layers = pics[0].shape
                videowriter = cv2.VideoWriter(filename+addon+'.avi', 0, 32, (width, height), 1)
                for pic in pics:
                    videowriter.write(pic)
                videowriter.release()
                pics = []
                numVids += 1
                recording = False
            else:
                print 'recording'
                recording = True          
    elif picture == True:
        if key == 32: # spacebar
            if numPics == 0:
                addon = ''
            else:
                addon = '_'+str(numPics+1)
            numPics += 1
            cv2.imwrite(filename+addon+'.png', image)
