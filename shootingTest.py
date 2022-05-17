import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
switch=12
GPIO.setup(switch, GPIO.IN)

f=GPIO.input(switch)
