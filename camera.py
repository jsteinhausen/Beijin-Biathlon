import cv2

cap = cv2.VideoCapture(0)

# Capture frame
for i in range(3):
	ret, frame = cap.read()
	if ret:
		cv2.imwrite('image'+str(i)+'.jpg', frame)
		print("True")

	cap.release()