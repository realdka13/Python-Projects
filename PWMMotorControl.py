import RPi.GPIO as gpio
import time

##Move Forward Auto
def Forward(tf,spd):
    print('Moving Forward at', spd,'%')
    pwmOne.ChangeDutyCycle(spd)#Set Speed
    pwmTwo.ChangeDutyCycle(spd)#Set Speed
    gpio.output(17, False)#Right Side Back
    gpio.output(22, True)#Right Side For
    gpio.output(23, False)#Left Side Back
    gpio.output(24, True)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(22, False)
    gpio.output(24, False)

##Move Backward Auto
def Backward(tf,spd):
    print('Moving Backward at', spd,'%')
    pwmOne.ChangeDutyCycle(spd)#Set Speed
    pwmTwo.ChangeDutyCycle(spd)#Set Speed
    gpio.output(17, True)#Right Side Back
    gpio.output(22, False)#Right Side For
    gpio.output(23, True)#LeftSide Back
    gpio.output(24, False)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(17, False)
    gpio.output(23, False)

##Rotate Right Auto
def Right(tf,rightspd,leftspd):
    print('Rotating Right: Right side at', rightspd,'% ; Left side at', leftspd,'%')
    pwmOne.ChangeDutyCycle(rightspd)#Reset Speed
    pwmTwo.ChangeDutyCycle(leftspd)#Reset Speed
    gpio.output(17, False)#Right Side Back
    gpio.output(22, True)#Right Side For
    gpio.output(23, True)#LeftSide Back
    gpio.output(24, False)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(22, False)
    gpio.output(23, False)

##Rotate Left Auto
def Left(tf,rightspd,leftspd):
    print('Rotating Left: Right side at', rightspd,'% ; Left side at', leftspd,'%')
    pwmOne.ChangeDutyCycle(rightspd)#Reset Speed
    pwmTwo.ChangeDutyCycle(leftspd)#Reset Speed
    gpio.output(17, True)#Right Side Back
    gpio.output(22, False)#Right Side For
    gpio.output(23, False)#LeftSide Back
    gpio.output(24, True)#LeftSide For
    time.sleep(tf)
    #Stop Motors
    gpio.output(17, False)
    gpio.output(24, False)











###Run
try:
    ##Init
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(18, gpio.OUT)#PWM
    gpio.setup(25, gpio.OUT)#PWM
    pwmOne=gpio.PWM(18,1000)#Init PWM
    pwmTwo=gpio.PWM(25,1000)#Init PWM
    pwmOne.start(100)     ##Duty cycle has to stay above 50 for relevant torque
    pwmTwo.start(100)     ##Duty cycle has to stay above 50 for relevant torque
    ##


    Forward(1,100)
    Forward(2,50)
    Backward(1,100)
    Backward(2,50)
    Forward(.5,100)
    Right(1.5,100,100)
    Left(1.5,100,100)
    Right(1.5,100,0)
    Left(1.5,100,0)
    Right(1.5,0,100)
    Left(1.5,0,100)
    Backward(.5,100)

except KeyboardInterrupt:
    print('Actions Cancelled')
    gpio.cleanup()
