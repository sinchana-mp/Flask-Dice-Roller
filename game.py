import random

print(" Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 10...")

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f" Correct! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print(" Too low! Try again.")
    else:
        print(" Too high! Try again.")