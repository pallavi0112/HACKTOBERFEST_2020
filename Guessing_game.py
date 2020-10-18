# ****GUSSE THE NUMBER **** source code using function

import random
#Globle Declearation 
Bool = True
is_game_over = False
fixed_number = random.randint(1,50)


#Function of Logo and Instruction
def logo():
    print("********************WELCOME TO********************")
    print("***************NUMBER GUESSING GAME***************\n")
    print("Instruction : There is one winning number between 1 to 50 \n You have to find that number in 7 chance\n\n")

# Game working 
def game():
    num = input("Enter the number you guess :")
    if(num==fixed_number):
        print("\n\t\t Congratulation!!! You Win The game")
        return False
    elif(num>fixed_number):
        print("\n #### Number Is High ####")
        print("\n<<<< Sorry! Next Try >>>\n")
    else:
        print("\n #### Number Is Low ####\n")
        print("<<<< Sorry! Next Try >>>\n")
        is_game_over = True

# for looping
def game_loop():
    i = 0
    while(i<7 and game()!= False):
        i+=1
    if(is_game_over == False):
        print("\n\t\t########### Game Over ############\n\n")

# Game workflow
def start_game():
    logo()
    game_loop()

# To start the game
start_game()
