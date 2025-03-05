import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

opto_trig = 13
duration_sec = 90;
opto_pulse_duration = 3;
ds = duration_sec * 100;
prevstate_first = False
currstate_first = False
print("Time is %s " % (datetime.datetime.now()))

try:
    while 1:
        #time.sleep(0.01)
        currstate_first = GPIO.input(opto_trig)
        pwm.start(0)
        if currstate_first == 0:
            print("Time is %s " % (datetime.datetime.now()))
            pwm.ChangeDutyCycle(50)
            pwm.ChangeFrequency(20)
            sleep(opto_pulse_duration)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Press ctrl+C to stop")
    pass


