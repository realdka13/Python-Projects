##TODO, Limit number of guesses
#Clean Screen

from random import *

def PlayAgain():###
    playerResponse = input('Would you like to play again? y/n\n')
    print(playerResponse)

    if playerResponse == 'y':#Start Game Again
        PlayGame()
    else:
        print('See you next time!')    
###

def PlayGame():###
#Initializing
    hiddenNumber = randint(1,100)#Generate Random Number
    playerWon = False #Has the player won?
    print('I have a random nunmber in mind between 1 and 100. Try and guess it!\n')

#Play Game
    while playerWon == False:
        while True:
            try:
                playerGuess = input('Make a Guess: \n')#Get input from player
                playerGuessINT = int(playerGuess)#Convert playerGuess to int
                break
            except ValueError:
                print('Please Enter a Number\n')

        if playerGuessINT == 0:#Display Correct Number(For Debugging)
            print(hiddenNumber)

        elif playerGuessINT == hiddenNumber:#Guessing Correct Number
            print('You are Correct!\n')
            playerWon = True
            PlayAgain()

        elif playerGuessINT < hiddenNumber:#Player guesses too low
            print('My number is higher\n')

        elif playerGuessINT > hiddenNumber:#Player guesses too high
            print('My number is lower\n')
###

PlayGame() #Start Game
