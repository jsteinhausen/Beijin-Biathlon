# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import adafruitMotorshield
import time

import targethelper
import imutils
import cv2
from pyimagesearch.shapedetector import ShapeDetector
import numpy as np


def cut_out(im,distance):
    if targethelper.Target.test_cord(140,160,distance):
        im_out = im[220:380,275:380, :]
        im_out = im_out[:, :, ::-1]
        return im_out

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
        if targets[i].is_this_targent(circles)[0]:
            actual_target=targets[i]
            if targets[i].is_this_targent(circles)[1]:
                actual_target=targets[i].get_inv_target()
    return actual_target


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
