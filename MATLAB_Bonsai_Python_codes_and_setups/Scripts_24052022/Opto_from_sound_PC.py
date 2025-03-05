import RPi.GPIO as GPIO
import time
import datetime
from time import sleep
from picamera import PiCamera

# first wait 300 seconds for day 1, start the python just after you see: "Time is %s " % (datetime.datetime.now()) 
# first wait 60 seconds for day 2,

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

laser = 1
opto_trig = 13
pre_start_sound_duration = 60 #day 2 60
opto_pulse_duration = 2.5
sound_duration = 30
no_sound_duration = 60
opto_repeat = 10

prevstate_first = False
currstate_first = False
#print("Time is %s " % (datetime.datetime.now()))

movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Sound_conditioning/behavior/Sound_opto_conditioning_day2/1118857_25042021/'
movie_file = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Sound_conditioning/behavior/Sound_opto_conditioning_day2/1118857_25042021/sound_opto_day2.h264'
projection = 'LHb->PMnR'

camera.start_preview()
camera.start_recording(movie_file, bitrate=10000000)
t0 = time.time() # start time in seconds
sleep(pre_start_sound_duration)
print("NOW START %s " % (datetime.datetime.now()))
num_seconds = []
r=0
try:
    while 1:
        #time.sleep(0.01)
        currstate_first = GPIO.input(opto_trig)
        pwm.start(0)
        if currstate_first == 0:
            r +=1
            t1 = time.time() # current time
            d = t1 - t0
            num_seconds.append(d) # diff time from onset of movie
            print(r, d)
            pwm.ChangeDutyCycle(50)
            pwm.ChangeFrequency(20)
            sleep(opto_pulse_duration)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Press ctrl+C to stop")
    pass

camera.stop_recording()
camera.stop_preview()

parameters = {'projection' : projection, 'pre_start_sound_duration': pre_start_sound_duration, 'laser' : laser, 'opto_pulse_duration' : opto_pulse_duration, 'opto_repeat' : opto_repeat, 'sound_duration' : sound_duration,  'no_sound_duration' : no_sound_duration,'movie_directory' : movie_directory}
with open(movie_file + '.txt', 'a') as file:
    file.write(str(parameters))
with open(movie_directory + 'Onset_Opto_Timing.txt', 'a') as file:
    file.write(str(num_seconds))
