from gpiozero import LED
import psutil
from time import sleep
from datetime import datetime

led_yellow = LED(6)
led_red = LED(5)
led_green = LED(13)

while True:
    cpu_usage = psutil.cpu_percent(interval = 1, percpu = True)
    cpu_usage_mean = sum(cpu_usage) / len(cpu_usage)
    cpu_usage_mean = round(cpu_usage_mean, 3)
    print(f'CPU Usage Mean: {cpu_usage_mean}')
    if 4 > cpu_usage_mean > 2:
        led_yellow.on()
        led_red.off()
        led_green.off()
    elif cpu_usage_mean >= 4:
        led_yellow.off()
        led_red.on()
        led_green.off()
    else:
        led_red.off()
        led_yellow.off()
        led_green.on()
    sleep(1)
    led_yellow.off()
    led_red.off()
    led_green.off()
