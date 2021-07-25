"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell 
them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons 
from the very first exercise)

Extras:

- Keep the game going until the user types “exit”
- Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random

n = random.randint(1, 9)

user_response = "0"
retries = 0

while user_response != "exit":
    retries+=1
    user_response = input("Guess the number: ")
    if user_response != "exit":
        if int(user_response) == n:
            print("Congratulations! You get the number in the " + str(retries) + " try")
            retries = 0
            n = random.randint(1, 9)
            print("Playing again...\n\n")
        if int(user_response) < n:
            print("Too low!")
        if int(user_response) > n:
            print("Too high!")
    else:
        print("Leaving game...")
