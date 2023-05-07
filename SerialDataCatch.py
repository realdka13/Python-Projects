#TODO
#Reformat to own code
#Rename variables
#Terminate Serial Coneection when done
#Needs packet Error checking <-check for malformed packet

import serial #PySerial
import time

arduinoData = serial.Serial('com3', '115200') #Come up with solution to find this this automatically??
time.sleep(1) #Give serial port time to setup

while(1 == 1):  #Loop()
    while(arduinoData.inWaiting() == 0): #Waits until data in the serial port, pops out when it reads data
        pass

    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8') #Strips extra stuff (B',/r,/n) off of packet
    splitPacket = dataPacket.split(',')
    aCal = float(splitPacket[0])
    gCal = float(splitPacket[1])
    mCal = float(splitPacket[2])
    sCal = float(splitPacket[3])
    pitch = float(splitPacket[4])
    roll = float(splitPacket[5])
    yaw = float(splitPacket[6])

    print("A_Cal =" , aCal, "G_Cal =" , gCal, "M_Cal =" , mCal, "S_Cal =", sCal, "Pitch =", pitch, "Roll =", roll, "Yaw", yaw)
