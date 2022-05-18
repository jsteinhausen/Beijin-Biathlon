import RPi.GPIO as GPIO
import time
import adafruitMotorshield
#GPOI.setmode(GPIO.BCM)
mode = GPIO.getmode()
shield=adafruitMotorshield.AdafruitMotorShield()
shield.createDCMotor()
#GPIO12
switch=12
GPIO.setup(switch, GPIO.IN)
while True:
    print(GPIO.input(switch))
#while not GPIO.input(switch):
    #shield.adafruitDCMotor.backward()

#shield.adafruitDCMotor.stop()
