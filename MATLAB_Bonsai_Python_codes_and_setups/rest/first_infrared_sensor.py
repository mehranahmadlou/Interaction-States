import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
GPIO.setup(15, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

first_sensor = 15

prevstate_first = False
currstate_first = False

with open("first_sensor.txt", "a") as text_first:
    for i in range(3000):
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
            else:
                pwm.stop()
                print("No opto")