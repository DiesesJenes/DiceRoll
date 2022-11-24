
import random

number_dices_to_roll = input("How much dice would you like to roll?: ")
roll = True

while roll:
    for dice in range(1, int(number_dices_to_roll) + 1):
        print(random.choice(range(1, 7)))

    choice = input("Do you want to roll again? Please answer wirth Yes or No: ")
    if choice == "yes" or choice == "Yes":
        number_dices_to_roll = input("How much dice would you like to roll this time?: ")
    else:
        roll = False

