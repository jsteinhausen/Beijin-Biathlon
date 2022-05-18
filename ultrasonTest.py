import RPi
from ultrasound import Ultrasound

sensor=Ultrasound(15, 16)
try:

 print(sensor.median_dist())
except KeyboardInterrupt:
  pass
RPi.GPIO.cleanup()