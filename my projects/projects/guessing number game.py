# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.

import random

MINNUM = 0
MAXNUM = 100

secretNumber = random.randint(MINNUM, MAXNUM)
guessedNumber = None
numberOfTries = 0
listOfGuessedNumbers = []

print("Let's play a game. I've randomly picked a number between " + str(MINNUM) + " and " + str(MAXNUM) + ". Try to guess it!")

while guessedNumber != secretNumber:
    print("Your guess: ")
    guessedNumber = int(input())
    
    if guessedNumber == secretNumber:
        numberOfTries += 1
        listOfGuessedNumbers.append(guessedNumber)
        print("Congrats! You guessed the number: " + str(guessedNumber) + " correctly!")
        print("The number of Your tries: " + str((numberOfTries)))
    elif guessedNumber < secretNumber:
        if not guessedNumber in listOfGuessedNumbers:
            numberOfTries += 1
        else:
            print("You already tried guessing this number.")
        print("The number you guessed is too small. Try again.")
        listOfGuessedNumbers.append(guessedNumber)
    else:
        if not guessedNumber in listOfGuessedNumbers:
            numberOfTries += 1
        else:
            print("You already tried guessing this number.")
        print("The number you guessed is too big. Try again.")
        listOfGuessedNumbers.append(guessedNumber)

# print("All the numbers You guessed: " + str(listOfGuessedNumbers))
