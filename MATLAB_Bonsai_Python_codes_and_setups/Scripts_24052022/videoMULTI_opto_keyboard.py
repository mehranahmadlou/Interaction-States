# with multi cameras

import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import pygame
import time
import datetime

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

laser = 3
opto_pulse_duration = 4
movie_duration = 300
exp_name = 'NovelObjects_black_Opto_4xx'
movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAhetal_20210211_Optogenetics_Behavior/Opto_Behaviour/1121612/'
movie_file = '/home/pi/swc/mrsic_flogel/public/projects/MeAhetal_20210211_Optogenetics_Behavior/Opto_Behaviour/1121612/' + exp_name + '.h264'
projection = 'vgatADH MRN ChR2'

camera.start_preview()
camera.start_recording(movie_file, bitrate=10000000)
GPIO.output(11, 1)
GPIO.output(23, 1)
t0 = time.time() # start time in seconds

pwm.start(0)
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('OPTO KEYBOARD','press espace for opto')

num_opto = 0
opto_onsets=[]
done = False
try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    num_opto += 1
                    t1 = time.time() # current time
                    print("OPTO ON")
                    pwm.ChangeDutyCycle(50)
                    sleep(opto_pulse_duration)
                    pwm.ChangeDutyCycle(0)
                    sleep(0)
                    num_seconds = t1 - t0 # diff time from start of the movie
                    opto_onsets.append(num_seconds)
                if event.key == pygame.K_ESCAPE or num_opto == 15:
                    print("Opto Done, wait 300 sec ...")
                    sleep(300)
                    t1 = time.time() 
                    num_seconds = t1 - t0 # duration of movie
                    movie_duration = num_seconds
                    done = True
                    pygame.quit()    
except KeyboardInterrupt:
    GPIO.output(11, 0)
    GPIO.output(23, 0)
    pygame.quit() 
    print("Press ctrl+C to stop")
    pass

pwm.stop(0)

camera.stop_recording()
camera.stop_preview()

GPIO.output(11, 0)
GPIO.output(23, 0)

GPIO.cleanup()

parameters = {'projection' : projection, 'laser' : laser, 'opto_pulse_duration' : opto_pulse_duration, 'movie_duration' : movie_duration, 'movie_directory' : movie_directory}

with open(movie_directory + exp_name + '_protocol_info.txt', 'a') as file:
    file.write(str(parameters))
with open(movie_directory + exp_name + '_opto_onsets.txt', 'a') as file:
    file.write(str(opto_onsets))


