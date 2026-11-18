# Dice Simulator Using the Random Module

import random

while True:
    choice = input("Press Enter to roll the dice, or type q to quit: ").lower()

    if choice == "q":
        print("Thanks for playing!")
        break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("Dice 1:", dice1)
    print("Dice 2:", dice2)
    print("Total:", dice1 + dice2)
    print()

# output
# Press Enter to roll the dice, or type q to quit: 
# Dice 1: 2
# Dice 2: 6
# Total: 8

# Press Enter to roll the dice, or type q to quit: 