import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
while True:
    GPIO.output(24, True)
    time.sleep(10)
    GPIO.output(24, False)
    GPIO.output(23, True)
    time.sleep(3)
    GPIO.output(23, False)
    GPIO.output(18, True)
    time.sleep(1)
    GPIO.output(18, False)
    for x in range(0, 8):
        GPIO.output(25, True)
        time.sleep(0.5)
        GPIO.output(25, False)
        time.sleep(0.5)
