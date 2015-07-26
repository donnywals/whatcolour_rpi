import RPi.GPIO as GPIO
import time

bluepin = 21
greenpin = 20
redpin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(bluepin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)
GPIO.setup(redpin, GPIO.OUT)

freq = 60

r = GPIO.PWM(redpin, freq)
r.start(0)

g = GPIO.PWM(greenpin, freq)
g.start(0)

b = GPIO.PWM(bluepin, freq)
b.start(0)

try:
    while True:
        current_time = time.localtime()
        hours = float(time.strftime("%H", current_time))
        minutes = float(time.strftime("%M", current_time))
        seconds = float(time.strftime("%S", current_time))

        r_val = hours/24*100
        g_val = minutes/60*100
        b_val = seconds

        r.ChangeDutyCycle(r_val)
        g.ChangeDutyCycle(g_val)
        b.ChangeDutyCycle(b_val)

        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
