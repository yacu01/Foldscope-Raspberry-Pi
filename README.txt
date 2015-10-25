The first two scripts require OpenCV to be installed on the Raspberry Pi (RPi). While OpenCV is a large library that takes a while to install, the capabilities of it outweighs this hassle. It may seem a little overkill just for taking pictures and videos on the RPi, but it enables many other functions like the tracking of molecular organisms.

Here are the functions of the scripts in this repo:

recorder.py: 
  - python script to record videos and take pictures with the Raspberry Foldscope
  - can customize the filetype and filename for the pictures/videos
  - can save multiple pictures/videos with the same basic filename e.g. video_1.avi, video_2.avi etc.

video_player.py: 
  - python script to play back a previously recorded video
  - can navigate frame-by-frame forwards and backwards
  - can save multiple pictures of the frames of the video
  
timelapse.py:
  - take pictures for set intervals of time with indexed names
  - DOES NOT require OpenCV
