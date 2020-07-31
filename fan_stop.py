#!/usr/bin/python3.7

import pigpio

gpio_pin = 18
pi = pigpio.pi()

pi.set_mode(gpio_pin, pigpio.INPUT)
pi.stop()
