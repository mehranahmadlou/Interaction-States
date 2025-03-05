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
GPIO.setup(11, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

laser = 5
opto_pulse_duration = 4.7 #2.2
opto_repeat = 24 #48
ISI = 0.3
prestimulus = 0
after_opto = 120
movie_duration = (opto_pulse_duration + ISI) * opto_repeat + prestimulus + after_opto
movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAhetal_20210211_Optogenetics_Behavior/Explore_Exploit_Objects/ON/11268xx/AllNovelObjects_Opto_4.h264'
# projection = 'VGAT MRN ChR2'
projection = 'LHb MRN eNpHR3.0'
# 'AllNovelObjects_Opto_1'

camera.start_preview()
camera.start_recording(movie_directory, bitrate=10000000)
GPIO.output(11, 1)
GPIO.output(23, 1)

sleep(prestimulus)

pwm.start(0)

for dc in range(opto_repeat):
    pwm.ChangeDutyCycle(100) # 50:   20Hz       ,        100:    0Hz
    sleep(opto_pulse_duration)
    pwm.ChangeDutyCycle(0)
    sleep(ISI)
pwm.stop(0)

sleep(after_opto)

GPIO.output(11, 0)
GPIO.cleanup()

camera.stop_recording()
camera.stop_preview()

parameters = {'projection' : projection, 'laser' : laser, 'opto_pulse_duration' : opto_pulse_duration, 'opto_repeat' : opto_repeat, 'ISI' : ISI, 'prestimulus' : prestimulus, 'after_opto' : after_opto, 'movie_duration' : movie_duration, 'movie_directory' : movie_directory}

with open(movie_directory + '.txt', 'a') as file:
    file.write(str(parameters))

