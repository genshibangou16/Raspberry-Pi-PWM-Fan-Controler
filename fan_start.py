#!/usr/bin/python3.7

import pigpio
import time
import subprocess
import os
import sys
import datetime

gpio_pin = 18
pi = pigpio.pi()

top = 1000000
bottomL = 220000
freqL = 150000
bottomH = 500000
freqH = 8333000
high = 70
low = 40

def get_temp():
    return float(subprocess.run('cat /sys/class/thermal/thermal_zone0/temp', shell=True, encoding='utf-8', stdout=subprocess.PIPE).stdout) / 1000

def get_duty(temp = low):
    now = datetime.datetime.now().hour
    if now >= 8 and now < 23:
        hz = freqH
        btm = bottomH
    else:
        hz = freqL
        btm = bottomL
    if high < temp:
        rs = top
    elif temp < low:
        rs = btm
    else:
        rs = int(btm + ((top - btm) / (high -low)) * (temp - low))
    return hz, rs

def pwm():
    pi.set_mode(gpio_pin, pigpio.OUTPUT)
    pi.write(gpio_pin, 1)
    while True:
        count = 0
        temp = 0
        while count < 30:
            temp += get_temp()
            count += 1
            time.sleep(1)
        temp /= 30
        duty = get_duty(temp)
        pi.hardware_PWM(gpio_pin, duty[0], duty[1])

def fork():
    pid = os.fork()
    if pid > 0:
        f = open('/run/fan.pid','w')
        f.write(str(pid)+"\n")
        f.close()
        sys.exit()
    if pid == 0:
        pwm()

if __name__ == '__main__':
    fork()
