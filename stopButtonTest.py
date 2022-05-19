import RPi.GPIO as GPIO
import time

import adafruitMotorshield

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createStepperMotor(1.8,65,0.1)
shield.adafruitStepperMotor.stepperSpeed=0.05
#GPIO.setmode(GPIO.BCM)
switch=6
GPIO.setup(switch, GPIO.IN,GPIO.PUD_DOWN)
GPIO.add_event_detect(switch, GPIO.RISING)

try:
    while True:
        shield.adafruitStepperMotor.oneStepForward()
        print(GPIO.input(switch))
        #if GPIO.event_detected(switch):
            #print('Button pressed')
            #shield.adafruitStepperMotor.oneStepBackward()
except KeyboardInterrupt:
    pass
shield.adafruitStepperMotor.stepperMotor.release()
GPIO.cleanup()
print('stop')