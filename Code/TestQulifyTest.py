import cv2 
import numpy as np
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
import RPi.GPIO as GPIO
import time
from camera import camera
import threading
time.sleep(0.5)
cam = camera() 
vs = threading.Thread(target=cam.update, daemon=True)
vs.start()

def DetectOrange(frame): # function detect orange color by HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_Orange = np.array([0, 45, 10])
    upper_Orange = np.array([26, 255, 255])
    Orange_detect = cv2.inRange(hsv, lower_Orange, upper_Orange)
    return Orange_detect

def DetectBlue(frame): # function detect blue color by HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_Blue = np.array([105, 51, 0])
    upper_Blue = np.array([116, 255, 255])
    Blue_detect = cv2.inRange(hsv, lower_Blue, upper_Blue)
    return Blue_detect

pigpio_factory = PiGPIOFactory()
servo = AngularServo(12, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)

in1, in2, en = 19, 16, 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT) # In 1
GPIO.setup(in2, GPIO.OUT) # In 2
GPIO.setup(en, GPIO.OUT) # En
pwm = GPIO.PWM(en, 1000)

def forward(speed):
    pwm.start(speed)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

def stopM():
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        pwm.start(0)

# Define GPIO pins
TRIG_PIN_1 = 18
ECHO_PIN_1 = 27
TRIG_PIN_2 = 22
ECHO_PIN_2 = 23
TRIG_PIN_3 = 24
ECHO_PIN_3 = 10

# Set up pins
GPIO.setup(TRIG_PIN_1, GPIO.OUT)
GPIO.setup(ECHO_PIN_1, GPIO.IN)
GPIO.setup(TRIG_PIN_2, GPIO.OUT)
GPIO.setup(ECHO_PIN_2, GPIO.IN)
GPIO.setup(TRIG_PIN_3, GPIO.OUT)
GPIO.setup(ECHO_PIN_3, GPIO.IN)

def measure_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, True)
    time.sleep(0.000001)
    GPIO.output(trig_pin, False)

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
       

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()
       
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound: 343 m/s
    return int(distance)

Kp = 0.5
Kd = 0.2
errors = 0
output = 0
derivative = 0
previous_error = 0
servoCenter = 85

def PIDUltrasonic():
    global previous_error 
    distance_L = measure_distance(TRIG_PIN_1, ECHO_PIN_1)
    distance_R = measure_distance(TRIG_PIN_2, ECHO_PIN_2)
    distance_C = measure_distance(TRIG_PIN_3, ECHO_PIN_3)
    distance_L = max(min(distance_L, 80), 2)
    distance_R = max(min(distance_R, 80), 2)
    distance_C = max(min(distance_C, 80), 2)
     
    valDistance = distance_R - distance_L
    errors = valDistance - 0
    derivative = errors - previous_error
    output = ((Kp * errors) + (Kd * derivative))
    output = max(min(output, 35), -40)
    previous_error = errors
    valServo = servoCenter-output
    # print(output)
    servo.angle = valServo
    # time.sleep(0.1)
    

try:
    # while True:
    servo.angle = servoCenter
    # time.sleep(0.5)  
    forward(30)
    mode = 0
    while True: 
        ret, frame = cam.get()
        crop = frame [150:1200 , 0:1200]
        height, width = frame.shape[:2]
        flipped_frame = cv2.flip(frame, -1) 
        times = time.time()
        while time.time() - times < 40 :
            distance_L = measure_distance(TRIG_PIN_1, ECHO_PIN_1)
            distance_R = measure_distance(TRIG_PIN_2, ECHO_PIN_2)
            distance_C = measure_distance(TRIG_PIN_3, ECHO_PIN_3)
            distance_L = max(min(distance_L, 80), 2)
            distance_R = max(min(distance_R, 80), 2)
            distance_C = max(min(distance_C, 80), 2)
            print("distance_L = ", distance_L, " distance_C = ", distance_C, " distance_R = ",distance_R )
          
            # ret, frame = cam.get()
            # crop = cam [150:1200 , 0:1200]
            if distance_C < 70:
                servo.angle = 110
            
            Orange_detect = DetectOrange(flipped_frame)
            Blue_detect = DetectBlue(flipped_frame)
            Orange_contours, _ = cv2.findContours(Orange_detect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            Blue_contours, _ = cv2.findContours(Blue_detect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            if len(Orange_contours) > 0:
                for cnt in Orange_contours:
                    area = cv2.contourArea(cnt)
                    if area > 1000:  
                        x, y, w, h = cv2.boundingRect(cnt)
                        print("find")
            else:
                PIDUltrasonic()
            # print(count)
            time.sleep(0.01)

        while True:
            forward(0)
        
        # print("distance_L = ", distance_L, " distance_C = ", distance_C, " distance_R = ",distance_R )
        
        # time.sleep(0.5)
         # Call the DTCT function to get the distance

        # ret, frame = cam.get()
        # flipped_frame = cv2.flip(frame, -1)        
        
        # Orange_detect = DetectOrange(flipped_frame)
        # Blue_detect = DetectBlue(flipped_frame)
        # Orange_contours, _ = cv2.findContours(Orange_detect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # Blue_contours, _ = cv2.findContours(Blue_detect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # height, width = frame.shape[:2]
        # x = (width // 3) * 2
        # center_y = height // 2
       
     
        # cv2.line(frame, (0, center_y), (width, center_y), (0, 0, 0), 2) 
        #     if len(Orange_contours) > 0:
        #         for cnt in Orange_contours:
        #             area = cv2.contourArea(cnt)
        #             if area > 180:  
        #                 x, y, w, h = cv2.boundingRect(cnt)
        #                 center_x = x + w // 2
        #                 print(area)
        #                 times = time.time()
        #                 while time.time() - times < 2.2 :
        #                     forward(20)
        #                     servo.angle = 50
        #                 times = time.time()
        #                 while time.time() - times < 1.1 :
        #                     servo.angle = 85
        #                     while True:
        #                         stopM()
        #                 break
       
        # if len(Orange_contours) > 0:
        #     for cnt in Orange_contours:
        #         area = cv2.contourArea(cnt)
        #         x, y, w, h = cv2.boundingRect(cnt)
        #         #center_x = x + w // 2 
        #         time.sleep(0.1)
        #         if  area > 1400 and y > 50 :
        #             print(area)
        #             times = time.time()
        #             while time.time() - times < 0.65 :
        #                 servo.angle = 110
        #             times = time.time()
        #             while time.time() - times < 1.1 :
        # #                 servo.angle = 85
        # if d > 50 :
        #    print(distance_center)
              
       
        # else:
        #     #forward(30)
        #     pass

except KeyboardInterrupt:
    pass

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
time.sleep(0.5)
GPIO.cleanup()
cam.shutdown()

# Stop the servo and clean up GPIO


