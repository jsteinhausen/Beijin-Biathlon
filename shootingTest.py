import RPi.GPIO as GPIO
import time
import adafruitMotorshield

mode = GPIO.getmode()
shield=adafruitMotorshield.AdafruitMotorShield()
shield.createDCMotor()

switch=12
GPIO.setup(switch, GPIO.IN)
while True:
    print(GPIO.input(switch))
#while not GPIO.input(switch):
    #shield.adafruitDCMotor.backward()

#shield.adafruitDCMotor.stop()
