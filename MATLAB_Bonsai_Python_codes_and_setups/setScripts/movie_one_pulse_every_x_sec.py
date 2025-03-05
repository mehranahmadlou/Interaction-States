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

laser = 25
opto_pulse_start = 0
opto_pulse_duration = 60
opto_repeat = 1
ISI = 0
posttime = 0

movie_duration = opto_pulse_start + ((opto_pulse_duration + ISI) * opto_repeat) + posttime
movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Experiment/1118866_24022021/SC_ZI_ST/Experiment_1118866_SCtoZIST_test_15.h264'
projection = 'SC->ZI/ST'

camera.start_preview()
camera.start_recording(movie_directory, bitrate=10000000)

pwm.start(0)
sleep(opto_pulse_start)

for dc in range(opto_repeat):
    pwm.ChangeDutyCycle(50)
    sleep(opto_pulse_duration)
    pwm.ChangeDutyCycle(0)
    sleep(ISI)

pwm.stop(0)

sleep(posttime)
    
camera.stop_recording()
camera.stop_preview()

parameters = {'projection' : projection, 'laser' : laser, 'opto_pulse_start' : opto_pulse_start, 'opto_pulse_duration' : opto_pulse_duration, 'opto_repeat' : opto_repeat, 'ISI' : ISI, 'movie_duration' : movie_duration, 'posttime' : posttime, 'movie_directory' : movie_directory}

with open(movie_directory + '.txt', 'a') as file:
    file.write(str(parameters))

