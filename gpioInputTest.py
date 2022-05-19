import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
switch=6
GPIO.setup(switch, GPIO.IN,GPIO.PUD_DOWN)

try:
    while True:
        print(GPIO.input(switch))
except KeyboardInterrupt:
    pass
GPIO.cleanup()
print('stop')