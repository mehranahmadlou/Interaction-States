from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

camera.start_preview()
camera.start_recording('/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Experiment/1118866_24022021/SC_MLR/Experiment_1118866_SCtoMLR_NoOpto_Novelwhiteblue_6.h264', bitrate=10000000)

sleep(120)
camera.stop_recording()
camera.stop_preview()