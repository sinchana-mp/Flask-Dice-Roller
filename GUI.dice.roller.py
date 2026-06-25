from tkinter import *
import random

def roll_dice():
    result.config(text=f"🎲 {random.randint(1,6)}")

root = Tk()
root.title("Dice Roller")
root.geometry("300x200")

Label(root, text="Dice Roller", font=("Arial", 16)).pack(pady=10)

Button(root, text="Roll Dice", command=roll_dice).pack(pady=10)

result = Label(root, text="🎲", font=("Arial", 30))
result.pack(pady=10)

root.mainloop()