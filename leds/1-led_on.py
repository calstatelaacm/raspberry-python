# import RPi.GPIO library so we can use the GPIO pins
import RPi.GPIO as GPIO

# set it so that we use the "Broadcom SOC channels" instead of the pin numbers (1-40)
GPIO.setmode(GPIO.BCM)

# disable warnings
GPIO.setwarnings(False)

# tell the program that we will be using pin #21
GPIO.setup(21, GPIO.OUT)

# set GPIO pin 21 to HIGH (meaning on) (LOW means off)
print("Lights on")
GPIO.output(21, GPIO.HIGH)

# turn all power off to the pins used
GPIO.cleanup()