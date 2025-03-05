import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

# first wait 300 seconds, start the python just after you see: "Time is %s " % (datetime.datetime.now()) 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

laser = 0
opto_trig = 13
pre_start_sound_duration = 30
opto_pulse_duration = 3
sound_duration = 5
no_sound_duration = 30
opto_repeat = 30

prevstate_first = False
currstate_first = False
#print("Time is %s " % (datetime.datetime.now()))

movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Sound_conditioning/arousal/Sound_opto_pupil_test_day3/1118866_26052021/'
projection = 'SC->MLR'

t0 = time.time() # start time in seconds
sleep(pre_start_sound_duration)
print("Time is %s " % (datetime.datetime.now()))
num_seconds = []
r=0
try:
    while 1:
        #time.sleep(0.01)
        currstate_first = GPIO.input(opto_trig)
        pwm.start(0)
        if currstate_first == 0:
            sleep(2.0)
            r +=1
            t1 = time.time() # current time
            d = t1 - t0
            num_seconds.append(d) # diff time from onset of movie
            print(d , r)
            pwm.ChangeDutyCycle(50)
            pwm.ChangeFrequency(20)
            sleep(opto_pulse_duration)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Press ctrl+C to stop")
    pass


parameters = {'projection' : projection, 'pre_start_sound_duration': pre_start_sound_duration, 'laser' : laser, 'opto_pulse_duration' : opto_pulse_duration, 'opto_repeat' : opto_repeat, 'sound_duration' : sound_duration,  'no_sound_duration' : no_sound_duration,'movie_directory' : movie_directory}
with open(movie_directory + 'params.txt', 'a') as file:
    file.write(str(parameters))
with open(movie_directory + 'Onset_Opto_Timing.txt', 'a') as file:
    file.write(str(num_seconds))

