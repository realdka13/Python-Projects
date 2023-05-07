import RPi.GPIO as gpio
import time

#Setup GPIO
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#Setup Pins
gpio.setup(17,gpio.OUT) #LEDOne
gpio.setup(18,gpio.OUT) #LEDTwo
gpio.setup(27,gpio.OUT) #LEDThree
gpio.setup(22,gpio.OUT) #LEDFour
gpio.setup(10,gpio.OUT) #Buzzer
gpio.setup(23,gpio.IN,pull_up_down = gpio.PUD_DOWN)#Button

#INIT
gpio.output(17,gpio.LOW)
gpio.output(18,gpio.LOW)
gpio.output(27,gpio.LOW)
gpio.output(22,gpio.LOW)
gpio.output(10,gpio.LOW)


#Run CountDown
try:
    while True:
        if gpio.input(23) == gpio.HIGH:#Button
            print('Button Pushed')
            
            #ONE
            gpio.output(17,gpio.HIGH)#LED
            gpio.output(10,gpio.HIGH)#Buzzer
            print('3')
            time.sleep(.5)
            gpio.output(10,gpio.LOW)#Buzzer
            time.sleep(.5)

            #TWO
            gpio.output(18,gpio.HIGH)#LED
            gpio.output(10,gpio.HIGH)#Buzzer
            print('2')
            time.sleep(.5)
            gpio.output(10,gpio.LOW)#Buzzer
            time.sleep(.5)

            #THREE
            gpio.output(27,gpio.HIGH)#LED
            gpio.output(10,gpio.HIGH)#Buzzer
            print('1')
            time.sleep(.5)
            gpio.output(10,gpio.LOW)#Buzzer
            time.sleep(.5)
            
            #RED LEDS OFF  
            gpio.output(17,gpio.LOW)
            gpio.output(18,gpio.LOW)
            gpio.output(27,gpio.LOW)

            #FLASH GREEN LED
            for x in range(0,7):
                    print('Go!')
                    gpio.output(22,gpio.LOW)#LED
                    gpio.output(10,gpio.LOW)#Buzzer
                    time.sleep(.1)
                    gpio.output(22,gpio.HIGH)#LED
                    gpio.output(10,gpio.HIGH)#Buzzer
                    time.sleep(.1)
                    gpio.output(22,gpio.LOW)#LED
                    gpio.output(10,gpio.LOW)#Buzzer

	
except KeyboardInterrupt:
        print('Actions Cancelled')
        gpio.cleanup()
