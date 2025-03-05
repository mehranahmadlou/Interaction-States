import RPi.GPIO as GPIO
import time
import datetime
from time import sleep
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.IN)
loom_chan = 19

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

movie_directory = '/home/pi/Desktop/test.h264'
camera.start_preview()
camera.start_recording(movie_directory, bitrate=10000000)
movie_s = datetime.datetime.now()
movie_start = [datetime.datetime.now(), "movie_start"]

prevstate_second = False
currstate_second = False

with open(movie_directory + "opto_loom_1.txt", "a") as text_second:
    text_second.write(str(movie_start))
    for i in range(6000):
        time.sleep(0.01)
        prevstate_second = currstate_second
        currstate_second = GPIO.input(loom_chan)
        if currstate_second != prevstate_second:
            newstate_second = "1" if currstate_second else "0"
            print("Input from infrared %s is %s" % (loom_chan, newstate_second))
            values_second = [datetime.datetime.now(), newstate_second]
            text_second.write(str(values_second))
sleep(5)
camera.stop_recording()
camera.stop_preview()