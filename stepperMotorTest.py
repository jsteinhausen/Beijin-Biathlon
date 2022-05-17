import adafruitMotorshield
import time

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createStepperMotor(1.8,65,0.1)
<<<<<<< HEAD
shield.adafruitStepperMotor.stepperSpeed=0.004
=======
shield.adafruitStepperMotor.stepperSpeed=0.005
>>>>>>> cd541c88788989155440ba83b4d80a83f46c381b

#for i in range(shield.adafruitStepperMotor.distance2steps(100)):

shield.adafruitStepperMotor.moveDistance(-100)
    #0.001 is perfect
    #0.0009 is stable
    #0.0008 is stable


shield.adafruitStepperMotor.stepperMotor.release()
print(shield.adafruitStepperMotor.stepsMade)
print(shield.adafruitStepperMotor.distanceTraveled)