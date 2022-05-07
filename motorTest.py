import adafruitMotorshield
import time

shield=adafruitMotorshield.AdafruitMotorShield()
shield.createDCMotor()

shield.adafruitDCMotor.dcMotor.forward()
time.sleep(2)
shield.adafruitDCMotor.dcMotor.stop()