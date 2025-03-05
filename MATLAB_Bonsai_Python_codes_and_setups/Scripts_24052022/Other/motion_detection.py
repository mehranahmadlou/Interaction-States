import io
import random
import picamera
import numpy as np
from PIL import Image
import RPi.GPIO as GPIO
from time import sleep
from picamera.array import PiRGBAnalysis
from picamera.color import Color

prior_image = None

def detect_motion(camera):
    global prior_image
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg', use_video_port=True)
    stream.seek(0)
    if prior_image is None:
        prior_image = Image.open(stream)
        return False
    else:
        current_image = Image.open(stream)
        result = random.randint(0, 10) == 0
        prior_image = current_image
        return result
    
#class MyColorAnalyzer(PiRGBAnalysis):
#    def __init__(self, camera):
#        super(MyColorAnalyzer, self).__init__(camera)
#        self.last_color = ''

#    def analyze(self, a):
        # Convert the average color of the pixels in the middle box
#        c = Color(
#            r=int(np.mean(a[30:60, 60:120, 0])),
 #           g=int(np.mean(a[30:60, 60:120, 1])),
 #           b=int(np.mean(a[30:60, 60:120, 2]))
 #           )
        # Convert the color to hue, saturation, lightness
   #     h, l, s = c.hls
    #    c = 'none'
   #     if s > 1/3:
     #       if h > 8/9 or h < 1/36:
      #          c = 'red'
    #       elif 5/9 < h < 2/3:
       #         c = 'blue'
        #    elif 5/36 < h < 4/9:
       #         c = 'green'
        # If the color has changed, update the display
      #  if c != self.last_color:
       #     self.camera.annotate_text = c
        #    self.last_color = c    
    #
with picamera.PiCamera() as camera:
    camera.resolution = (1028, 960)
    camera.framerate = 25
    #camera.awb_mode = 'off'
    #camera.awb_gains = (1.4, 1.5)
    
    
    #camera.start_preview(alpha=128)
    #box = np.zeros((96, 160, 3), dtype=np.uint8)
    #box[30:60, 60:120, :] = 0x80
    #camera.add_overlay(memoryview(box), size=(160, 90), layer=3, alpha=64)
    
    stream = picamera.PiCameraCircularIO(camera, seconds=10)
    camera.start_recording(stream, format='h264')
    try:
        while True:
            camera.wait_recording(1)
            if detect_motion(camera):
                print('Motion detected!')
                
                
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
    
                GPIO.setup(12, GPIO.OUT)
                pwm = GPIO.PWM(12, 20)
                pwm.start(0)

                for dc in range(2):
                    pwm.ChangeDutyCycle(50)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)
                    sleep(1)
    
                pwm.stop(10)
                
                #camera.split_recording('after.h264')
                #stream.copy_to('before.h264', seconds=10)
                #stream.clear()
                #while detect_motion(camera):
                 #   camera.wait_recording(1)
                  #  print('Motion stopped')
                   # camera.split_recording(stream)
    finally:
        camera.stop_recording()
                