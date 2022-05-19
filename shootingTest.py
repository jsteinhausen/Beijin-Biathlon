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

def init_shoot():
    while GPIO.input(switch)==0:
        shield.adafruitDCMotor.backward()


def shoot():
    shield.adafruitDCMotor.backward()
    time.sleep(1)
    while GPIO.input(switch) == 0:
        print(GPIO.input(switch))
        shield.adafruitDCMotor.backward()

    shield.adafruitDCMotor.stop()

def shooting_release():
    shield.adafruitDCMotor.forward()
    time.sleep(1)
    GPIO.cleanup()




try:
    while GPIO.input(switch)==0:
        shield.adafruitDCMotor.backward()
    shield.adafruitDCMotor.stop()
    shoot()
    release()
    print(GPIO.input(switch))
except KeyboardInterrupt:
    pass
shield.adafruitDCMotor.stop()
GPIO.cleanup()
print('stop')
#while not GPIO.input(switch):
    #shield.adafruitDCMotor.backward()

#shield.adafruitDCMotor.stop()
