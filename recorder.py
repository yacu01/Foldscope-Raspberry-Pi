from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

numPics = 0 #change this to the number of pictures that have already been made
numVids = 0 #change this to the number of videos that have already been made
filename = 'test'  #DONOT put the filetype in the filename

pictureFileType = '.png' #sets the picture file type
videoFileType = '.avi' #sets the video file type

title = 'Test' #The title displayed on the video/photo

fileTypeChosen = False
video = False
picture = False
recording = False
pics = []

camera = PiCamera() #initializes the camera
camera.resolution = (640, 480) #resolution for the camera.. too high and the RPi cannot display the image. Can go higher if not displaying the image. 
camera.framerate = 32 #sets the framerate for the camera

### camera settings ###
#camera.shutter_speed = 
#camera.sharpness = 
#camera.saturation = 
#camera.iso = 
#camera.image_effect = 
#camera.contrast = 
#camera.brightness = 


rawCapture = PiRGBArray(camera, size=camera.resolution)

#allow the camera to warm up its sensor
time.sleep(0.1)

#capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    
    if not fileTypeChosen:
        #prompt user to select the mode
        camera.annotate_text = 'click v for video mode \nor i for image mode'
    else:
        #displays the title
        camera.annotate_text = title

    #grab the NumPy array of pixels    
    image = frame.array

    #show the frame
    cv2.imshow(title, image)
    
    #wait a minimum of one milisecond, record if key pressed
    key = cv2.waitKey(1) & 0xFF

    #clear the stream
    rawCapture.truncate(0)

    if key == ord('q'):
        #quits the script
        #TODO fix the closing mechanism
        camera.close()
        cv2.destroyAllWindows()
        break
    elif not fileTypeChosen:
        if key == ord('v'):
            print 'video mode'
            fileTypeChosen = True
            video = True
        elif key == ord('i'):
            print 'image mode'
            fileTypeChosen = True
            picture = True
    elif key == ord('r'):
        #allows user to switch modes
        pics = []
        print 'reset'
        video = False
        picture = False
        fileTypeChosen = False
    elif video == True: #video mode
        pics += [image] #adds the current image to list of images
        if key == 32: #spacebar
            if recording == True:
                # end the recording and save the video
                addon = '_'+str(numVids+1) #addon the number of videos already made so it doesn't override a video
                height, width, layers = pics[0].shape
                
                #construct a video writer
                videowriter = cv2.VideoWriter(filename+addon+videoFileType, 0, 32, (width, height), 1) 
                
                #loop through the pics and 'write' it to the video writer object                
                for pic in pics:
                    videowriter.write(pic)
                    
                #'releases' the video writer and save the video
                videowriter.release()
                
                pics = [] #resets the picture array to empty
                numVids += 1 #adds one to the number of videos created
                recording = False
            else:
                print 'recording'
                recording = True          
    elif picture == True: #picture mode
        if key == 32: #spacebar
            addon = '_'+str(numPics+1)
            numPics += 1
            cv2.imwrite(filename+addon+pictureFileType, image)
