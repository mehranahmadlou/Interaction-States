from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

camera.start_preview()
camera.start_recording('/home/pi/Desktop/test.h264', bitrate=10000000)

GPIO.output(12, 1)

sleep(10)

camera.stop_recording()
camera.stop_preview()
GPIO.output(12, 0)

GPIO.cleanup()