#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
led_pin = 24
GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( led_pin,GPIO.OUT )

GPIO.output(led_pin,True)
time.sleep(2)
GPIO.output(led_pin,False)
