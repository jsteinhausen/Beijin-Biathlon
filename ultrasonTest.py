from ultrason import Ultrason

sensor=Ultrason(15,16)
while True:
  print(sensor.DistUltrason())