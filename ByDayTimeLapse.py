from datetime import datetime, date, time
import time
from picamera import PiCamera

## PiCamera
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1920,1080)
##

##USER SETTINGS
inputNumberOfPics = 0
inputStartHour = 0
inputStartMin = 0
inputStartSec = 0
inputTakePictureMin = 0
inputTakePictureSec = 0
###

### GET USER INPUT
print('Currently set to take pictures every 20 minutes')
print('')
inputNumberOfPics = int(input('Enter Number of Pictures to Take: '))
inputStartHour = int(input('Enter HOUR to Start(0 - 23): '))
inputStartMin = int(input('Enter MINUTE to Start(0 - 59): '))
inputStartSec = int(input('Enter SECOND to Start(0 - 59): '))
#inputTakePictureMin = int(input('Enter on what MINUTE to take Pictures(0 - 59): '))
#inputTakePictureSec = int(input('Enter on what SECOND to take Pictures(0 - 59): '))
###

print('')
print(datetime.now().strftime('Program Started: %Y-%m-%d %H:%M:%S\n')) #Print full time once

numberOfPics = 0 #Kepp track of number of pictures already taken
canStart = 0 #Keep track of when to start taking pictures

while canStart == 0: #Start Time for taking pictures
    goTimeHour = int(datetime.now().strftime('%H')) #Get Current Hour
    goTimeMin = int(datetime.now().strftime('%M')) #Get Current Minute
    goTimeSec = int(datetime.now().strftime('%S')) #Get Current Second

    if goTimeHour == inputStartHour and goTimeMin == inputStartMin and goTimeSec == inputStartSec:
        canStart = 1;
        print(datetime.now().strftime('Started Taking Pictures: %H:%M:%S\n')) #Display When Program Started Taking Pictures

        print('Picture Taken') #Take Pic One
        currentTime = datetime.now().strftime('%Y-%m-%d_%H:%M\n') #Take and name picture at current time
        camera.capture('/home/pi/Camera/%s.jpg' % currentTime)


        print(datetime.now().strftime('%H:%M:%S\n')) #Print time of picture taken
        time.sleep(1)


while numberOfPics + 1 != inputNumberOfPics: #Stop after taking 5 pictures
    goTimeHour = int(datetime.now().strftime('%H')) #Get Current Hour
    goTimeMin = int(datetime.now().strftime('%M')) #Get Current Minute
    goTimeSec = int(datetime.now().strftime('%S')) #Get Current Second

##Print the Time(For Debugging)
##    print(goTimeHour)
##    print(goTimeMin)
##    print(goTimeSec)
##    print('\n')

#### and goTimeMin == inputTakePictureMin (Put this on the line below when finished)
    if goTimeMin == 0 or goTimeMin == 20 or goTimeMin == 40: #inputTakePictureSec: Check if time
        print('Picture Taken:') #Take Picture
        currentTime = datetime.now().strftime('%Y-%m-%d_%H:%M\n') #Take and name picture at current time
        camera.capture('/home/pi/Camera/%s.jpg' % currentTime)
        print(datetime.now().strftime('%H:%M:%S\n')) #Print time of picture taken

        numberOfPics = numberOfPics + 1 #Increment numberOfPics
        time.sleep(65) #Wait 65 seconds to avoid taking 2 pictures
        
    time.sleep(.15)

print('Time Lapse Complete!')
