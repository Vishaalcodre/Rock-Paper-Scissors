
"""
Created on Fri Sep  2 10:06:47 2022

"""

import random

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

computer_choice = random.randint(0, 2)
print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user_choice > 2 or user_choice < 0:
    print("Invalid Input")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
elif computer_choice == user_choice:
    print("It's a Tie")
elif computer_choice > user_choice:
    print("You Lose")
elif user_choice > computer_choice:
    print("You Win")
