#!/usr/bin/python

import RPi.GPIO as GPIO #Importing the Raspberry Pi's GPIO pins
import time #This is so that we can include time.sleep() to let the LED rest while it's on

led = 21 #This makes the LED go to GPIO pin 21, and the cathode into the GND
Running = True # This makes the while loop keep on running

GPIO.setmode(GPIO.BCM) #This is the counting method used as default, there's plenty more
GPIO.setup(led,GPIO.OUT) #When the LED is connected to GPIO pin 21, this is the switch to turn it on and off

try: #Try this while loop, if it fails, move on
    while Running: #While running is still equal to the default method True
	print("I am now on!")
	GPIO.output(led,GPIO.HIGH)
	time.sleep(1)
	print("I am now off!")
	GPIO.output(led,GPIO.LOW)

except KeyboardInterrupt: #This makes it stop and equal to False when pressing CTRL + C
    print("I am now going to rest!")

finally: #Finally do this last step
    GPIO.cleanup() #Very important to not have code residue left over from the last launch, or it could run into problems
