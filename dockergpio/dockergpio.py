from periphery import GPIO

def LED(gpiochip, pin):
    try:
        led = GPIO(gpiochip, pin, "out")
        return led
    except TypeError as e:
        print('{}'.format(e))
    except LookupError:
        print('GPIO line was not found by the provided name')
    except:
        print('unknown error occurred')

def ledOn(gpiochip, pin):
    try:
        led = GPIO(gpiochip, pin, "out")
        led.write(True)
    except TypeError as e:
        print('{}'.format(e))
    except LookupError:
        print('GPIO line was not found by the provided name')
    except:
        print('unknown error occurred')