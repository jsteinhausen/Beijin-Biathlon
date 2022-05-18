
import adafruitMotorshield
import time

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createDCMotor()
shield.adafruitDCMotor.forward()
time.sleep(2)
shield.adafruitDCMotor.stop()