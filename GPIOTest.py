import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
led=11
GPIO.setup(led, GPIO.OUT,initial=GPIO.LOW)

#LED ON
GPIO.output(led, GPIO.HIGH)
time.sleep(2)
#LED OFF
GPIO.output(led, GPIO.LOW)
time.sleep(2)
