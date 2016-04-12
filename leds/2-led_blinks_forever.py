# import time library (this allows us to put the program to sleep)
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)

# this will make it loop forever unless you have a condition stating otherwise
while True:

  # turn led on
  GPIO.output(21, GPIO.HIGH)
  time.sleep(1)

  # turn led off
  GPIO.output(21, GPIO.LOW)
  time.sleep(1)