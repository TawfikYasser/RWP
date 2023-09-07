from gpiozero import LED
from signal import pause

red_led = LED(20)

red_led.blink(1)
pause()
