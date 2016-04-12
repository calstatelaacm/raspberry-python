# import OS module to run commands on OS
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)

print("-----------------")
print("  Button + GPIO  ")
print("-----------------")

# print the current button status
print(GPIO.input(21))
while True:
  if(GPIO.input(21) == False):
    print("Button Pressed")
    os.system('date')
    print(GPIO.input(21))
    time.sleep(3)
  else:
    os.system('clear')
    print("Waiting for you to press a button")