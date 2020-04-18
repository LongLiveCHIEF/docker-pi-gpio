from dockergpio import LED

red = LED(17, "/dev/gpiochip0")

red.write(True)