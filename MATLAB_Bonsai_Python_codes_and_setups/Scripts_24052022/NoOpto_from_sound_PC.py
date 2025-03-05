import RPi.GPIO as GPIO
import time
import datetime
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.IN)

opto_trig = 13
pre_start_sound_duration = 60
opto_pulse_duration = 0
sound_duration = 60
no_sound_duration = 60
opto_repeat = 1
laser = 0

currstate_first = False
#print("Time is %s " % (datetime.datetime.now()))

movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Sound_conditioning/behavior/Sound_noopto_test_day3/1118857_26042021/sound_noopto_day3.h264'
projection = 'LHb->PMnR'



try:
    while 1:
        #time.sleep(0.01)
        currstate_first = GPIO.input(opto_trig)
        if currstate_first == 0:
            print("Time is %s " % (datetime.datetime.now()))
            camera.start_preview()
            camera.start_recording(movie_directory, bitrate=10000000)
            sleep(pre_start_sound_duration+sound_duration+no_sound_duration)
            print("Time is %s " % (datetime.datetime.now()))
            camera.stop_recording()
            camera.stop_preview()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Press ctrl+C to stop")
    pass



parameters = {'projection' : projection, 'pre_start_sound_duration': pre_start_sound_duration, 'laser' : laser, 'opto_pulse_duration' : opto_pulse_duration, 'opto_repeat' : opto_repeat, 'sound_duration' : sound_duration,  'no_sound_duration' : no_sound_duration,'movie_directory' : movie_directory}
with open(movie_directory + '.txt', 'a') as file:
    file.write(str(parameters))


