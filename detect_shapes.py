# import the necessary packages
import targethelper
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"])
#image = cv2.flip(image, 1)
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
circles=[]
 #loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	#M containing all non zero values
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) )
	cY = int((M["m01"] / M["m00"]) )
	# multiply the contour (x, y)-coordinates by the resize ratio,
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	shape = sd.detect(c)
	if shape=='circle':
		circles.append(targethelper.Circle(cX,cY))
	# then draw the contours and the name of the shape on the image
	cX = int(cX*ratio)
	cY = int(cY*ratio)

	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
	# show the output image
	cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
	cv2.imshow('custom window', image)
	cv2.resizeWindow('custom window', 400, 400)
	key = cv2.waitKey(0)

#x 300 y 400
#big X 185 (115)j Y 285 (115)j
def myFunc(e):
  return e.x
#circles.sort(key=myFunc)
tolerance=0.05
#circles[0].y=110
tg=targethelper.Target(400,300,tolerance,105,105,185,285)
tg1=targethelper.Target(400,300,tolerance,115,115,185,285)
#small x 105 (195)j y 105 (195)j
obj=False
inv=False
obj,inv =tg.is_this_targent(circles)
obj2,inv2 =tg1.is_this_targent(circles)


cv2.destroyAllWindows()