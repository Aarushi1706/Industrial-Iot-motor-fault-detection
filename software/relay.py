import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
while True:
GPIO.output(22, 0) # ON (click)
print("Relay ON")
time.sleep(2)
GPIO.output(22, 1) # OFF
print("Relay OFF")
time.sleep(2)
