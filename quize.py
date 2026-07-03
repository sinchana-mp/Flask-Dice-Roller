score = 0

print("===== Python Quiz =====")

answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. Which language are you learning? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour Score:", score, "/3")