import RPi.GPIO as gp


gp.setmode(gp.BOARD)
gp.setup(20,gp.OUT)
gp.setup(15,gp.IN)
gp.output(20,True)