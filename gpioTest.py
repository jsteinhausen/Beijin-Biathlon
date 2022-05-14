import RPi.GPIO as gp


gp.setmode(gp.BOARD)
gp.setup(36,gp.OUT)
gp.output(36,True)