import board
from adafruit_motorkit import MotorKit

class AdafruitMotorShield:
    def __init__(self):
        self.kit = MotorKit(i2c=board.I2C())

    def createDCMotor(self):
        AdafruitDCMotor()


    def createStepperMotor(self):
        self.stepperMotor=AdafruitStepper()
        return self.stepperMotor


class AdafruitDCMotor(AdafruitMotorShield):
    motorSpeed=1.0
    def __init__(self):
        #Uses the first motor of the motor kit as a default
        self.parent.dcMotor=self.parent.kit.motor3

        self.parent.dcMotor.throttle = 0


    #Holds the motor in a certain position
    def stop(self):
        self.parent.dcMotor.throttle = 0

    #Max Speed is 1
    def setMotorDCSpeed(self,motorSpeed):
        self.parent.dcMotor=motorSpeed

    def forward(self):
        self.parent.dcMotor.throttle = self.motorSpeed

    def backward(self):
        self.parent.dcMotor.throttle=-self.motorSpeed

    #The motor can be moved without any resistance
    def release(self):
        self.parent.dcMotor.throttle= None



    """Using adafruit_motorkit with a stepper motor"""
class AdafruitStepper(AdafruitMotorShield):

    distanceTraveled=0
    stepsMade = 0.0
    def __init__(self,distanceOneStep,distanceOneMicrostep):
        #This Attribute needs to be calculate with the size of the Wheel
        self.distanceOneStep=distanceOneStep
        #Attributes is the result of distanceOneStep by 8
        self.distanceOneMicrostep=distanceOneMicrostep

        self.stepperMotor=self.parent.kit.stepper1

        self.stepperMotor.release()
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

    def resetDistanceTraveled(self):
        self.stepsMade=0


