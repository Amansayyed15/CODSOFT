import tkinter as tk
import string
import random

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    characters = string.ascii_letters
    if complexity == "Medium":
        characters += string.digits
    elif complexity == "High":
        characters += string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#f0f4f7")

title_label = tk.Label(root, text="Password Generator", font=("Arial", 18), bg="#f0f4f7")
title_label.pack(pady=20)

length_frame = tk.Frame(root, bg="#e3e6ea", bd=2, relief="sunken")
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 14), bg="#e3e6ea")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(length_frame, font=("Arial", 14), bd=2)
length_entry.grid(row=0, column=1, padx=10, pady=10)

complexity_var = tk.StringVar(value="Low")
complexity_frame = tk.Frame(root, bg="#e3e6ea", bd=2, relief="sunken")
complexity_frame.pack(pady=10)
complexity_label = tk.Label(complexity_frame, text="Password Complexity:", font=("Arial", 14), bg="#e3e6ea")
complexity_label.grid(row=0, column=0, padx=10, pady=10)
complexity_menu = tk.OptionMenu(complexity_frame, complexity_var, "Low", "Medium", "High")
complexity_menu.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), bg="#6c8ebf", fg="white", command=generate_password)
generate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f4f7")
result_label.pack(pady=10)

root.mainloop()
