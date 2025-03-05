import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

first_sensor = 15
second_sensor = 14

with open("first_sensor.txt", "a") as text_first, open("second_sensor.txt", "a") as text_second:
    while True:
        while GPIO.input(first_sensor) == 1:
        #with open("first_sensor.txt", "a") as text_first:
            #for i in range(300):
            time.sleep(0.01)
            print("Input from infrared %s" % (first_sensor))
            values_first = datetime.datetime.now()
            text_first.write(str(values_first))
            pwm.start(0)
            pwm.ChangeDutyCycle(50)
            pwm.ChangeFrequency(20)
        pwm.stop()
        #print("No opto")
                
        while GPIO.input(second_sensor) == 1:
        #with open("second_sensor.txt", "a") as text_second:
            #for i in range(300):
            time.sleep(0.01)
            print("Input from infrared %s" % (second_sensor))
            values_second = datetime.datetime.now()
            text_second.write(str(values_second))            