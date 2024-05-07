import tkinter as tk
from tkinter import ttk
import math

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def button_click(value):
    entry.insert(tk.END, value)

def square_root():
    try:
        result = math.sqrt(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def trigonometric_function(func):
    try:
        result = eval(f"math.{func}({eval(entry.get())})")
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def scientific_calculator():
    root = tk.Tk()
    root.title("Scientific Calculator")

    global entry
    entry = tk.Entry(root, width=40, borderwidth=5, font=('Helvetica', 14))
    entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
        ("C", 1, 4), ("√", 1, 5), ("sin", 2, 4), ("cos", 2, 5),
        ("tan", 3, 4), ("log", 3, 5), ("pi", 4, 4), ("(", 4, 5),
        (")", 5, 4), ("^", 5, 5)
    ]

    for (text, row, col) in buttons:
        if text == "=":
            button = ttk.Button(root, text=text, padding=10, command=evaluate_expression)
        elif text == "C":
            button = ttk.Button(root, text=text, padding=10, command=clear)
        elif text == "√":
            button = ttk.Button(root, text=text, padding=10, command=square_root)
        elif text in ["sin", "cos", "tan"]:
            button = ttk.Button(root, text=text, padding=5, command=lambda func=text: trigonometric_function(func))
        elif text == "log":
            button = ttk.Button(root, text=text, padding=5, command=lambda: button_click("math.log10("))
        elif text == "pi":
            button = ttk.Button(root, text=text, padding=10, command=lambda: button_click("math.pi"))
        else:
            button = ttk.Button(root, text=text, padding=10, command=lambda value=text: button_click(value))
        
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    root.mainloop()

scientific_calculator()
