#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
freq=50
pwm = GPIO.PWM(16, freq)
leftPosition = 0.75
rightPosition = 2.5
middlePosition = (rightPosition - leftPosition) /2 + leftPosition
positionlist = [leftPosition, middlePosition, rightPosition, middlePosition]
ms=1000/freq
dutyCyclePercentage=positionlist[0]*100/ms
pwm.start(dutyCyclePercentage)
time.sleep(1)
#dutyCyclePercentage=positionlist[1]*100/ms
#pwm.start(dutyCyclePercentage)
#time.sleep(1)
dutyCyclePercentage=positionlist[2]*100/ms
pwm.start(dutyCyclePercentage)
time.sleep(1)
pwm.stop()

GPIO.cleanup()
