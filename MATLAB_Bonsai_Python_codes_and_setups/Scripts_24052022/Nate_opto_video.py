import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 10)

laser = 60
opto_pulse_duration = 1
opto_repeat = 3
ISI = 60
prestimulus = 30
after_opto = 60
movie_duration = (opto_pulse_duration + ISI) * opto_repeat + prestimulus + after_opto
movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/NaMi_20200413_midbrainhistology/Opto_behavior/16/rightSNr_7_0Hz_05mV_30s.h264'
projection = 'Right SNr'

camera.start_preview()
camera.start_recording(movie_directory, bitrate=10000000)

sleep(prestimulus)

pwm.start(0)

for dc in range(opto_repeat):
    pwm.ChangeDutyCycle(100)
    sleep(opto_pulse_duration)
    pwm.ChangeDutyCycle(0)
    sleep(ISI)

pwm.stop(0)

sleep(after_opto)

camera.stop_recording()
camera.stop_preview()

parameters = {'projection' : projection, 'laser' : laser, 'opto_pulse_duration' : opto_pulse_duration, 'opto_repeat' : opto_repeat, 'ISI' : ISI, 'prestimulus' : prestimulus, 'after_opto' : after_opto, 'movie_duration' : movie_duration, 'movie_directory' : movie_directory}

with open(movie_directory + '.txt', 'a') as file:
    file.write(str(parameters))

