from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
import RPi.GPIO as GPIO
from time import sleep

pigpio_factory = PiGPIOFactory()
servo =AngularServo(12, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)
in1, in2, en = 19, 16, 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT) # In 1
GPIO.setup(in2, GPIO.OUT) # In 2
GPIO.setup(en, GPIO.OUT) # En
pwm = GPIO.PWM(en, 1000)
pwm.start(30)
try:
    servo.angle = 126.5 
    sleep(0.5)
    GPIO.output(in1, GPIO.HIGH) #start
    GPIO.output(in2, GPIO.LOW)
    sleep(2.5)
    servo.angle = 70 #turn right
    sleep(2.5)
    servo.angle = 126.5
    GPIO.output(in1, GPIO.HIGH) #move forward
    GPIO.output(in2, GPIO.LOW)
    sleep(2)
    servo.angle = 73 #turn right
    sleep(2.5)
    servo.angle = 126.5
    GPIO.output(in1, GPIO.HIGH) #move forward
    GPIO.output(in2, GPIO.LOW)
    sleep(2)

    GPIO.output(in1, GPIO.LOW) #stop
    GPIO.output(in2, GPIO.LOW)
    servo.angle = 126.5
    sleep(2)
except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
sleep(0.5)
GPIO.cleanup()
