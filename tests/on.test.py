from dockergpio import LED

red = LED("/dev/gpiochip0", 17)

red.write(True)