import random

choice = ['Rock', 'Paper', 'Scissor']

computer_choice = random.choice(choice)
user_choise = input("Do you want Rock, Paper, or Scissor?\n")

print("Computer's choice was: " + computer_choice + "!")

if computer_choice == user_choise:
    print("\nTie")
elif computer_choice == "Paper" and user_choise == "Scissor":
    print("\nYOU WON!!")
elif computer_choice == "Rock" and user_choise == "Paper":
    print("\nYOU WON!!")
elif computer_choice == "Scissor" and user_choise == "Rock":
    print("\nYOU WON!!")
else:
    print("\nYOU LOSE, Computer wins this round")