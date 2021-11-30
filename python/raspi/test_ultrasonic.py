#!/usr/bin/env python
########################################################################                                                                  
# This example demonstrates using the Ultrasonic sensor with
# the GoPiGo
#
#
# http://www.dexterindustries.com/GoPiGo/                                                                
# History
# ------------------------------------------------
# Author     Date      		Comments
# Scott      28 March 17 	Initial Authoring
#
#
########################################################################
#
# ! Attach Ultrasonic sensor to A1 Port.
#
########################################################################
from gopigo import *
import time

print "Press ENTER to start"
raw_input()
while True:
	dist=us_dist(15)			#Find the distance of the object in front
	print "Distance:",dist,'cm'
	time.sleep(.5)
