import RPi.GPIO as GPIO
from time import sleep


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


def initServos():
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


def ServoRun():
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


initServos()
ServoRun()
