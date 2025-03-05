import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)

opto_trig = 19
duration_sec = 90;
opto_pulse_duration = 3;
ds = duration_sec * 100;
prevstate_first = False
currstate_first = False
print("Time is %s " % (datetime.datetime.now()))

try:
    while 1:
        #time.sleep(0.01)
        prevstate_first = currstate_first
        currstate_first = GPIO.input(opto_trig)
        if currstate_first != prevstate_first:
            newstate_first = "1" if currstate_first else "0"
            print("Input from infrared %s is %s" % (opto_trig, newstate_first))
            pwm.start(0)
            if newstate_first == "0":
                print("Time is %s " % (datetime.datetime.now()))
                pwm.ChangeDutyCycle(50)
                pwm.ChangeFrequency(20)
                sleep(opto_pulse_duration)
            else:
                print("No opto")
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Press ctrl+C to stop")
    pass

