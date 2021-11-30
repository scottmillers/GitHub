#!/usr/bin/env python
# This code depends upon the picamera library
# http://piccamera.readthedocs.io
# You need to install the python3-picamera package using
# > sudo apt-get install python3-picamera
# 
# This example is to test the GoPiGo Camera by creating a photo and putting it
# into a file called image.jpg
#
from time import sleep
from picamera import PiCamera


camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm up time
sleep(2)

camera.capture('image.jpg')
