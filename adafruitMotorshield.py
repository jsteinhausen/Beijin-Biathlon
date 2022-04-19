import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

kit.motor1.throttle = 1.0
time.sleep(0.5)
kit.motor1.throttle = 0

"""Simple test for using adafruit_motorkit with a stepper motor"""

for i in range(100):
    kit.stepper1.onestep()
    time.sleep(0.01)