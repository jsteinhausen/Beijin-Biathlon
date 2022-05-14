import RPi.GPIO as gp


gp.setmode(gp.BOARD)
gp.setup(16,gp.OUT)
gp.setup(15,gp.IN)
gp.output(16,True)