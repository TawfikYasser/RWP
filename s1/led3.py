from gpiozero import LED

red_led = LED(20)

while True:
    s = input()
    if s == "on":
        red_led.on()
    elif s == "off":
        red_led.off()
    else:
        print("invalid")
