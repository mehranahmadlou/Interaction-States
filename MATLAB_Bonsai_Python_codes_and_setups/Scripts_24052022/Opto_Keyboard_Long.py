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
pwm = GPIO.PWM(12, 20)

laser = 5
opto_pulse_duration = 30
movie_duration = 300
exp_name = 'Experiment_1122831_Opto_OneNovel_blackrubber_LongOpto_4xxx'
movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Opto_Behaviour/1122831_22112021/OneNovel_LongStim/'
movie_file = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Opto_Behaviour/1122831_22112021/OneNovel_LongStim/' + exp_name + '.h264'
projection = 'Vglut3 MnR ChR2'

camera.start_preview()
camera.start_recording(movie_file, bitrate=10000000)
t0 = time.time() # start time in seconds

pwm.start(0)
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('OPTO KEYBOARD','press espace for opto')

num_opto = 0
opto_onsets=[]
done = False
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
            if event.key == pygame.K_ESCAPE or num_opto == 5:
                print("Opto Done, wait 30 sec ...")
                sleep(30)
                t1 = time.time() 
                num_seconds = t1 - t0 # duration of movie
                movie_duration = num_seconds
                done = True
                pygame.quit()    


pwm.stop(0)

camera.stop_recording()
camera.stop_preview()

parameters = {'projection' : projection, 'laser' : laser, 'opto_pulse_duration' : opto_pulse_duration, 'movie_duration' : movie_duration, 'movie_directory' : movie_directory}

with open(movie_directory + exp_name + '_protocol_info.txt', 'a') as file:
    file.write(str(parameters))
with open(movie_directory + exp_name + '_opto_onsets.txt', 'a') as file:
    file.write(str(opto_onsets))


