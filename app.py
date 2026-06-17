from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def roll_dice():
    number = random.randint(1, 6)

    return f"""
    <h1>🎲 Dice Roller</h1>
    <h2>You rolled: {number}</h2>
    <a href="/">Roll Again</a>
    """

if __name__ == "__main__":
    app.run(debug=True)