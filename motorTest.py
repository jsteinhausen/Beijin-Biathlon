import adafruitMotorshield
import time

shield=AdafruitMotorshield()
shield.createDCMotor()

shield.dcMotor.forward()
time.sleep(2)
shield.dcMotor.stop()