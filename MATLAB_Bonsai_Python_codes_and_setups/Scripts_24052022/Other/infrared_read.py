import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
GPIO.setup(14, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(12, GPIO.OUT)

#print(GPIO.input(14))
#print(GPIO.input(15))

first_sensor = 14
second_sensor = 15
#pwm = GPIO.PWM(12, 20)

prevstate_first = False
currstate_first = False
prevstate_second = False
currstate_second = False

with open("first_sensor.txt", "a") as text_first:
    for i in range(300):
        time.sleep(0.1)
        prevstate_first = currstate_first
        currstate_first = GPIO.input(first_sensor)
        if currstate_first != prevstate_first:
            newstate_first = "1" if currstate_first else "0"
            print("Input from infrared %s is %s" % (first_sensor, newstate_first))
            values_first = [datetime.datetime.now(), newstate_first]
            text_first.write(str(values_first))        

with open("second_sensor.txt", "a") as text_second:
    for i in range(300):
        time.sleep(0.1)
        prevstate_second = currstate_second
        currstate_second = GPIO.input(second_sensor)
        if currstate_second != prevstate_second:
            newstate_second = "1" if currstate_second else "0"
            print("Input from infrared %s is %s" % (second_sensor, newstate_second))
            values_second = [datetime.datetime.now(), newstate_second]
            text_second.write(str(values_second))