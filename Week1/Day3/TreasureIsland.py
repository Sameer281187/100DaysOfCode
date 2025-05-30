print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
direction = input('''You are at cross road. Where do you want to go.
******************Type 'left' or 'right'******************
''')

if direction.lower() != "left":
    print("You have fallen into a hole. Game over")
    exit("Game over")

swim = input('''You've come to a lake. There is an island in the middle of the lake.
******************Type 'wait' to wait for a boat. Type 'swim' to swim across.******************
''')

if swim.lower() != "wait":
    print("You are attacked by trout. Game over")
    exit("Game over")

door = input('''You've arrived at the island unharmed. There is a house with 3 doors.
    One red, One yellow and one blue. Which color do you choose?
    ''')

if door.lower() == "yellow":
    print("You win.")
elif door.lower() == "red":
    print("Burned by Fire.\n Game over.")
elif door.lower() == "blue":
    print("Eaten by beasts. \n Game Over.")
else:
    print("Game Over")