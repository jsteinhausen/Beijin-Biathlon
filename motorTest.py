import adafruitMotorshield
import time

shield=adafruitMotorshield.AdafruitMotorshield()
shield.createDCMotor()

shield.dcMotor.forward()
time.sleep(2)
shield.dcMotor.stop()