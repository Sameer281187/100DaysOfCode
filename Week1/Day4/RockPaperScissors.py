import random
from contextlib import nullcontext

print("***********************Welcome to Rock Paper and Scissors game***********************")
game_values = ["Rock", "Paper", "Scissors"]
player_1_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

print("Player 1 chose: \n \n")
if player_1_selection == 0:
    print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
    ''')
elif player_1_selection == 1:
    print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'  
    ''')
elif player_1_selection == 2:
    print('''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
    ''')
else:
    print("You entered an invalid number. You lose")
    exit(1)

computer_selection = random.randint(0,2)

print("Computer chose: \n \n")
if computer_selection == 0:
    print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
    ''')
elif computer_selection == 1:
    print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'  
    ''')
else:
    print('''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
    ''')

winner = ""

if player_1_selection == computer_selection:
    winner = "Draw"
elif player_1_selection == 2 and computer_selection == 0:
    winner = "Computer"
elif computer_selection == 2 and player_1_selection == 0:
    winner = "Player 1"
else:
    winner = "Player 1" if player_1_selection > computer_selection else "Computer"

if winner == "Draw":
    print(f"The game ended in a {winner}")
elif winner == "Player 1":
    print("You Won")
else:
    print("You Lose")
