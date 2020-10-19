# we are going to create ***Number guessing Game 😀***
# global declaration...... 
import random 
#Fixed_number = 47
Bool = False
count=7
# Instructions of game.......
def game_logo():
    print("\n*****Number guessing game*****\n")
    print("  welcome in the game \U0001F603 \n")
    print("There are some instructions \U0001F606 :\n")
    print("1.you have to choose a number from 1 to 100")
    print("2.you have 7 chance to playing \n")
    print("3.if you would like to quit the game put   number 4")
    print(" I hope you like it \U0001F642\n let's start...... \U0001F44D  ")

# working game......... 
def game_work():
    Fixed_number = random.randint(1,100)
    guess_number=int(input("\nguess any number\U0001F914: "))
    if guess_number == 4 :
        print("Game Over")
        return True 
    elif guess_number==Fixed_number :
        print("congratulations!!\nyou won the Game")
        count+=1
        return True
    elif guess_number>Fixed_number :
        print("you guessed high \U0001F62C")
    else :
        print("you guessed low \U0001F62C")
      
# Gaming loop Manage 
def game_loop():
    i=0
    Count = 6
    while i<7 and game_work()!=True :
          while Count>=0:
              if Count>0:
                  print(f"don't be upset you still have {Count} chance")
                  print("Try again ")
                  break 
              else :
                  print("sorry you don't have chance anymore \nyou lose \U0001F602")
                  break
          Count-=1
          i+=1
        
def game_start():
    game_logo()
    
    game_loop()
    
# game going to start...... 
game_start()
