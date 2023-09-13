from matplotlib import pyplot as plt
from matplotlib import animation
from gpiozero import LED
import numpy as np
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 20

led_blue = LED(5)
led_red = LED(6)

fig = plt.figure()

ax = plt.axes(xlim=(0, 30), ylim=(15, 45))

line, = ax.plot(np.arange(30), np.ones(30, dtype=float) * np.nan, lw=1, c='blue', marker='d', ms=2)

h, t = Adafruit_DHT.read_retry(sensor, pin)

def init():
    return line

def animate(i):
    h, t = Adafruit_DHT.read_retry(sensor, pin)
    if t <= 25:
        led_blue.on()
        led_red.off()
    else:
        led_blue.off()
        led_red.on()
    print(f'Frame # {i} - Temperature = {t}')
    y = t
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=100, blit=False)

anim.save(f"/home/admin/RWP/S3/anim_temp_{int(time.time())}.gif", writer='pillow')

led_blue.off()
led_red.off()

plt.savefig(f"/home/admin/RWP/S3/anim_temp_{int(time.time())}.png") # Optional
