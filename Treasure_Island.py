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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


left_right = input("You're at a crossroads, where do you want to go? Type 'left' or 'right'. ").lower()

if left_right == "right":
  print("Oh no, you've fallen into a ditch... Game over.")
else:
  swim = input("You've made it to a beautiful tropical island. Do you want to swim or wait on the island? Type 'swim' or 'wait'. ").lower()
  if swim == "swim":
        print("Oh no, you've been attacked by a killer trout! Game over!")
  else:
    door = input("You've made it to a room filled with three powerful doors. Choose which door you want to go through. Type 'red', 'blue', or 'yellow'. ").lower()
    if door == "red":
      print("Oh no!! You've been burned by fire! Game over.")
    elif door == "blue":
      print("Oh no!! You've been eaten by Beasts! Game over.")
    else:
      print("Congradulations!!! You have won Treasure Island!")
              
      




