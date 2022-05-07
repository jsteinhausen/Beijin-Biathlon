import adafruitMotorshield
import time

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createStepperMotor(1.8,6.0,0.1)

#for i in range(shield.adafruitStepperMotor.distance2steps(100)):
while True:
    shield.adafruitStepperMotor.oneStepForward()
    #0.0009 is stable
    #0.0008
    time.sleep(0.0008)

shield.adafruitStepperMotor.stepperMotor.release()
print(shield.adafruitStepperMotor.stepsMade)
print(shield.adafruitStepperMotor.distanceTraveled)