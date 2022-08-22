rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

selection = input("What do you choose? Type 0 for rock, 1 for Paper, or 2 for Scissors. ")

game_images = [rock, paper, scissors]

if selection == "0":
  print(game_images[0])
elif selection == "1":
  print(paper)
elif selection == "2":
  print(scissors)
else:
  print("Number out of range. You loose.")


computer_chose = random.randint(0, 2)

print(f"computer chose {computer_chose}:")

if computer_chose == 0:
  print(rock)
elif computer_chose == 1:
  print(paper)
elif computer_chose == 2:
  print(scissors)


if selection == "0" and computer_chose == 0:
  print("Tie game.")
if selection == "1" and computer_chose == 0:
  print("You win.")
if selection == "2" and computer_chose == 0:
  print("You loose.")
if selection == "0" and computer_chose == 1:
  print("You loose.")
if selection == "1" and computer_chose == 1:
  print("Tie game.")
if selection == "2" and computer_chose == 1:
  print("You win.")
if selection == "0" and computer_chose == 2:
  print("You win.")
if selection == "1" and computer_chose == 2:
  print("You loose.")
if selection == "2" and computer_chose == 2:
  print("Tie game.")






