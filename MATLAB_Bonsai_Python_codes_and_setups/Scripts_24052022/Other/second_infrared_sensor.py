import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.IN)

second_sensor = 14

prevstate_second = False
currstate_second = False

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