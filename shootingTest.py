import RPi.GPIO as GPIO
import time
import adafruitMotorshield
#GPOI.setmode(GPIO.BCM)
mode = GPIO.getmode()
shield=adafruitMotorshield.AdafruitMotorShield()
shield.createDCMotor()
#GPIO12
switch=12
GPIO.setup(switch, GPIO.IN,GPIO.PUD_DOWN)

try:
    while True:
        print(GPIO.input(switch))
except KeyboardInterrupt:
    pass

GPIO.cleanup()
print('stop')
#while not GPIO.input(switch):
    #shield.adafruitDCMotor.backward()

#shield.adafruitDCMotor.stop()
