from time import sleep

import RPi.GPIO as gp


gp.setmode(gp.BOARD)
gp.setup(16,gp.OUT)
gp.output(16,True)
sleep(60)
gp.out(16,False)