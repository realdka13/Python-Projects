from vpython import *   #Visuals
import numpy as np      #For scientific computing in python
import serial
from serial.tools import list_ports
import math
import time


#Global Variables
simRunning = False
arduinoData = serial.Serial('com3','115200')

#GUI Functions
def LiveButton():
    liveButton.disabled = True
    analysisButton.disabled = False
    startStopSimButton.disabled = False
    connectionText.visible = True
    connectionIndicator.visible = True

def AnalysisButton():
    liveButton.disabled = False
    analysisButton.disabled = True
    startStopSimButton.disabled = True
    connectionText.visible = False
    connectionIndicator.visible = False

def StartStopSimButton():
    global simRunning
    if(simRunning):
        startStopSimButton.text = "Start Simulation"
        simRunning = False
    else:
        startStopSimButton.text = "Stop Simulation"
        simRunning = True


#Scene Setup
orientationScene = canvas(width=800, height=800, forward=vector(-1,-1,-1))
orientationScene.append_to_caption("\n")

connectionText = label(pixel_pos= True, pos=vec(45,10,0), text='Connection: ', box=False)
connectionIndicator = label(pixel_pos= True, pos=vec(90,9,0), text='•', box=False)

liveButton = button(text='Live', pos=orientationScene.title_anchor, bind=LiveButton)
analysisButton = button(text='Analysis', pos=orientationScene.title_anchor, bind=AnalysisButton)
startStopSimButton = button(text='Start Simulation', pos=orientationScene.caption_anchor, bind=StartStopSimButton)

LiveButton()


#3D Objects
pcb = box(length=2, width=2, height=.2, color=color.blue, opacity=0.5)
chip = box(length=.5, width=.5, height=.2,pos=vector(.75,.201,0), color=color.gray(.5), opacity=0.5)
BNO055 = compound([pcb,chip])
xAxisArrow = arrow(axis=vector(1,0,0), length=2, shaftwidth=.1, color=color.red)
yAxisArrow = arrow(axis=vector(0,1,0), length=2, shaftwidth=.1, color=color.green)
zAxisArrow = arrow(axis=vector(0,0,1), length=2, shaftwidth=.1, color=color.blue)


#Movement
while(True):
    if(simRunning):
        #Do nothing when no data found
        while(arduinoData.inWaiting() == 0):
            pass

        #Process Packet
        dataPacket = arduinoData.readline()
        dataPacket = str(dataPacket, 'utf-8')
        splitPacket = dataPacket.split(',')

        q0=float(splitPacket[0])
        q1=float(splitPacket[1])
        q2=float(splitPacket[2])
        q3=float(splitPacket[3])

        roll = math.atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
        pitch = -math.asin(2*(q0*q2-q3*q1))
        yaw = -math.atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3))

        #Vectors
        y=vector(0,1,0) #Helper always vertical vector, used to find s

        k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch)) #BNO055 forward vector
        s=cross(k,y) #BNO055 side vector
        v=cross(s,k) #BNO055 up vector

        vRot = v*cos(roll)+cross(k,v)*sin(roll) #The rotation of the v vector after applying Rodrigues' Rotation Formula

        #Setting position of object
        BNO055.axis = k
        BNO055.up = vRot

        #Vpython Delay
        rate(50)