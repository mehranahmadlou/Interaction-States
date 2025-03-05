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

laser = 5
opto_pulse_duration = 3
opto_repeat = 750
ISI = 3
prestimulus = 0
after_opto = 120
movie_duration = (opto_pulse_duration + ISI) * opto_repeat + prestimulus + after_opto
movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/cFOs_ChR2/1120755/test_LHb_ChR2_cFosxxx.h264'
projection = 'LHb > MnR ChR2'

camera.start_preview()
camera.start_recording(movie_directory, bitrate=10000000)

sleep(prestimulus)

pwm.start(0)

for dc in range(opto_repeat):
    pwm.ChangeDutyCycle(50)
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

