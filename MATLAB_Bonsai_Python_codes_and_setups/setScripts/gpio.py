import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 20)
pwm.start(0)

for dc in range(40):
    pwm.ChangeDutyCycle(50)
    sleep(2)
    pwm.ChangeDutyCycle(0)
    sleep(1)
    
pwm.stop(10)

#sudo mount -t cifs -o username=mahmadlou,uid=1000,gid=1000 //winstor.id.swc.ucl.ac.uk/winstor/swc/ /home/pi/swc