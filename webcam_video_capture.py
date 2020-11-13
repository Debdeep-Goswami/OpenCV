
'''______________________________________________________________________________________
	This is a simple python program to Capture and Display video from a web cam
	
	Simplified by	:-	Debdeep Goswami
	
_______________________________________________________________________________________'''
		
import cv2,time

# 1. Create an object to capture the video
video=cv2.VideoCapture(0)


#8. Loop to Display continuous frames	
while True:

	# 2. Create a frame object
	check, frame=video.read()


	# 3. Displaying the frame as output
	cv2.imshow("Capturing",frame)


	# 4. For playing as video
	key=cv2.waitKey(1)


	# 5. To Stop the capturing ( Press q to exit )
	if key == ord('q'):
		break


# 6. Shutdown the camera
video.release()


# 7.Exit all screens
cv2.destroyAllWindows()
