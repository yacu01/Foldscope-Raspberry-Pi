import time
import picamera

waitTime = 300 #time in seconds

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2) # lets camera warm up
    for filename in camera.capture_continuous('img{counter :03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(waitTime) #waits waitTime seconds