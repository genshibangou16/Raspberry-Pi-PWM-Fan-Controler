#!/usr/bin/python3.7

#!/usr/bin/python3.7

import pigpio
import time
import datetime

pin = 18
pi = pigpio.pi()

top = 1000000
bottom = 200000
hz_day = 60
hz_night = 160000
high = 80
low = 40
x_range = high - low

def get_duty(temp):
    now = datetime.datetime.now().hour
    if now >= 8 and now < 23:
        hz = hz_day
    else:
        hz = hz_night
    if high <= temp:
        duty = top
    elif temp <= low:
        duty = bottom
    else:
        x = temp - low
        duty = int(bottom + (top - bottom) * x * x / x_range / x_range)
    return hz, duty

pi.set_mode(pin, pigpio.OUTPUT)
pi.write(pin, 1)
time.sleep(30)

def fork():
    while True:
        i = 0
        temp = 0
        for i in range(5):
            with open('/sys/class/thermal/thermal_zone0/temp') as f:
                temp += int(f.read())
            time.sleep(1)
        temp /= 5000
        rs = get_duty(temp)
        pi.hardware_PWM(pin, rs[0], rs[1])

if __name__ == '__main__':
    fork()
