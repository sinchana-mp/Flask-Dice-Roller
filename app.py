from flask import Flask
import random

app = Flask(__name__)

secret_number = random.randint(1, 10)

@app.route("/<int:guess>")
def guess(guess):
    if guess < secret_number:
        return "Too Low! Try a bigger number."
    elif guess > secret_number:
        return "Too High! Try a smaller number."
    else:
        return "🎉 Correct! You guessed it!"

@app.route("/")
def home():
    return """
    <h1>Number Guessing Game</h1>
    <p>Guess a number from 1 to 10.</p>
    <p>Example: add /5 to the URL</p>
    """

if __name__ == "__main__":
    app.run(debug=True)