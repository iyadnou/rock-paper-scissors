import random

choices = ["Rock", "Paper", "Scissors"]

player = input("Choose Rock, Paper, or Scissors: ").capitalize()

if player not in choices:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
else:
    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a draw!")
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")