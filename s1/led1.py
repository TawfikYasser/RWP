from gpiozero import LED

red_led = LED(20)

while True:
    red_led.on()
