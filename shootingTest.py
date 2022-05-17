import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
switch=12
GPIO.setup(switch, GPIO.IN)

while True:
    print(GPIO.input(switch))
