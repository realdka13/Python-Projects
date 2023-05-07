import RPi.GPIO as GPIO
import pygame
import pygame.display

##Setup Pygame Window
pygame.init()
background_color = (255,255,255)
(width, height) = (1, 1) #Screen Size

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Keyboard Input')
screen.fill(background_color)
font = pygame.font.SysFont("Times New Roman", 18)
##

running = True
while running:
    #Run while key is pressed
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print('W pressed')
    if pressed[pygame.K_s]:
        print('S pressed')
    if pressed[pygame.K_a]:
        print('A pressed')
    if pressed[pygame.K_d]:
        print('D pressed')
    
    #Run only once
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pressed[pygame.K_UP]:
            LEDStatus = "On"
            print(LEDStatus)
        if pressed[pygame.K_DOWN]:
            LEDStatus = "Off"
            print(LEDStatus)
