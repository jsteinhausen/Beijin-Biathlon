import board
from adafruit_motorkit import MotorKit
#kit = MotorKit(i2c=board.I2C())

class AdafruitDCMotor:
    motorSpeed=1.0
    def __init__(self):
        kit = MotorKit(i2c=board.I2C())
        #Uses the first motor of the motor kit as a default
        self.dcMotor=kit.motor3

        self.dcMotor.throttle = 0


    #Holds the motor in a certain position
    def stop(self):
        self.dcMotor.throttle = 0

    #Max Speed is 1
    def setMotorDCSpeed(self,motorSpeed):
        self.motorSpeed=motorSpeed

    def forward(self):
        self.dcMotor.throttle = self.motorSpeed

    def backward(self):
        self.dcMotor.throttle=-self.motorSpeed

    #The motor can be moved without any resistance
    def release(self):
        self.dcMotor.throttle= None



    """Using adafruit_motorkit with a stepper motor"""
class AdafruitStepper:

    distanceTraveled=0
    stepsMade = 0.0
    def __init__(self,distanceOneStep,distanceOneMicrostep):
        #This Attribute needs to be calculate with the size of the Wheel
        self.distanceOneStep=distanceOneStep
        #Attributes is the result of distanceOneStep by 8
        self.distanceOneMicrostep=distanceOneMicrostep

        self.stepperMotor=self.kit.stepper1
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


