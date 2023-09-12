from gpiozero import DistanceSensor, LED
from time import sleep
from gpiozero import Servo

sensor = DistanceSensor(echo = 21, trigger = 20)
led_blue = LED(16)
led_red = LED(12)
led_green = LED(6)
led_yellow = LED(5)
servo = Servo(18)

while True:
    if sensor.distance * 100 > 50:
        led_red.on()
        led_blue.off()
        led_green.off()
        led_yellow.off()
        servo.min()
        print(f'Distance  = {sensor.distance * 100}')
    elif 50 > sensor.distance * 100 > 30:
        led_red.off()
        led_blue.on()
        servo.max()
        led_green.off()
        led_yellow.off()
        print(f'Distance  = {sensor.distance * 100}')
    elif 30 > sensor.distance * 100 > 10:
        led_red.off()
        led_blue.off()
        led_green.off()
        servo.min()
        led_yellow.on()
        print(f'Distance  = {sensor.distance * 100}')
    elif sensor.distance * 100 < 10:
        led_red.off()
        servo.min()
        led_blue.off()
        led_green.on()
        led_yellow.off()
        print(f'Distance  = {sensor.distance * 100}')
    sleep(1)
