################################## Day 46: 69 Days of Python #####################################


# Task: create a calculator using tkinter
import tkinter as tk
from functools import partial

def call_result(labelResult, number1, number2):
    try:
        a = int(number1.get())
        b = int(number2.get())
        result = a + b
        labelResult.config(text=f"Result: {result}")
    except ValueError:
        labelResult.config(text="Invalid input!")

def call_sub(labelResult, number1, number2):
    try:
        a = int(number1.get())
        b = int(number2.get())
        result = a - b
        labelResult.config(text=f"Result: {result}")
    except ValueError:
        labelResult.config(text="Invalid input!")

def call_mul(labelResult, number1, number2):
    try:
        a = int(number1.get())
        b = int(number2.get())
        result = a * b
        labelResult.config(text=f"Result: {result}")
    except ValueError:
        labelResult.config(text="Invalid input!")

def call_div(labelResult, number1, number2):
    try:
        a = int(number1.get())
        b = int(number2.get())
        if b != 0:
            result = a / b
            labelResult.config(text=f"Result: {result:.2f}")
        else:
            labelResult.config(text="Error: Division by zero!")
    except ValueError:
        labelResult.config(text="Invalid input!")

root = tk.Tk()
root.geometry("400x200")
root.title("Simple Calculator")

number1 = tk.StringVar()
number2 = tk.StringVar()

# Labels and entry fields
tk.Label(root, text="Enter Number 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root, textvariable=number1)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Number 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root, textvariable=number2)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Result label
labelResult = tk.Label(root, text="Result: ", font=("Arial", 12))
labelResult.grid(row=3, column=0, columnspan=2, pady=10)

# Buttons for operations
tk.Button(root, text="+", command=partial(call_result, labelResult, number1, number2)).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="-", command=partial(call_sub, labelResult, number1, number2)).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="*", command=partial(call_mul, labelResult, number1, number2)).grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="/", command=partial(call_div, labelResult, number1, number2)).grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
