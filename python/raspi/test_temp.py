#!/usr/bin/env python
########################################################################                                                                  
# This example demonstrates using the a Temperature/Humidity sensor with
# the GoPiGo
#
#
# http://www.dexterindustries.com/GoPiGo/                                                                
# History
# ------------------------------------------------
# Author     Date      		Comments
# Scott      28 March 17 	Initial Authoring
# 			     
import gopigo
import sys

blue = 0
white = 1

while True:
        try:

            [temp,humidity] = gopigo.dht(white)

            print("temp = %f C humidity = %f"%(temp, humidity))

        except IOError:
            print("I2C error")
