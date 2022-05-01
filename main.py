from gpiozero import DistanceSensor
from time import sleep
from tkinter import *
from tkinter.ttk import *
import RPi.GPIO as GPIO


sleepTime1 = 1
sleepTime2 = 0.5

sensor = DistanceSensor(echo=22, trigger=27,
                        max_distance=.2, threshold_distance=.05)
# tkinter GUI code
bottomPin = 24      # bottom
midRightPin = 4     # mid right
midLeftPin = 17     # mid left
topRightPin = 18    # top right
topLeftPin = 23     # top left

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(bottomPin, GPIO.OUT)
GPIO.setup(midRightPin, GPIO.OUT)
GPIO.setup(midLeftPin, GPIO.OUT)
GPIO.setup(topRightPin, GPIO.OUT)
GPIO.setup(topLeftPin, GPIO.OUT)

bottomServo = GPIO.PWM(bottomPin, 50)
midRightServo = GPIO.PWM(midRightPin, 50)
midLeftServo = GPIO.PWM(midLeftPin, 50)
topRightServo = GPIO.PWM(topRightPin, 50)
topLeftServo = GPIO.PWM(topLeftPin, 50)

smallSleep = .5
bigSleep = 1.3

RUNNING = True


def initServos():
    global smallSleep
    global bigSleep
    bottomServo.start(3)  # bottom
    sleep(smallSleep)
    midRightServo.start(3)  # mid right
    sleep(smallSleep)
    midLeftServo.start(12.5)  # mid left
    sleep(smallSleep)
    topRightServo.start(3)  # outer right
    sleep(smallSleep)
    topLeftServo.start(12.5)  # outer left
    sleep(smallSleep)


initServos()
master = Tk()
master.attributes('-fullscreen', True)

# Variables for lables
count = IntVar()
i = 0


def ServoRun():
    global smallSleep
    global bigSleep
    master.configure(background='red')
    master.update()

    topLeftServo.ChangeDutyCycle(3)
    sleep(bigSleep)
    topLeftServo.ChangeDutyCycle(12.5)
    sleep(bigSleep)

    topRightServo.ChangeDutyCycle(12.5)
    sleep(bigSleep)
    topRightServo.ChangeDutyCycle(3)
    sleep(bigSleep)

    bottomServo.ChangeDutyCycle(12.5)
    sleep(bigSleep)
    bottomServo.ChangeDutyCycle(3)
    sleep(bigSleep)

    midLeftServo.ChangeDutyCycle(12.5/1.6)
    sleep(smallSleep-.4)
    midRightServo.ChangeDutyCycle(12.5/1.6)
    sleep(bigSleep)

    midLeftServo.ChangeDutyCycle(12.5)
    sleep(smallSleep-.4)
    midRightServo.ChangeDutyCycle(3)
    sleep(bigSleep)


def ultrasonic():
    master.configure(background='blue')
    master.update()
    while True:
        print("Distance: ", sensor.distance * 100)
        sleep(.15)
        RUNNING = False
        if (sensor.distance >= .2):
            RUNNING = True
            break


def run():
    global smallSleep
    global bigSleep
    ServoRun()
    sleep(1)
    ultrasonic()
    master.configure(background='green')
    master.update()
    # Update count for display
    global count
    global i
    i += 1
    count.set(i)
    master.update()


# top label
Label(master, text="Smart Clothes Folder",
      background='white', font=('Arial', 40)).pack(side='top')

# Center Label's
# Clothes Counter reading
Label(master, text="Number of clothes:", background='lightGreen',
      font=('Arial', 25)).place(relx=0.45, rely=.35, anchor=NE)
Label(master, textvariable=count, background='lightGreen',
      font=('Arial', 25)).place(relx=0.55, rely=.35, anchor=NE)

# Start button
Button(master, text="Run", command=run).place(
    relx=0.5, rely=.55, anchor=CENTER)

# Quit button
Button(master, text="Quit", command=master.destroy).place(
    relx=0.5, rely=.95, anchor=CENTER)

while (RUNNING):
    master.update()
    sleep(0.65)
