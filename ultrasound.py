import RPi.GPIO as gp
from time import sleep,time


class Ultrasound:

    def __init__(self,pin_in,pin_out):
        self.pin_in=pin_in
        self.pin_out=pin_out
        gp.setmode(gp.BOARD)
        gp.setup(self.pin_out, gp.OUT)
        gp.setup(self.pin_in, gp.IN)
        sleep(1)
        gp.output(self.pin_out, gp.LOW)
        sleep(0.000002)
        global st, sto

    def distance(self):
        gp.output(16, gp.HIGH)  #initialisation du capteur
        sleep(0.00001)
        gp.output(16, gp.LOW)
        while gp.input(15) == 0:
            st = time()         #start time of the impulsion
            # print(st,"\n")
        while gp.input(15) == 1:
            sto = time()        #stop time of the impulsion
            #print(sto)
            tt = sto - st
            dist = (tt * 351240) / 2  # ici la vitesse du son et donné en cm/s et donc dist en cm
            dist = round(dist, 3)    #rounding nach dem dritten zahl nach dem komma ?
            #print("distance est de", dist)
        return dist


