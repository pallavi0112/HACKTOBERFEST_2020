import random
while True:
  ans = input("Enter 'y' to roll the dice, enter 'n' to quit: ")
  if ans == 'y':
    print(random.randint(1,6))
  elif ans == 'n':
    break
  else:
    print("Incorrect input")
