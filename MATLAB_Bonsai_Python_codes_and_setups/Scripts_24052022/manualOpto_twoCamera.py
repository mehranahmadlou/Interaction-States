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
GPIO.setup(23, GPIO.OUT)

camera.start_preview()
camera.start_recording('/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Opto_Behaviour/1121913_mPFCMRN_ACR2/Manual_Opto_1xx.h264', bitrate=10000000)
#camera.start_recording('/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Opto_Behaviour/1118863_26042021/Experiment_1118863_PostTMTnoopto_24.h264', bitrate=10000000)
# Experiment_1110500_manualopto_2
GPIO.output(11, 1)
GPIO.output(23, 1)

sleep(300)

GPIO.output(11, 0)
GPIO.output(23, 0)

GPIO.cleanup()

camera.stop_recording()
camera.stop_preview()
