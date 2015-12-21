import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
	truth = GPIO.input(24)
	if(truth == False):
		print("Hi")
		time.sleep(0.2)
	else:
		print("hello")
		time.sleep(0.2)
