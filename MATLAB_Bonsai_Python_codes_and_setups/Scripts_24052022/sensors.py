import RPi.GPIO as GPIO
import time
import datetime
from time import sleep
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

first_sensor = 15
second_sensor = 14

prevstate_first = False
currstate_first = False
prevstate_second = False
currstate_second = False

camera = PiCamera()
camera.resolution = (1028, 960)
camera.framerate = 25

movie_directory = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Self_Stimulation/x/'
movie_file = '/home/pi/swc/mrsic_flogel/public/projects/MeAh_JuDz_20210211_Optogenetics_Behavior/Self_Stimulation/x/selfstim.h264'
projection = 'AH -> MnR ChR2'

camera.start_preview()
camera.start_recording(movie_file, bitrate=10000000)


t0 = time.time() # start time in seconds

while True:
    t1 = time.time() # current time
    num_seconds = t1 - t0 # diff
    if num_seconds > 2400:  # e.g. break after 3600 seconds
        camera.stop_recording()
        camera.stop_preview()
        pwm.stop()
        GPIO.cleanup()
        print("Done")
        parameters = {'projection' : projection, 'laser_port' : first_sensor, 'nolaser_port' : second_sensor, 'movie_directory' : movie_directory}
        with open(movie_directory + 'info.txt', 'a') as file:
            file.write(str(parameters))
        break
    while GPIO.input(first_sensor) == 1 and GPIO.input(second_sensor) == 0:
        with open(movie_directory + 'first_sensor.txt', 'a') as text_first:
            #for i in range(300):
            time.sleep(0.01)
            prevstate_first = currstate_first
            currstate_first = GPIO.input(first_sensor)
            if currstate_first != prevstate_first:
                newstate_first = "1" if currstate_first else "0"
                print("Input from infrared %s is %s" % (first_sensor, newstate_first))
                values_first = [datetime.datetime.now(), newstate_first]
                text_first.write(str(values_first))
                pwm.start(0)
                if newstate_first == "1":
                    pwm.ChangeDutyCycle(50)
                    pwm.ChangeFrequency(20)
                    #sleep(0.1)
                else:
                    pwm.stop()
                    print("No opto")
    while GPIO.input(second_sensor) == 1 and GPIO.input(first_sensor) == 0:
        with open(movie_directory + 'second_sensor.txt', 'a') as text_second:
            #for i in range(300):
            time.sleep(0.01)
            prevstate_second = currstate_second
            currstate_second = GPIO.input(second_sensor)
            if currstate_second != prevstate_second:
                newstate_second = "1" if currstate_second else "0"
                print("Input from infrared %s is %s" % (second_sensor, newstate_second))
                values_second = [datetime.datetime.now(), newstate_second]
                text_second.write(str(values_second))
                #sleep(0.1)
    while GPIO.input(second_sensor) == 0 and GPIO.input(first_sensor) == 0:
        pwm.stop()

