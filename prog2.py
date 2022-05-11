

import board
import time
import busio
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit



kit = MotorKit(i2c=board.I2C())

kit.stepper1.release()

speed = 3
distance1=0
distance_in = 30
distance_out = 1909
nb_steps=0
nbpas =0
nb_stepscounter=0
nb_tours = 0
shoot_end = False
bande=30

class Prog1:
    
    #speed = 3
    #distance1=0
    #distance_in = 30
    #distance_out = 1909
    #nb_steps=0
    #nbpas =0
    #nb_stepscounter=0
    #nb_tours = 0
    #shoot_end = False
    #bande=30
    
    def parcours (distance):
        global nb_tours
        global distance_out
        #print('calcul distance en angle')
        nb_tours=distance/0.18849
        distance_out=nb_tours*360
        nb_steps=(round(distance_out/1.8))
        print('nb de steps parcouru', nb_steps)
        return nb_steps
    
    def counter(steps):
        global nb_stepscounter
        global nb_steps
        
        #if steps>=0:
        nb_stepscounter = nb_stepscounter + steps
        print('totale de pas effectué au tot',nb_stepscounter)
        #else:
            #nb_stepscounter = nb_stepscounter - steps
            #print('totale de pas effectué négatif',nb_stepscounter)
        
        return nb_stepscounter
       
    def direction(nbpas):
        #global distance1
        #nbpas = parcours(-1)
    #pour dire au moteur combien de step il doit faire en fct de la distance
        if nbpas>=0:
            for i in range(abs(nbpas)): 
                kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                time.sleep(0.002)
        else:
            for i in range(abs(nbpas)): 
                kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                time.sleep(0.002)
        
    
    direction(parcours(2))
    counter(parcours(2))
    
    #nb_stepscounter = nbpas + nb_stepscounter
    #print('graduation',nb_stepscounter)    
        
    while shoot_end == False :
            time.sleep(3)
            kit.stepper1.release()
            shoot_end = True
            
    shoot_end=False #condition venant du detecteur de position de tir
    #nbpas = parcours(0.05)                    
    #for i in range(nbpas):
        #kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        #time.sleep(0.001)
    direction(parcours(-3))
    counter(parcours(-3))
    
    #nb_stepscounter = nbpas + nb_stepscounter
    #print('graduation',nb_stepscounter)
    
    while shoot_end == False :
            time.sleep(3)
            kit.stepper1.release()
            shoot_end = True
            
    shoot_end=False #condition venant du detecteur de position de tir
    
    direction(parcours(0.5))
    counter(parcours(0.5))
    #for i in range(parcours(0.8)+round(0.05)):
        #kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        #time.sleep(0.001)
    
    
    if bande>=30:
        kit.stepper1.release()
    else:
        print('ça marche pas')
        for i in range(parcours(0.2)):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            time.sleep(0.0008)
 