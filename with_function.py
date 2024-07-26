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

#without using functions

list = [rock, paper, scissors]
user_input = int(input("what Would you Like to select?\n0 for rock\n1 for paper\n2 for scissors: "))
if user_input == 0 or user_input == 1 or user_input == 2:
    print(list[user_input])
    computer = random.randint(0,2)
    print(f"Computer selected: {computer}")
    print(list[computer])
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
    
else:
    print("invalid input")
