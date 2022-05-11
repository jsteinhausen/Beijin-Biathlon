import time

import adafruit_motor.stepper
import board
from adafruit_motorkit import MotorKit


class AdafruitMotorShield:
    def __init__(self):
        self.kit = MotorKit(i2c=board.I2C())

    def createDCMotor(self):
        self.adafruitDCMotor=AdafruitDCMotor(self)


    def createStepperMotor(self,stepAngle,diametre,distanceOneMicrostep):
        self.adafruitStepperMotor=AdafruitStepper(self,stepAngle,diametre,distanceOneMicrostep)

class AdafruitDCMotor:
    motorSpeed=1.0
    def __init__(self,adafruitMotorShield):
        #Uses the first motor of the motor kit as a default
        self.dcMotor=adafruitMotorShield.kit.motor3

        self.dcMotor.throttle = 0


    #Holds the motor in a certain position
    def stop(self):
        self.dcMotor.throttle = 0

    #Max Speed is 1
    def setMotorDCSpeed(self,motorSpeed):
        self.dcMotor=motorSpeed

    def forward(self):
        self.dcMotor.throttle = self.motorSpeed

    def backward(self):
        self.dcMotor.throttle=-self.motorSpeed

    #The motor can be moved without any resistance
    def release(self):
        self.dcMotor.throttle= None



    """Using adafruit_motorkit with a stepper motor"""
class AdafruitStepper:
    DEFAULT_STEPPER_SPEED=0.001
    stepperSpeed=DEFAULT_STEPPER_SPEED
    distanceTraveled=0
    stepsMade = 0.0
    def __init__(self,adafruitMotorShield,stepAngle,diametre,distanceOneMicrostep):
        #This Attribute needs to be calculate with the size of the Wheel
        self.distanceOneStep=stepAngle*diametre
        self.nbStepsRound=360/stepAngle
        #Attributes is the result of distanceOneStep by 8
        self.distanceOneMicrostep=distanceOneMicrostep
        self.stepperMotor=adafruitMotorShield.kit.stepper1
        self.stepperMotor.release()
        self.stepper=adafruit_motor.stepper
        self.stepperMotorStyle=self.stepper.SINGLE

    def oneStepForward(self):
        self.stepperMotor.onestep(direction=self.stepper.FORWARD,style=self.stepperMotorStyle)
        self.distanceTraveled+=self.distanceOneStep
        self.stepsMade+=1

    def oneStepBackward(self):
        self.stepperMotor.onestep(direction=self.stepper.BACKWARD,style=self.stepperMotorStyle)
        self.distanceTraveled-=self.distanceOneStep
        self.stepsMade+=1

    def oneMicroStepForward(self):
        self.stepperMotor.onestep(direction=self.stepper.FORWARD,style=self.MICROSTEP)
        self.distanceTraveled+=self.distanceOneMicrostep
        self.stepsMade+=0.125

    def oneMicroStepBackward(self):
        self.stepperMotor.onestep(direction=self.stepper.BACKWARD,style=self.MICROSTEP)
        self.distanceTraveled-=self.distanceOneMicrostep
        self.stepsMade+=0.125

    def resetDistanceTraveled(self):
        self.distanceTraveled=0

    def resetstepsMade(self):
        self.stepsMade=0
    def distance2steps (self,distance):
        #print('calcul distance en angle')
        nbSteps=(round(distance/self.distanceOneStep))
        print('For distance '+ str(distance)+ ' the stepper needs ' +str(nbSteps)+ ' steps')
        return nbSteps
    def moveDistance(self,distance):
        nbSteps=self.distance2steps(distance)
        if nbSteps>=0:
            for i in range(abs(nbSteps)):
                self.oneStepForward()
                time.sleep(self.stepperSpeed)
        else:
            for i in range(abs(nbSteps)):
                self.oneStepBackward()
                time.sleep(self.stepperSpeed)

    def changeSpeed(self,speed):
        if speed>=self.DEFAULT_STEPPER_SPEED:
            self.stepperSpeed=speed
        else:
            self.DEFAULT_STEPPER_SPEED








