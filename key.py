#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
led_pin = 24
GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( led_pin,GPIO.OUT )
exec="/var/www/exec.txt"
while 1:
    file=open(exec,'r')
    tmp=file.read()
    file.close()
    if tmp=="key":
        print("key")
        file=open(exec,'w')
        file.close()
        GPIO.output(led_pin,True)
        time.sleep(3)
        GPIO.output(led_pin,False)
    time.sleep(1)
