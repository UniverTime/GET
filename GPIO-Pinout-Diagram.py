import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.output(23, GPIO.input(17))