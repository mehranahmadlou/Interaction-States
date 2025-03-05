import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import time
import datetime

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(11, 0)
GPIO.output(12, 0)
GPIO.output(23, 0)
GPIO.cleanup()