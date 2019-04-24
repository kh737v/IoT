import RPi.GPIO as GPIO
import time

led_pin=21

GPIO.setmode(GPIO.BCM) #BOARD)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 100)
pwm.start(0)

print 'from 0 to 100'
for i in range(100):
  print i
  pwm.ChangeDutyCycle(i)
  time.sleep(0.1)

print 'from 100 to 1'
for i in range(100, 0, -1):
  print i
  pwm.ChangeDutyCycle(i)
  time.sleep(0.1)

pwm.stop()
GPIO.cleanup()

# how to run ?
# pi@raspberrypi:~/python $ sudo python servo_pwm.py

