import picamera
from time import sleep
with picamera.PiCamera() as camera:
	camera.resolution=(640,480)
	camera.start_preview()
	camera.start_recording('/home/pi/video.h264')
	sleep(10)
	camera.stop_recording()
	camera.stop_preview()
