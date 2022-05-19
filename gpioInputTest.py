import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
switch=6
GPIO.setup(switch, GPIO.IN,GPIO.PUD_DOWN)

#LED ON
GPIO.output(switch, GPIO.HIGH)
try:
    while True:
        print(GPIO.input(switch))
except KeyboardInterrupt:
    pass
GPIO.cleanup()
print('stop')