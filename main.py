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
loop = True
list = ["rock", "paper", "scissors"]
user_input = input("I Would Like to select: ").lower()

def figures(input):
    if input == "rock":
        print(rock)
        return True
    elif input == "paper":
        print(paper)
        return True
    elif input == "scissors":
        print(scissors)
        return True
    else:
        print("Invalid input")
        return False

loop = figures(user_input)  

while loop:
    computer = random.choice(list)
    print("Computer selected: "+ computer)
    figures(computer)
    if user_input == computer:
        print("Draw")
    elif user_input == "paper" and computer == "rock":
        print("You Won")
    elif user_input == "scissors" and computer == "paper":
        print("You Won")
    elif user_input =="rock" and computer == "scissors":
        print("You Won")
    else:
        print("Computer Won")
    loop = False
