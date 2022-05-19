import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self,PIN,PWM):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        self.p = GPIO.PWM(PIN, PWM)
        self.p.start(2.0)

    def translate(self,value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    #speed entre 5 et 10
    def turn_to_angle(self,angle):
        t = True
        pwnPercent = self.translate(angle, 0.0, 180, 5.0, 10.0)
        self.p.ChangeDutyCycle(pwnPercent)
        time.sleep(0.14)


        #time.sleep(0.5)
        #return pwnPercent



# ChangeDutyCycle(5) 5 steht fuer pulsweite von 5% von 20ms (f=50Hz)
# 5% -> 0°
# 10% -> 90° (maxwert von verwendetem servo)