import adafruitMotorshield
import time

testDcMotor=adafruitMotorshield.AdafruitDCMotor()

testDcMotor.forward()
time.sleep(2)
testDcMotor.stop()