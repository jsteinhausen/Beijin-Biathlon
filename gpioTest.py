import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=5
GPIO.setup(led, GPIO.OUT,initial=GPIO.LOW)
try:
    #LED ON
    GPIO.output(led, GPIO.HIGH)
    time.sleep(60)
    #LED OFF
    GPIO.output(led, GPIO.LOW)
    time.sleep(2)
except KeyboardInterrupt:
    pass
GPIO.cleanup()

