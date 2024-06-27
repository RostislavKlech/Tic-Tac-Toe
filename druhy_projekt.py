"""
Druhý projekt do Engeto Online Python Akademie

Autor: Rostislav Klech  
Email: KlechRostislav@seznam.cz
Discord: Rosta K
"""

separator = 45*"="
field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win_O = ["O", "O", "O"]
win_X = ["X", "X", "X"]


def current_field(field: list):
    """
    Creates current field
    """
    separator_ttt = "+---+---+---+"
    top = "| " + field[0] + " | " + field[1] + " | " + field[2] + " |" 
    center = "| " + field[3] + " | " + field[4] + " | " + field[5] + " |"
    bottom = "| " + field[6] + " | " + field[7] + " | " + field[8] + " |"
    print(separator_ttt)
    print(top)
    print(separator_ttt)
    print(center)
    print(separator_ttt)
    print(bottom)
    print(separator_ttt)

def change_field(row: list, position: int, symbol: str):
    row[position-1] = symbol



print("Welcome to Tic Tac Toe")
print(separator)
print("GAME RULES:")
print("""Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or            
* diagonal row.
The layout of the numbers corresponds 
to the layout on the mobile phone.""")
print(separator)
print("Let's start the game.")
print(separator)
current_field(field)
print(separator)


while ([field[0], field[1], field[2]] != win_O and 
       [field[0], field[1], field[2]] != win_X and 
       [field[3], field[4], field[5]] != win_O and 
       [field[3], field[4], field[5]] != win_X and
       [field[6], field[7], field[8]] != win_O and 
       [field[6], field[7], field[8]] != win_X and 
       [field[0], field[4], field[8]] != win_O and 
       [field[0], field[4], field[8]] != win_X and
       [field[6], field[4], field[2]] != win_O and 
       [field[6], field[4], field[2]] != win_X and
       [field[0], field[3], field[6]] != win_O and
       [field[0], field[3], field[6]] != win_X and
       [field[1], field[4], field[7]] != win_O and
       [field[1], field[4], field[7]] != win_X and
       [field[2], field[5], field[8]] != win_O and
       [field[2], field[5], field[8]] != win_X):
    print(separator)
    input_O = input("Player O | Please enter your move number: ")
    print(separator)
    while (input_O not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) or field[int(input_O)-1] == "X" or field[int(input_O)-1] == "O":
        if input_O not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Input is not number btw. 1 and 9. Try again:")
            input_O = input("Player O | Please enter your move number: ")
            print(separator)
        elif field[int(input_O)-1] == "X":
            print("Place is already taken by X. Try again:")
            input_O = input("Player O | Please enter your move number: ")
            print(separator) 
        elif field[int(input_O)-1] == "O":
            print("Place is already taken by O. Try again:")
            input_O = input("Player O | Please enter your move number: ")
            print(separator)
    change_field(field, int(input_O), "O")
    current_field(field)
    if ([field[0], field[1], field[2]] == win_O or       
       [field[3], field[4], field[5]] == win_O or 
       [field[6], field[7], field[8]] == win_O or  
       [field[0], field[4], field[8]] == win_O or 
       [field[6], field[4], field[2]] == win_O or
       [field[0], field[3], field[6]] == win_O or
       [field[1], field[4], field[7]] == win_O or
       [field[2], field[5], field[8]] == win_O):
        print(separator)
        print("Congratulations, the player O WON!")
        print(separator)
        break
    if " " not in field:
        print(separator)
        print("It is a draw!")
        print(separator)
        break
    print(separator)
    input_X = input("Player X | Please enter your move number: ")
    print(separator)
    while (input_X not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) or field[int(input_X)-1] == "X" or field[int(input_X)-1] == "O":
        if input_X not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Input is not number btw. 1 and 9. Try again:")
            input_X = input("Player O | Please enter your move number: ")
            print(separator)
        elif field[int(input_X)-1] == "X":
            print("Place is already taken by X. Try again:")
            input_X = input("Player O | Please enter your move number: ") 
            print(separator)
        elif field[int(input_X)-1] == "O":
            print("Place is already taken by O. Try again:")
            input_X = input("Player O | Please enter your move number: ")
            print(separator)
    change_field(field, int(input_X), "X")
    current_field(field) 
    if ([field[0], field[1], field[2]] == win_X or       
       [field[3], field[4], field[5]] == win_X or 
       [field[6], field[7], field[8]] == win_X or  
       [field[0], field[4], field[8]] == win_X or 
       [field[6], field[4], field[2]] == win_X or
       [field[0], field[3], field[6]] == win_X or
       [field[1], field[4], field[7]] == win_X or
       [field[2], field[5], field[8]] == win_X):
        print(separator)
        print("Congratulations, the player X WON!")
        print(separator)
        break
    #REMIZA PO TAHU X NEMUZE NASTAT  



    
    
            


    



