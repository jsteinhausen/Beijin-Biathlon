import adafruitMotorshield
import time

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createStepperMotor(1.8,6,((1.8/8)*6))

for i in range(shield.adafruitStepperMotor.distance2steps(10)):
    shield.adafruitStepperMotor.oneStepForward()
    time.sleep(2)

print(shield.adafruitStepperMotor.stepsMade)
print(shield.adafruitStepperMotor.distanceTraveled)