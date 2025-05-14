import tkinter as tk
import random

window = tk.Tk()
window.title("Rock, Paper, Scissors Game!")
window.geometry("400x400")

def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = ""

    if user_choice == computer_choice:
        result = f"Both chose {user_choice}. It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = f"You chose {user_choice}, computer chose {computer_choice}. You win!"
    else:
        result = f"You chose {user_choice}, computer chose {computer_choice}. Computer wins!"

    result_label.config(text=result)


heading = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 16))
heading.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=300, justify="center")
result_label.pack(pady=30)

window.mainloop()