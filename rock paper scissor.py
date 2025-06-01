
import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()


if user_choice not in item_list:
    print("Invalid input. Please enter Rock, Paper, or Scissor.")
else:
    computer_choice = random.choice(item_list)
    print(f"User choice: {user_choice}, Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "Paper":
        if computer_choice == "Scissor":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "Scissor":
        if computer_choice == "Rock":
            print("Computer wins!")
        else:
            print("You win!")
