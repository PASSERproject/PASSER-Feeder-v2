#!/usr/bin/python
# John Filipowicz
# Radford University
 
# Purpose: Library file to either collect data or capture video

import sys
sys.path.insert(0, '~/sensor_libraries/DHT')
import Adafruit_DHT
import datetime
import time
from subprocess import call


def collect():

	# GPIO pin connected to data pin verify correctness.
	pin = 17

	# Reading the sensor. If using the DHT22, change the 11 to 22
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)

	# Un-comment the below line to use F instead of C
	# temperature = temperature * 9/5.0 + 32

	# Change the name of the file by changing the string literal "x.csv"
	# Don't do this. The filename is hard coded right now
	filename = "/media/pi/FEEDER_DATA/DHT_data.csv"
	datum = open(filename, "a")

	# Writing the sensor data to file
	datum.write("\n" + str(temperature) + ",")
	datum.write(str(humidity) + ",")
	datum.write(str(datetime.datetime.now()))
	datum.close()

def capture():
    # Output location
    path = "/media/pi/FEEDER_DATA/"

    # File Name
    output = time.strftime("%m-%d-%Y_%H-%M-%S") + ".avi"

    # Frames Per Second
    fps = 30

    # Video Duration
    time = "0:0:10"

    call(["streamer", "-q", "-r", fps, "-f", "rgb24", "-t", time, "-o", path + output])
