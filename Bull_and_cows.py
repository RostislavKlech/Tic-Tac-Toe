"""
Druhý projekt do Engeto Online Python Akademie

Autor: Rostislav Klech
Email: KlechRostislav@seznam.cz
Discord: Rosta K
"""

import random

separator = 45*"-"
guessed_number = ["", "", "", ""]
guess = 1
help_variable = True

def generate_4digit_number():
    random_number = ["", "", "", ""]
    random_number[0] = str(random.randint(1,9))
    while len(set(random_number)) < 4:
        for i in range(1,4):
            random_number[i] = str(random.randint(0,9))
    return random_number

def is_number(number: str):
    while (not number.isnumeric()) or len(number) != 4 or number[0] == "0":
        print(separator)
        print("This is not 4 digit number. Try again: ")
        number = input("Enter a number: ")
    return list(number)
    

def is_correct(correct_number: list, guessed_number: list):
    if correct_number == guessed_number:
        return False
    else:
        return True

def bull(correct_number: list, guessed_number: list):
    bulls = 0
    for i in range(4):
        if correct_number[i] == guessed_number[i]:
            bulls += 1
    return bulls

def cow(correct_number: list, guessed_number: list):
    cows = 0
    for i in range(4):
        for j in range(4):
            if correct_number[i] == guessed_number[j]:
                cows += 1
    return cows


print("Hi there!")
print(separator)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(separator)

guessed_number = is_number(input("Enter a number: "))
correct_number = generate_4digit_number()

while is_correct(correct_number, guessed_number) or help_variable:
    help_variable = False
    bulls = bull(correct_number, guessed_number)
    cows = cow(correct_number, guessed_number)
   
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow")
    elif bulls == 1:
        print(f"{bulls} bull, {cows} cows")
    elif cows == 1:
        print(f"{bulls} bulls, {cows} cow")
    else:
        print(f"{bulls} bulls, {cows} cows.")
    
    print(separator)
    guessed_number = guessed_number = is_number(input("Enter a number: "))
    
    if guessed_number == correct_number:
        if guess < 4:
            print(f"Correct,  you've guessed the right number\nin {guess} guesses!")
            print(separator)
            print("That's amazing.")
        elif guess >= 4 and guess < 12:
            print(f"Correct,  you've guessed the right number\nin {guess} guesses!")
            print(separator)
            print("That's average.")
        else:
            print(f"Correct,  you've guessed the right number\nin {guess} guesses!")
            print(separator)
            print("That's not so good.")
    guess += 1

    
    	






