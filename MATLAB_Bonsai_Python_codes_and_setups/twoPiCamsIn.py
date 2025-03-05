from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import time
import datetime

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.cleanup()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN)


camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25


while not GPIO.input(26):
    print("waiting")
    

camera.start_preview()
camera.start_recording('/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Opto_Behaviour/1122864_sertMRN_ACR2_20012022/OneNovelOneOld/Opto_NovelObject_AllOld_6xx_cam2.h264', bitrate=10000000)

#GPIO.cleanup()

#camera.stop_recording()
#camera.stop_preview()


# while GPIO.input(26):
#     sleep
#     
# while GPIO.input(26):
#     sleep
#     
# while GPIO.input(26):
#     sleep
    


#GPIO.cleanup()
