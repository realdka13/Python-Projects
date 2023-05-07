import RPi.GPIO as gpio
import time

##Initialize
def Init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

##Move Forward Auto
def Forward(tf):
    print('Moving Forward')
    gpio.output(17, False)#Right Side Back
    gpio.output(22, True)#Right Side For
    gpio.output(23, False)#Left Side Back
    gpio.output(24, True)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(22, False)
    gpio.output(24, False)

##Move Backward Auto
def Backward(tf):
    print('Moving Backward')
    gpio.output(17, True)#Right Side Back
    gpio.output(22, False)#Right Side For
    gpio.output(23, True)#LeftSide Back
    gpio.output(24, False)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(17, False)
    gpio.output(23, False)

##Rotate Right Auto
def Right(tf):
    print('Rotating Right')
    gpio.output(17, False)#Right Side Back
    gpio.output(22, True)#Right Side For
    gpio.output(23, True)#LeftSide Back
    gpio.output(24, False)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(22, False)
    gpio.output(23, False)

##Rotate Left Auto
def Left(tf):
    print('Rotating Left')
    gpio.output(17, True)#Right Side Back
    gpio.output(22, False)#Right Side For
    gpio.output(23, False)#LeftSide Back
    gpio.output(24, True)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(17, False)
    gpio.output(24, False)


##Run
Init()

Forward(2)
Backward(2)
Right(2)
Left(2)
