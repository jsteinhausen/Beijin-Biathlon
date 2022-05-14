import RPi.GPIO as gp


gp.setmode(gp.BOARD)
gp.setup(16,gp.OUT)
gp.output(16,True)