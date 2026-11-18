# Number Guessing Game

import random

secret_number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        print("Number of attempts:", attempts)
        break



# output
# Guess the number between 1 and 100.
# Enter your guess: 23
# Too high! Try again.
# Enter your guess: 453
# Too high! Try again.
# Enter your guess: 123
# Too high! Try again.
# Enter your guess: 12
# Too low! Try again.
# Enter your guess: 100
# Too high! Try again.
# Enter your guess: 99
# Too high! Try again.
# Enter your guess: 89
# Too high! Try again.
# Enter your guess: 87
# Too high! Try again.
# Enter your guess: 76
# Too high! Try again.
# Enter your guess: 65
# Too high! Try again.
# Enter your guess: 45
# Too high! Try again.
# Enter your guess: 34
# Too high! Try again.
# Enter your guess: 23
# Too high! Try again.
# Enter your guess: 12
# Too low! Try again.
# Enter your guess: 23
# Too high! Try again.
# Enter your guess: 13
# Too low! Try again.
# Enter your guess: 15
# Too low! Try again.
# Enter your guess: 16
# Too low! Try again.
# Enter your guess: 18
# Too high! Try again.
# Enter your guess: 17
# Correct! You guessed the number.
# Number of attempts: 20