from __future__ import division
import numpy as np
import sounddevice as sd
#from time import sleep
import time
import serial
import soundfile as sf
import cv2

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM9'

volume = 0.39  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz
duration1 = 5.0  # in seconds
f = 4000  # sine frequency, Hz
t1 = np.arange(int(duration1 * fs)) / fs
samples1 = volume * np.sin(2 * np.pi * f * t1)


# Capture video from webcam
vid_capture0 = cv2.VideoCapture(0,cv2.CAP_DSHOW)
vid_capture1 = cv2.VideoCapture(1,cv2.CAP_DSHOW)


vid_capture0.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
vid_capture0.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
frame_w0 = int(vid_capture0.get(3))
frame_h0 = int(vid_capture0.get(4))

vid_capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
vid_capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
frame_w1 = int(vid_capture1.get(3))
frame_h1 = int(vid_capture1.get(4))


vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output0 = cv2.VideoWriter("Pupil.avi", vid_cod, 30.0, (frame_w0, frame_h0))
output1 = cv2.VideoWriter("Whisker.avi", vid_cod, 30.0, (frame_w1, frame_h1))

t = time.time()

while True:
    # Capture each frame of webcam video
    ret0, frame0 = vid_capture0.read()
    ret1, frame1 = vid_capture1.read()
    cv2.imshow("Pupil video", frame0)
    cv2.imshow("Whisker video", frame1)
    elapsed = time.time() - t
    if elapsed > 30.00:
        t = time.time()
        sd.play(samples1, fs)
        ser.open()
        time.sleep(0.1)
        ser.close()

    output0.write(frame0)
    output1.write(frame1)
    # Close and break the loop after pressing "x" key
    if cv2.waitKey(1) == ord("q"):
        break
# close the already opened camera
vid_capture0.release()
vid_capture1.release()
# close the already opened file
output0.release()
output1.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()
