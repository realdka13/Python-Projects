import board
import neopixel #Using BCM numbering
import RPi.GPIO as GPIO
import datetime
import time

upTime = 30
maxTimeInS = 60

#Buzzer
buzzerPin=4

#Button Test
buttonPin=15

#Weight Sensor
sensorPressed = False

#Countdown Variables
timerStarted = False
countingDown = True

#Pixel Variables
pixel_pin = board.D18
num_pixels = 12
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.25, auto_write=False)

#TimerVariables
targetTime = datetime.datetime.now()
LEDUpdateTimes = []
standUpTime = datetime.datetime.now()
stoodUp = False

#Count Up Variable
upTargetTime = datetime.datetime.now()
offTimerStart = False
upTargetSet = False

def Buzzer(beepType):
	if(beepType == 0):									#Test Beep
		GPIO.output(buzzerPin,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(buzzerPin,GPIO.LOW)
	elif(beepType == 1):									#Times up beep
		for i in range(3):
			for i in range(3):
				GPIO.output(buzzerPin,GPIO.HIGH)
				time.sleep(.075)
				GPIO.output(buzzerPin,GPIO.LOW)
				time.sleep(.075)
			time.sleep(.15)
	elif(beepType == 2):
		for i in range(2):
			GPIO.output(buzzerPin,GPIO.HIGH)
			time.sleep(.1)
			GPIO.output(buzzerPin,GPIO.LOW)
			time.sleep(.1)

#Sets the target time and sets timer variable to True
def TimerStart():
	global targetTime
	global timerStarted
	global countingDown

	targetTime = datetime.datetime.now() + datetime.timedelta(seconds = maxTimeInS)
	print("Target Time: %d:%d:%d" %(targetTime.hour,targetTime.minute,targetTime.second))
	timerStarted = True
	print("Start time: ", datetime.datetime.now(), "\n")
	countdingDown = True

#Will update the neopixel ring as time checkpoints are hit
def UpdatePixels(currentTime):
	global timerStarted
	global targetTime
	global sensorPressed

	if(timerStarted == True and len(LEDUpdateTimes) > 0 and sensorPressed):
		if(currentTime >= LEDUpdateTimes[0]):
			pixels[len(LEDUpdateTimes)-1] = (0,0,0) #Pixels are from 0-12
			pixels.show()
			print("Pixel Popped! Current Time: ",currentTime, "Next update time: ",LEDUpdateTimes[0],"Will pop pixel: ", len(LEDUpdateTimes)-1)
			LEDUpdateTimes.pop(0)
	elif(not countingDown):
		if(currentTime >= LEDUpdateTimes[0]):
			pixels[len(LEDUpdateTimes)-1] = (0,0,255) #Pixels are from 0-12
			pixels.show()
			print("Pixel Added! Current Time: ",currentTime, "Next update time: ",LEDUpdateTimes[0],"Will pop pixel: ", len(LEDUpdateTimes)-1)
			LEDUpdateTimes.pop(0)


#Calculates time checkpoits
def CalculateUpdates(currentTime):
	global LEDUpdateTimes
	global maxTimeInS
	global num_pixles
	global stoodUp
	global standUpTime
	global targetTime
	global countingDown

	if(countingDown):
		secondsPerLED = maxTimeInS/num_pixels
		if(not stoodUp):
			print("\nTarget Times: ")
			for i in range(12):
				nextTime = currentTime + datetime.timedelta(seconds = secondsPerLED*(i+1))
				LEDUpdateTimes.append(nextTime);
				print(i,":",LEDUpdateTimes[i])
			print("\n")
		elif(stoodUp):

			secondsLeft = targetTime - standUpTime 						#Calculate time left
			print("SecondsLeft: ", secondsLeft)
			targetTime = (currentTime - standUpTime) + targetTime 				#Calculate new target time
			print("New target Time: ",targetTime)
			LEDIndex = len(LEDUpdateTimes) 							#Calculate new times startin at the same LED Update times index
			LEDUpdateTimes.clear()
			for i in range(LEDIndex):
				nextTime = currentTime + datetime.timedelta(seconds = secondsPerLED*(i+1))
				LEDUpdateTimes.append(nextTime);
				print(i,":",LEDUpdateTimes[i])
			print("\n")
	elif(not countingDown):
		LEDUpdateTimes.clear()
		secondsPerLED = upTime/num_pixels
		print("\n Up Target Times: ")
		for i in range(12):
			nextTime = currentTime + datetime.timedelta(seconds = secondsPerLED*(i+1))
			LEDUpdateTimes.append(nextTime);
			print(i,":",LEDUpdateTimes[i])
		print("\n")

def CountOffTime():
	global offTimerStart
	global upTimerTarget
	global upTargetSet
	global countingDown
	global LEDUpdateTimes

	if(upTargetSet == False):
		upTimerTarget = datetime.datetime.now() + datetime.timedelta(seconds=upTime)
		print("Up Time Target: ",upTimerTarget)
		upTargetSet = True
		countingDown = False
		CalculateUpdates(datetime.datetime.now())
	elif(datetime.datetime.now() >= upTimerTarget):
		print("You can now be seated")
		LEDUpdateTimes.clear()
		pixels.fill((0,0,255))
		pixels.show()
		upTargetSet = False
		offTimerStart = False
		countingDown = True
		Buzzer(2)

#Check if Button Pressed
def CheckButton():
	global sensorPressed
	sensorPressed = not GPIO.input(buttonPin)

#1 time setups
def Setup():
	GPIO.setup(buzzerPin,GPIO.OUT)
	GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#Loop this
def Main():
	global timerStarted
	global stoodUp
	global standUpTime
	global targetTime
	global offTimerStart

	while True:
		currentTime = datetime.datetime.now() 						#Reset Current Time
		CheckButton()									#Update Button
		if(timerStarted == False and sensorPressed == True and offTimerStart == False): #Pressed Sensor(for now)
			pixels.fill((0,0,255))
			pixels.show()
			CalculateUpdates(currentTime)
			TimerStart()

		elif(timerStarted == True and sensorPressed == False and offTimerStart == False): #Timer started but gotten up
			if(not stoodUp):
				stoodUp = True
				standUpTime = datetime.datetime.now()
				print("\nUser Stood Up: ",standUpTime)

		elif(timerStarted == True and sensorPressed == True and offTimerStart == False): #Currently Sitting
			if(stoodUp):								#If user stood up, calculate new time
				if(currentTime < standUpTime + datetime.timedelta(seconds = upTime)):
					print("User Reseated: ", currentTime)
					CalculateUpdates(currentTime)
					stoodUp = False
				else:
					print("Reset Timer!")
					stoodUp = False
					offTimerStart = False
					timerStarted = False
					countingDown = True
					Buzzer(2)
					LEDUpdateTimes.clear()
					pixels.fill((0,0,255))
					pixels.show()
			elif(currentTime >= targetTime): 					#Timer Complete
				print("Time complete: ",currentTime)
				Buzzer(1)
				LEDUpdateTimes.clear()
				pixels.fill((0,0,0))
				pixels.show()							#Just in case the timing isnt quite right
				timerStarted = False
				offTimerStart = True
			else: 									#Timer counting
				print("Time Left: ", targetTime - currentTime ,end="\r")
		elif(timerStarted == False and sensorPressed == False and offTimerStart == True):
			CountOffTime()
		elif(timerStarted == False and sensorPressed == True and offTimerStart == True):
			Buzzer(1)
		UpdatePixels(currentTime)


if __name__ == '__main__':
	try:
		Setup()
		Main()
	except KeyboardInterrupt:
		print("\n\nKeyboard Inturrupt: Exiting")
		pixels.fill((0,0,0))
		pixels.show()
		GPIO.output(buzzerPin,GPIO.LOW)
		GPIO.cleanup()
