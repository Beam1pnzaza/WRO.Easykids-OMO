from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
import RPi.GPIO as GPIO
import time
import cv2 
import numpy as np
from camera import camera
import threading

cam = camera() 
vs = threading.Thread(target=cam.update, daemon=True)
vs.start()

def DetectRed(frame): # function detect red color by HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 126, 56])
    upper_red = np.array([12, 255, 255])
    red_detect = cv2.inRange(hsv, lower_red, upper_red)
    return red_detect

def DetectGreen(frame): # function detect green color by HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([59, 235, 25])
    upper_green = np.array([74, 255, 255])
    green_detect = cv2.inRange(hsv, lower_green, upper_green)
    return green_detect

pigpio_factory = PiGPIOFactory()
servo = AngularServo(12, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)
in1, in2, en = 19, 16, 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT) # In 1
GPIO.setup(in2, GPIO.OUT) # In 2
GPIO.setup(en, GPIO.OUT) # En
pwm = GPIO.PWM(en, 1000)
pwm.start(20)

try:
    while True:
        # start with set servo and drive forward
        servo.angle = 125
        time.sleep(0.5)
        GPIO.output(in1, GPIO.HIGH) 
        GPIO.output(in2, GPIO.LOW)

        # set camera and detect color
        ret, frame = cam.get()

        # Flip the frame horizontally and vertically
        flipped_frame = cv2.flip(frame, -1)

        red_detect = DetectRed(flipped_frame)
        green_detect = DetectGreen(flipped_frame)
        red_contours, _ = cv2.findContours(red_detect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        green_contours, _ = cv2.findContours(green_detect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # import x line for detect position of object color
        height, width = frame.shape[:2]
        x1 = width // 3
        x2 = (width // 3) * 2
        center_y = height // 2
        cv2.line(frame, (x1, 0), (x1, height), (0, 0, 0), 2)
        cv2.line(frame, (x2, 0), (x2, height), (0, 0, 0), 2)
        cv2.line(frame, (0, center_y), (width, center_y), (0, 0, 0), 2)

        # Detect red
        if len(red_contours) > 0:
            for cnt in red_contours:
                area = cv2.contourArea(cnt)
                if area > 2000:  # Area Red object
                    x, y, w, h = cv2.boundingRect(cnt)
                    center_x = x + w // 2
                    if center_x < x1: # Zone-1 Red (left line x1)
                        pwm.start(0)
                        time.sleep(1)           
                        print("Red area Zone1:", area)
                        timeS = time.time()
                        while time.time() - timeS < 0.8:
                            GPIO.output(in1, GPIO.HIGH) 
                            GPIO.output(in2, GPIO.LOW)
                            servo.angle = 80
                        timeS = time.time()
                        while time.time() - timeS < 1:
                            GPIO.output(in1, GPIO.HIGH) 
                            GPIO.output(in2, GPIO.LOW)
                            servo.angle = 160
                        break
                    elif x1 <= center_x < x2:  # Zone-2 Red (left line x2)
                        servo.angle = 75
                        pwm.start(0)
                        time.sleep(1)
                        print("Red area Zone2", area)
                        timeS = time.time()
                        while time.time() - timeS < 1.5:
                            GPIO.output(in1, GPIO.HIGH) 
                            GPIO.output(in2, GPIO.LOW)
                            servo.angle = 75
                        timeS = time.time()
                        while time.time() - timeS < 1.5:
                            GPIO.output(in1, GPIO.HIGH) 
                            GPIO.output(in2, GPIO.LOW)
                            servo.angle = 160
                        break
                    else:                       # Zone-3 Red (right line x2)
                        pwm.start(0)
                        time.sleep(1)
                        print("Red area Zone3:", area)
                        timeS = time.time()
                        while time.time() - timeS < 0.8:
                            GPIO.output(in1, GPIO.HIGH) 
                            GPIO.output(in2, GPIO.LOW)
                            servo.angle = 80
                        timeS = time.time()
                        while time.time() - timeS < 1:
                            GPIO.output(in1, GPIO.HIGH) 
                            GPIO.output(in2, GPIO.LOW)
                            servo.angle = 160
                        break
            
        # Detect green
        elif len(green_contours) > 0:                       
            for cnt in green_contours:
                area = cv2.contourArea(cnt)
                if area > 10000 :  # Area Green object 
                    x, y, w, h = cv2.boundingRect(cnt)
                    center_x = x + w // 2                                
                    if center_x < x1:  # Zone-1 Green (left line x1)
                        print("GREEN area Zone1:", area)
                        timeS = time.time()
                        while time.time() - timeS < 0.8:
                            # GPIO.output(in1, GPIO.HIGH) 
                            # GPIO.output(in2, GPIO.LOW)
                            servo.angle = 150
                        timeS = time.time()
                        while time.time() - timeS < 1.1:
                            servo.angle = 100
                        break
                    elif x1 <= center_x < x2:  # Zone-2 Green (left line x2)
                        print("GREEN area Zone2:", area)
                        timeS = time.time()
                        while time.time() - timeS < 1.6:
                            # GPIO.output(in1, GPIO.HIGH) 
                            # GPIO.output(in2, GPIO.LOW)
                            servo.angle = 150
                        timeS = time.time()
                        while time.time() - timeS < 2.2:
                            servo.angle = 100
                        break
                    else:  # Zone-3 Green (right line x2)
                        print("GREEN area Zone3:", area)
                        timeS = time.time()
                        while time.time() - timeS < 0.8:
                            # GPIO.output(in1, GPIO.HIGH) 
                            # GPIO.output(in2, GPIO.LOW)
                            servo.angle = 150
                        timeS = time.time()
                        while time.time() - timeS < 1.1:
                            servo.angle = 100
                        break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)

# Stop the servo and clean up GPIO
cv2.imwrite("red.jpg", red_detect)
cv2.imwrite("green.jpg", green_detect)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
time.sleep(0.5)
GPIO.cleanup()
cam.shutdown()
