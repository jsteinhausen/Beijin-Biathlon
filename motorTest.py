import adafruitMotorshield
from adafruitMotorshield import AdafruitMotorShield
import time

shield=adafruitMotorshield.AdafruitMotorshield()
shield.createDCMotor()

shield.adafruitDCMotor.dcMotor.forward()
time.sleep(2)
shield.adafruitDCMotor.dcMotor.stop()