import RPi.GPIO as GPIO
import time
import adafruitMotorshield

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createDCMotor()
switch=12
GPIO.setup(switch, GPIO.IN)

while GPIO.input(switch):
    shield.adafruitDCMotor.backward()

shield.adafruitDCMotor.stop()
