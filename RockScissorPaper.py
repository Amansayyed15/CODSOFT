import tkinter as tk
import random

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=f"User: {user_choice} | Computer: {computer_choice}\n{result}")
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")
root.config(bg="#f0f4f7")

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 18), bg="#f0f4f7")
title_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#e3e6ea", bd=2, relief="sunken")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), bg="#6c8ebf", fg="white", command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), bg="#6c8ebf", fg="white", command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), bg="#6c8ebf", fg="white", command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f4f7")
result_label.pack(pady=20)

score_label = tk.Label(root, text="User Score: 0 | Computer Score: 0", font=("Arial", 16), bg="#f0f4f7")
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), bg="#ff6f61", fg="white", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
