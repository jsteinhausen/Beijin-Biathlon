# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import adafruitMotorshield
import time
import RPi.GPIO as GPIO
import math
import servo
import targethelper
import imutils
import cv2

import ultrasound
from pyimagesearch.shapedetector import ShapeDetector
import adafruitMotorshield


shield = adafruitMotorshield.AdafruitMotorShield()
shield.createDCMotor()
shield.createStepperMotor(1.8,65,0.1)
sensor_ultrasound=ultrasound.Ultrasound(22,23)
switch=4
button=6
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
GPIO.add_event_detect(switch, GPIO.RISING, bouncetime=200)
servo45 = servo.Servo45(13, 50)
servo360 = servo.Servo360(12, 50)
DISTANCES2TAGETS_X = [1000, 1800, 250]
DISTANCE_FRONT2CAMERA=100
DISTANCE_FRONT2GUN=200
VELOCITY=5
G=9.81
running = False
global i

def cut_out(im,distance):
    #reglage ultrasound to rail
    distance+=55
    if (1400<=distance<=1600):
        im_out = im[190:360,280:400, :]
        im_out = im_out[:, :, ::-1]
        return im_out
    elif (900<=distance<=1100):
        im_out = im[100:400,230:440, :]
        im_out = im_out[:, :, ::-1]
        return im_out
    elif (650<=distance<=850):
        im_out = im[0:400, 150:450, :]
        im_out = im_out[:, :, ::-1]
        return im_out
    else:
        return im

def cop(im,border):
    im_out = im[border:im.shape[0] - border, border:im.shape[1] - border, :]
    im_out = im_out[:, :, ::-1]
    return im_out

def object_detect(image):
    tolerance = 0.25
    # circles[0].y=110
    targets = []
    targets.append(targethelper.Target(400, 300, tolerance, 105, 105, 185, 285))
    targets.append(targethelper.Target(400, 300, tolerance, 150, 110, 150, 290))
    # image = cv2.flip(image, 1)
    resized = imutils.resize(image, width=300, height=400)
    ratio = image.shape[0] / float(resized.shape[0])
    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY_INV)[1]
    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()
    circles = []
    # loop over the contours
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        # M containing all non zero values
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        # multiply the contour (x, y)-coordinates by the resize ratio,
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        shape = sd.detect(c)
        if shape == 'circle':
            circles.append(targethelper.Circle(cX, cY))
        # then draw the contours and the name of the shape on the image
    # x 300 y 400
    # big X 185 (115)j Y 285 (115)j
    # circles.sort(key=myFunc)


    # small x 105 (195)j y 105 (195)j

    for i in range(len(targets)):
        ret=False
        if targets[i].is_this_targent(circles)[0]:
            actual_target=targets[i]
            if targets[i].is_this_targent(circles)[1]:
                actual_target=targets[i].get_inv_target()
            return actual_target
        else:
            return targethelper.Target(400, 300, tolerance, 105, 105, 185, 285)


def take_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    #frame=cv2.flip(frame,0)
    frame=cv2.imread('image0.jpg')
    return ret, frame

def get_target():
    ret, frame= take_image()
    im= cut_out(frame,750)#sensor_ultrasound.median_dist()

    return object_detect(im)

def init_shoot():
    while GPIO.input(switch) == 0:
        shield.adafruitDCMotor.forward()
    shield.adafruitDCMotor.stop()

def shoot():
    #shield.adafruitDCMotor.forward()
    time.sleep(1)
    #while GPIO.input(switch) == 0:
        #print(GPIO.input(switch))
        #shield.adafruitDCMotor.backward()

    #shield.adafruitDCMotor.stop()

def shooting_release():
    shield.adafruitDCMotor.backward()
    time.sleep(1)
    GPIO.cleanup()

def recharge_gun():
    servo45.turn_to_angle(45)
    time.sleep(5)
    servo360.turn_to_angle(100)


def move_gun2angle(distance_z,distance_y):
    #conversion from mm to m
    distance_z=750
    distance_z/=1000
    distance_y/=1000
    lam=(VELOCITY^2)/(G*distance_z)
    tanA=(distance_y-0.08)/distance_z
    angle=math.atan((lam-(math.sqrt((pow(lam,2)-1-(2*lam*tanA))))))
    if angle<=45:
        servo45.turn_to_angle(angle)
    else:
        servo45.turn_to_angle(45)
    time.sleep(1)

try:
    init_shoot()
    recharge_gun()
    #recharge_gun()
    for i in range(1):
        shield.adafruitStepperMotor.movetodistance(DISTANCES2TAGETS_X[i])
        shield.adafruitStepperMotor.stepperMotor.release()
        target=get_target()
        if target.circle_high.x==target.width/2:
            shield.adafruitStepperMotor.moveDistance(DISTANCE_FRONT2GUN)
            move_gun2angle(sensor_ultrasound.median_dist(),target.circle_high.y)
            shoot()
            recharge_gun()
            move_gun2angle(sensor_ultrasound.median_dist(), target.circle_low.y)
            recharge_gun()
        else:
            shield.adafruitStepperMotor.moveDistance(-(target.width/2-105))
            if target.inv:
                move_gun2angle(sensor_ultrasound.median_dist(), target.circle_high.y)
                shoot()
            else:
                move_gun2angle(move_gun2angle(sensor_ultrasound.median_dist(), target.circle_low.y))
                shoot()
            recharge_gun()
            shield.adafruitStepperMotor.moveDistance((185-105))
            if target.inv:
                move_gun2angle(sensor_ultrasound.median_dist(), target.circle_low.y)
                shoot()
            else:
                move_gun2angle(move_gun2angle(sensor_ultrasound.median_dist(), target.circle_high.y))
                shoot()

            recharge_gun()
except KeyboardInterrupt:
    pass
#except TypeError:
    #pass
shield.adafruitDCMotor.stop()
shield.adafruitStepperMotor.steppperMotor.release()
GPIO.cleanup()














# See PyCharm help at https://www.jetbrains.com/help/pycharm/
