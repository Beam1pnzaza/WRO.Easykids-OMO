from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from time import sleep

pigpio_factory = PiGPIOFactory()
servo = AngularServo(12, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=pigpio_factory)
servo.angle = 126.5  # หมุนตัว servo มุม 90 องศา
                     # ยิ่งค่าเยอะ = ซ้าย
                     # ยิ่งค่าน้อย = ขวา
# 70 องศา = ขวาสุด
# 180 องศา = ซ้ายสุด
sleep(1)