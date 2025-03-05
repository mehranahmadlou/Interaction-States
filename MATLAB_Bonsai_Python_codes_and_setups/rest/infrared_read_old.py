import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
GPIO.setup(14, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)

print(GPIO.input(14))
print(GPIO.input(15))

first_sensor = 14
second_sensor = 15

prevstate = False
currstate = False

with open('test.txt', 'a') as text_file:
    while True:
        time.sleep(0.1)
        prevstate = currstate
        currstate = GPIO.input(first_sensor)
        if currstate != prevstate:
            newstate = '1' if currstate else '0'
            print('Input from infrared %s is %s' % (first_sensor, newstate))
            
            try:
                values = [datetime.datetime.now(), newstate]
                text_file.write('values')
            except:
                print('cannot open file')
                
    while True:
        time.sleep(0.1)
        prevstate = currstate
        currstate = GPIO.input(second_sensor)
        if currstate != prevstate:
            newstate = '1' if currstate else '0'
            print('Input from infrared %s is %s' % (second_sensor, newstate))
            
            try:
                values = [datetime.datetime.now(), newstate]
                text_file.write('values')
            except:
                print('cannot open file')