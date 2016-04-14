# from the 'time' library, import the sleep method
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)

# this will make it loop forever unless you have a condition stating otherwise
while True:

  # turn led on
  GPIO.output(21, GPIO.HIGH)
  sleep(1)

  # turn led off
  GPIO.output(21, GPIO.LOW)
  sleep(1)
