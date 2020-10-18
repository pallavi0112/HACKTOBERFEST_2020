# stone paper cesior game
def stone_paper_cesior(you, com):
    for i in range(1,5):
        if you == com:
            return 0
        elif you == "stone" and com == "paper":
            return -1
        elif you == "paper" and com == "stone":
            return 1
        elif you == "cesior"  and com == "paper":
            return 1
        elif you == "paper" and com == "cesior":
            return -1
        elif you == "stone" and com == "cesior":
            return 1
        elif you == "cesior" and com == "stone":
            return -1
   
import random
com = ""
for i in range(1, 5):
    com_num =  random.randint(0,100)
    if com_num >= 0 and com_num <= 33:
        com = "stone"
    elif com_num > 33 and com_num <= 66:
        com = "paper"
    elif com_num > 66 and com_num <=99:
        com = "cesior"


    you = input("Enter the Stone/Paper/Cesior to the user: ")
    result = stone_paper_cesior(you, com)
    print("computer is choose = ", com, "\n user in choose =",you)
    if result == 0:
        print("*****Drow the match******")
    elif result == 1:
        print("*****You win*****" )
    elif result == -1:
        print("*****you loss*****")

print("••••••••••••>Yor are Maximum use this game and you are exit:<••••••••••••")

