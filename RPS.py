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
playerinput = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors "))
computerinput = random.randint(0, 2)

if playerinput == 0:
    print(rock)
elif playerinput == 1:
    print(paper)
elif playerinput == 2:
    print(scissors)
else:
    print("Try again")





if computerinput == 0:
    print(rock)
elif computerinput == 1:
    print(paper)
elif computerinput == 2:
    print(scissors)
else:
    print("Try again!")



if playerinput == 0 and computerinput == 1:
    print("You lose")
elif playerinput == 0 and computerinput == 2:
    print("You win")
elif playerinput == 1 and computerinput == 0:
    print("You win")
elif playerinput == 1 and computerinput == 2:
    print("You lose")
elif playerinput == 2 and computerinput == 0:
    print("You lose")
elif playerinput == 2 and computerinput == 1:
    print("You win")
else:
    print("Draw")
