# The Perfect Guess Game

import random

randNumber = random.randint(0,20)
# print(randNumber)

userGuess  = None
guessCount = 0

while (userGuess != randNumber):
    userGuess = int(input("Enter a Guess Number : "))
    print("\n")

    guessCount +=1

    if (userGuess == randNumber):
        print("You Guessed it Right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it Wrong, Enter a Smaller Number")
        else:
             print("You guessed it Wrong, Enter a Greater Number")



print(f"You guessed the Number in {guessCount} attempt!")

# File Handling
# Store highest score in a text file

with open("highscore.txt","r") as f:
    highscore = int(f.read())


if (guessCount < highscore):
    print("You have just broken the High Score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guessCount))