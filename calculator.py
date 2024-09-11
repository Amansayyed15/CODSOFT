import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else 'Error'
    else:
        result = 'Invalid Operation'
    
    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator-Codsoft")
root.geometry("300x400")
root.config(bg="#f0f4f7")

frame = tk.Frame(root, bg="#e3e6ea", bd=2, relief="sunken")
frame.pack(pady=20, padx=20)

entry_num1 = tk.Entry(frame, font=("Arial", 16), bd=2)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(frame, font=("Arial", 16), bd=2)
entry_num2.grid(row=1, column=0, padx=10, pady=10)

operation_var = tk.StringVar()
operation_menu = tk.OptionMenu(frame, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=0, padx=10, pady=10)

calculate_button = tk.Button(frame, text="Calculate", font=("Arial", 14), bg="#6c8ebf", fg="white", command=calculate)
calculate_button.grid(row=3, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16), bg="#f0f4f7")
result_label.pack(pady=20)

root.mainloop()

