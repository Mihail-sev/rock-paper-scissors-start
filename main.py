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
from random import *
choose = [rock, paper, scissors]
human = int(input("Make your choise: 1 - rock, 2 - paper, 3 - scissors\n"))
if human < 0 or human > 3:
  print ("Your make incorrect choise, you lose!")
else:
  print ("Your choise\n" + choose[human-1] + "\nComputer choise")
computer = randint(1,3)
print (choose [computer-1])
if human == computer:
  print ("Is draw!")
elif human == 1 and computer == 2:
  print ("Computer win!")
elif human == 2 and computer == 1:
  print ("human win!")
elif human == 2 and computer == 3:
  print ("Computer win!")
elif human == 3 and computer == 2:
  print ("human win!")
elif human == 3 and computer == 1:
  print ("Computer win!")
elif human == 1 and computer == 3:
  print ("human win!")