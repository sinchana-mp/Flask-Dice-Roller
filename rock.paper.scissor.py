import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)

    user = input("\nChoose rock, paper, or scissors (or type exit): ").lower()

    if user == "exit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print(" You win!")
    else:
        print(" Computer wins!")