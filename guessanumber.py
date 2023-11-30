import random
import sys

def playAgain():
    while True:
        play_Again = input("Play again? Y / N: ")
        if play_Again.lower() == "y":
            game()
            break
        elif  play_Again.lower() == "n":
            sys.exit()
        else:
            print("     Invalid input. Please enter Y or N")

def game():
    secretNumber = random.randint(1,50)
    print("Guess the number between 1 and 50!\n")

    for guessAttempt in range(1,6):
        while True:
            try:
                guess = input("Enter your guess: ")
                intGuess = int(guess)
                break
            except ValueError:
                print("     Please enter a number.\n")
            
        if intGuess > secretNumber:
            print("     Too high! Guess again\n")
                            
        elif intGuess < secretNumber:
            print("     Too low! Guess again\n")
                            
        else: 
             break
        
    if intGuess == secretNumber:
        print("WOOOOOOOOOOO YES! Guessed correctly in " + str(guessAttempt) + " guesses.\n")
        playAgain()
    else: 
        print("Ran out of guesses. The number was "+ str(secretNumber)+"\n")
        playAgain()

game()