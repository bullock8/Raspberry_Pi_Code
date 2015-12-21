import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.OUT)
thing = True
def inputCheck(times):
	for n in range(times):
		if(GPIO.input(24) == False):
			break
		else:
			time.sleep(1.0/times)
try:
	while True:
		switchValue = GPIO.input(24)
		time.sleep(0.1)
		if(switchValue == True):
			GPIO.output(18, True)
			inputCheck(20)
			GPIO.output(18, False)
			GPIO.output(23, True)
			inputCheck(20)
			GPIO.output(23, False)
			GPIO.output(25, True)
			inputCheck(20)
			GPIO.output(25, False)
			thing = True
			count = 0
		else:
			print("hi")
			if(thing == False and count >20):
				GPIO.cleanup()
				sys.exit()
			elif(thing == False):
				count += 1
			else:
				thing = False
				count = 1
except KeyboardInterrupt:
	GPIO.cleanup()
