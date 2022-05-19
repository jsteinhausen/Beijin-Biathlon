import RPi.GPIO as GPIO
import time
import servo

try:
    servo45 = servo.Servo45(13, 50)
    servo45.turn_to_angle(90)

    #servo360 = servo.Servo360(12, 50)
    #servo360.turn_to_angle(180)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
#servoPIN = 13

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)

#p = GPIO.PWM(servoPIN, 50)  # GPIO 12 for PWM with 50Hz
#p.start(2.5)  # Initialization


# ChangeDutyCycle(5) 5 steht fuer pulsweite von 5% von 20ms (f=50Hz)
# 5% -> 0°
# 10% -> 90° (maxwert von verwendetem servo)

#def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
 #   leftSpan = leftMax - leftMin
  #  rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
   # valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    #return rightMin + (valueScaled * rightSpan)


#angle = 18 # winkel von 0 bis 45° eingeben
#pwnPercent = translate(45-angle, 0.0, 45.0, 5.0, 10.0)
#print(pwnPercent)

#try:
    #while True:
    #p.ChangeDutyCycle(pwnPercent)
    #time.sleep(0.5)
#except KeyboardInterrupt:
 #   p.stop()
