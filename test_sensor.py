from gpiozero import Servo, Button, DistanceSensor, RGBLED
from colorzero import Color
from time import sleep
from tkinter import *
from tkinter.ttk import *

ultrasonic = DistanceSensor(
    echo=22, trigger=27, max_distance=1, threshold_distance=.05)
while True:
    print(ultrasonic.distance)
    sleep(.5)
