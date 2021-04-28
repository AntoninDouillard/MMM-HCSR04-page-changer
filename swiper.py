#!/usr/bin/python3
# coding: utf-8

import RPi.GPIO as GPIO
import time
import json
import sys
import re
from statistics import mean
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins from node_helper config
numbers = re.compile(r'\d+')
gpio_numbers = numbers.findall(sys.argv[1])

GPIO_TRIGGER = int(gpio_numbers[0])
GPIO_ECHO = int(gpio_numbers[1])
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def to_node(type, message):
    try:
        print(json.dumps({type: message}))
    except Exception:
        pass

    sys.stdout.flush()


def get_distances():
    d = distance()    
    result = {"distance": d}
    to_node("result", result)

 
def distance():

    values = []

    # To avoir measurement errors, we average the last 10 results
    for _ in range(1, 10):
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
 
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
 
        StartTime = time.time()
        StopTime = time.time()
 
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
 
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
 
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
 
        values.append(distance)

    return mean(values)


if __name__ == '__main__':

    to_node("info", 'Python script for MMM-HCSR04-page-changer has started')
    try:
        while True:
            get_distances()
            time.sleep(0.3)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
