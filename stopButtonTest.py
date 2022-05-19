import RPi.GPIO as GPIO
import time

import adafruitMotorshield

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createStepperMotor(1.8,65,0.1)
shield.adafruitStepperMotor.stepperSpeed=0.005
#GPIO.setmode(GPIO.BCM)
switch=6
GPIO.setup(switch, GPIO.IN,GPIO.PUD_DOWN)
GPIO.add_event_detect(switch, GPIO.RISING,bouncetime=200)
button=False

try:
    while True:
        if button:
            shield.adafruitStepperMotor.moveDistance(10)
        else:
            shield.adafruitStepperMotor.stepperMotor.release()

        print('Button'+str(button))
        print(GPIO.input(switch))
        if GPIO.event_detected(switch):
            print('Button pressed')
            if button:
                button=False
            else:
                button=True
except KeyboardInterrupt:
    pass
shield.adafruitStepperMotor.stepperMotor.release()
GPIO.cleanup()
print('stop')