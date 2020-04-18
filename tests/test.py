from dockergpio import LED
import subprocess

red = LED(17, "/dev/gpiochip0")

red.write(True)