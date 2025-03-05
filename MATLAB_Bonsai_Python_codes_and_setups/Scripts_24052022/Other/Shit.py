import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

camera.start_preview()
camera.start_recording('/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Experiment/1118865_22022021/SC_ZIST/Experiment_1118865_SCtoZIST_opto_bigobject_L15_13.h264', bitrate=10000000)

pwm.start(0)

for dc in range(40):
    pwm.ChangeDutyCycle(50)
    sleep(2)
    pwm.ChangeDutyCycle(0)
    sleep(1)
    
pwm.stop(0)

camera.stop_recording()
camera.stop_preview()
