import adafruitMotorshield
import time

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createStepperMotor(1.8,65,0.1)
shield.adafruitStepperMotor.stepperSpeed=0.008

#for i in range(shield.adafruitStepperMotor.distance2steps(100)):

shield.adafruitStepperMotor.moveDistance(-100)
    #0.001 is perfect
    #0.0009 is stable
    #0.0008 is stable


shield.adafruitStepperMotor.stepperMotor.release()
print(shield.adafruitStepperMotor.stepsMade)
print(shield.adafruitStepperMotor.distanceTraveled)