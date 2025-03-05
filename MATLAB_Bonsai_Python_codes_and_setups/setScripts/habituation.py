from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25


camera.start_preview()
camera.start_recording('/home/pi/Desktop/test.h264', bitrate=10000000)

sleep(60)
camera.stop_recording()
camera.stop_preview() 