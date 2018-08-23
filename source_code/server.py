#!/usr/bin/python
import socket
import threading
import glob as g
import random
import time
import math
import datetime
#Use Tkinter for Python2 and tkinter for Python3
from Tkinter import *
from PIL import Image
from PIL import ImageTk
from multiprocessing.connection import Listener
from time import gmtime, strftime, sleep

# Andrew Ray, Mitchell Powell
# Radford University

#Variables here due to global requirements for threads/gui
#Create the TK system
root = Tk()
#Get rid of the tool bar
root.overrideredirect(True)

#Create a canvas
#This will have to be updated to match the touch screen resolution
canvas_width=720
canvas_height=480
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
displayTime=time.localtime()

#Pick a random picture to display
def getImage(array, oldNum):

	size = len(array)
	random.seed()
	num = random.randrange(0,size)
	while (num == oldNum):
		num = random.randrange(0,size)
	return array[num],num

#Scale the image to the screen using ratios
def resizeImage(im):
	# Get width and height of image
	pic_width, pic_height = im.size

	# If height is scaling factor, calculate scale based on height
	if(float(pic_height)/pic_width > float(canvas_height)/canvas_width):
		scale=float(canvas_height)/pic_height
	# If width is scaling factor, calculate scale based on width
	else:
		scale=float(canvas_width)/pic_width
	# Scale the picture height and width
	# abs and ceil are used to ensure a positive non-zero number
	new_pic_height = int(math.ceil(abs(scale * pic_height)))
	new_pic_width = int(math.ceil(abs(scale * pic_width)))

	# Return the resized image
	return im.resize((new_pic_width, new_pic_height),Image.ANTIALIAS)

#Display an image on the canvas
def displayImage(fileName, canvas):
	# Load the image file
	im = Image.open(fileName)
	# Any picture other than background gets scaled
	if(fileName != "display_images/background/black.jpg"):
		im = resizeImage(im)
	# Put the image into a canvas compatible class, and stick in an
	# arbitrary variable to the garbage collector doesn't destroy it
	canvas.image = ImageTk.PhotoImage(im)
	# Add the image to the canvas, and set the anchor to the top left / north west corner
	canvas.create_image(0, 0, image=canvas.image, anchor='nw')

#Show a black image
def showBlack():
	global canvas
	displayImage("display_images/background/black.jpg", canvas)

#Callback for thread when clicked that will
#reset the screen to black after 5 seconds
def resetScreen():
	time.sleep(5)
	showBlack()

#Down here so I can use global variables
#Yes I know this is evil, but it is forced due to GUIs...
oldNum=0
init=0
def callback(event):
	#Get all of the images in the current directory
	global oldNum
	global init
	global displayTime
	go=0

	#Determine if we have a multi-fire issue and only display once every 3 seconds
	if (init ==0):
		go=1
		init=1
		displayTime=time.localtime()

	if (init==1):
		testTime = time.localtime()
		H1 = displayTime.tm_hour
		M1 = displayTime.tm_min
		S1 = displayTime.tm_sec
		H2 = testTime.tm_hour
		M2 = testTime.tm_min
		S2 = testTime.tm_sec

		diffTime=0
		if (H2 != H1 or M2 !=M1):
			diffTime=1
		elif (S2-S1 > 10):
			diffTime=1
		if (diffTime == 1):
			go=1
			displayTime = testTime
	if (go == 1):
		images = g.glob('display_images/*.jpg')
		fileName,oldNum = getImage(images, oldNum)

		#Write to disk
		logFile = "/media/pi/FEEDER_DATA/screenPictureLog.csv"
		f = open(logFile, "a+")
		record = str(displayTime.tm_year) + "," + str(displayTime.tm_mon) + "," + str(displayTime.tm_mday) + "," + str(H2) + "," + str(M2) + "," + str(S2) + "," + str(fileName)
		f.write(record)
		f.write("\n")
		f.close()
		h=open("server_out.txt", "a+")
		h.write("made it")
		h.close()

		#Put image on screen
		displayImage(fileName, canvas)
		t = threading.Thread(target=resetScreen)
		t.start()

#Setup the mouse click callback
#canvas.bind("<Button-1>", callback)

#Networking code to listen on port 12345
def createSocket():
	print("Socket created")
	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 12346                # Reserve a port for your service.
	print(s.bind((host, port)))        # Bind to the port

	print(s.listen(5))                 # Now wait for client connection.
	while True:
		c, addr = s.accept()     # Establish connection with client.

		#Hack to trigger the change of image, doesn't actually receive data
		doh=3
		print(callback(doh))		

#Setup networking in a different thread
t = threading.Thread(target=createSocket)
t.start()

#Initial image is black
showBlack()

#Start the GUI
root.mainloop()
