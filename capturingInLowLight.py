import picamera
from time import sleep
from fractions import Fraction

with picamera.PiCamera() as camera:
	camera.resolution = (1280,720)
	camera.framerate = Fraction(1,6)
	camera.shutter_speed = 6000000
	camera.exposure_mode = 'off'
	camera.iso = 800
	sleep(10)
	camera.capture('dark.jpg')
