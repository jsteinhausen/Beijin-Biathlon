# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board


from adafruit_motorkit import MotorKit
#i2c = busio.I2C(board.SCL, board.SDA)
kit = MotorKit(i2c=board.I2C())

kit.motor1.throttle = 0

while True:
    print("Forward!")
    kit.motor3.throttle = 0.5
    time.sleep(1)

    print("Speed up...")
    for i in range(0, 101):
        speed = i * 0.01
        kit.motor3.throttle = speed
        time.sleep(0.01)

    print("Slow down...")
    for i in range(100, -1, -1):
        speed = i * 0.01
        kit.motor3.throttle = speed
        time.sleep(0.01)

    print("Backward!")
    kit.motor3.throttle = -0.5
    time.sleep(1)

    print("Speed up...")
    for i in range(0, -101, -1):
        speed = i * 0.01
        kit.motor3.throttle = speed
        time.sleep(0.01)

    print("Slow down...")
    for i in range(-100, 1):
        speed = i * 0.01
        kit.motor3.throttle = speed
        time.sleep(0.01)

    print("Stop!")
    kit.motor3.throttle = 0
    time.sleep(1)
