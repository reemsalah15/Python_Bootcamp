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

images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
  print(images[user_choice])
  computer_choice = random.randint(0, 2)
  print(f"Computer choice:\n{images[computer_choice]}")
  if user_choice == computer_choice:
      print("It's draw.")
  elif user_choice == 0 and computer_choice == 2:
      print("You win.")
  elif user_choice == 2 and computer_choice == 1:
      print("You win.")
  elif user_choice == 1 and computer_choice == 0:
      print("You win.")
  else:
      print("You lose")
  