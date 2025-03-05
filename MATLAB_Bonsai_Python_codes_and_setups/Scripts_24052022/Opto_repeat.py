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
opto_pulse_duration = 3
opto_off_duration = 12 #15:long
opto_repeat = 30

print("Time is %s " % (datetime.datetime.now()))

try:
    while True:
        if GPIO.input(opto_trig) == False:
            sleep(15)
            pwm.start(0)
            for i in range(opto_repeat):
                print("OPTO ON")
                pwm.ChangeDutyCycle(100) #50
                pwm.ChangeFrequency(20) #20
                sleep(opto_pulse_duration)
                pwm.ChangeDutyCycle(0)
                sleep(opto_off_duration)
            sleep(5)
            pwm.stop()
            break        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Press ctrl+C to stop")
    pass



