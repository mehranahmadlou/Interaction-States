from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

camera.start_preview()
camera.start_recording('/home/pi/swc/mrsic_flogel/public/projects/MeAhetal_20210211_Optogenetics_Behavior/Self_Stimulation/NewSetUp/1125771xx/movie1.h264', bitrate=10000000)
#camera.start_recording('/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Opto_Behaviour/1118863_26042021/Experiment_1118863_PostTMTnoopto_24.h264', bitrate=10000000)
# Experiment_1110500_manualopto_2
sleep(3600)

camera.stop_recording()
camera.stop_preview()
