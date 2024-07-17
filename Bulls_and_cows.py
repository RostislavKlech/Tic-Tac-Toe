"""
Druhý projekt do Engeto Online Python Akademie

Autor: Rostislav Klech
Email: KlechRostislav@seznam.cz
Discord: Rosta K
"""

import random

separator = 50*"-"
guess = 1

def generate_4digit_number():
    random_number = ["", "", "", ""]
    random_number[0] = str(random.randint(1,9))
    while len(set(random_number)) < 4:
        for i in range(1,4):
            random_number[i] = str(random.randint(0,9))
    return random_number

def is_number(number: str, guess: int):
    guesses = guess
    while (not number.isnumeric()) or len(set(number)) != 4 or number[0] == "0":
        print(separator)
        print("This is not 4 digit number where every digit is unique. Try again: ")
        number = input("Enter a number: ")
        guesses += 1
    return list(number), guesses
    

def is_correct(correct_number: list, guessed_number: list):
    if correct_number == guessed_number:
        return False
    else:
        return True

def bull_and_cow(correct_number: list, guessed_number: list):
    bulls = 0
    cows = 0
    for number in correct_number:
        if number in guessed_number:
            if correct_number.index(number) == guessed_number.index(number):
                bulls += 1
            else:
                cows += 1
    return bulls, cows


print("Hi there!")
print(separator)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(separator)

correct_number = generate_4digit_number()
guessed_number, guess = is_number(input("Enter a number: "), guess)

if correct_number == guessed_number:
    print(separator)
    print(f"Correct,  you've guessed the right number\nin {guess} guesses!")
    if guess == 1:
        print("That's unbelievable!")
    elif guess > 1 and guess < 4:
        print("That's amazing.")
    elif guess >= 4 and guess < 12:
        print("That's average.")
    else:
        print("That's not so good.")
else:
    while is_correct(correct_number, guessed_number):
        guess += 1
        bulls, cows = bull_and_cow(correct_number, guessed_number)
   
        if bulls == 1 and cows == 1:
            print(f"{bulls} bull, {cows} cow")
        elif bulls == 1:
            print(f"{bulls} bull, {cows} cows")
        elif cows == 1:
            print(f"{bulls} bulls, {cows} cow")
        else:
            print(f"{bulls} bulls, {cows} cows.")
    
        print(separator)
        guessed_number, guess = is_number(input("Enter a number: "), guess)
    
        if guessed_number == correct_number:
            if guess < 4:
                print(separator)
                print(f"Correct,  you've guessed the right number\nin {guess} guesses!")
                print("That's amazing.")
                break
            elif guess >= 4 and guess < 12:
                print(separator)
                print(f"Correct,  you've guessed the right number\nin {guess} guesses!")
                print("That's average.")
                break
            else:
                print(separator)
                print(f"Correct,  you've guessed the right number\nin {guess} guesses!")
                print("That's not so good.")
                break
    
        

  

    
    	






