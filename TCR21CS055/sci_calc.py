import tkinter as tk
from math import *

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry field for the expressions
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Function to update the entry with the button's value
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the expression
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to add advanced mathematical operations
def math_function(function):
    try:
        current = entry.get()
        if function == 'factorial':
            result = str(factorial(int(current)))
        elif function in ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt']:
            result = str(eval(f'{function}({current})'))
        else:
            result = str(eval(f'{current}{function}'))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define buttons
button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=18, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_click("/"))
button_equal = tk.Button(root, text="=", padx=48, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=39, pady=20, command=button_clear)

# Advanced function buttons
button_sin = tk.Button(root, text="sin", padx=20, pady=20, command=lambda: math_function('sin'))
button_cos = tk.Button(root, text="cos", padx=20, pady=20, command=lambda: math_function('cos'))
button_tan = tk.Button(root, text="tan", padx=20, pady=20, command=lambda: math_function('tan'))
button_log = tk.Button(root, text="log", padx=20, pady=20, command=lambda: math_function('log'))
button_exp = tk.Button(root, text="exp", padx=20, pady=20, command=lambda: math_function('exp'))

# Additional advanced function buttons
button_sqrt = tk.Button(root, text="√", padx=20, pady=20, command=lambda: math_function('sqrt'))
button_cbrt = tk.Button(root, text="³√", padx=20, pady=20, command=lambda: math_function('**(1/3)'))
button_ln = tk.Button(root, text="ln", padx=20, pady=20, command=lambda: math_function('log'))
button_exp2 = tk.Button(root, text="2^x", padx=20, pady=20, command=lambda: math_function('**2'))
button_exp3 = tk.Button(root, text="3^x", padx=20, pady=20, command=lambda: math_function('**3'))
button_abs = tk.Button(root, text="abs", padx=20, pady=20, command=lambda: math_function('abs'))
button_floor = tk.Button(root, text="floor", padx=20, pady=20, command=lambda: math_function('floor'))
button_ceil = tk.Button(root, text="ceil", padx=20, pady=20, command=lambda: math_function('ceil'))
button_degrees = tk.Button(root, text="degrees", padx=20, pady=20, command=lambda: math_function('degrees'))
button_radians = tk.Button(root, text="radians", padx=20, pady=20, command=lambda: math_function('radians'))

# Place buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)
button_subtract.grid(row=7, column=0)
button_multiply.grid(row=7, column=1)
button_divide.grid(row=7, column=2)

# Advanced function buttons placement
button_sin.grid(row=1, column=0)
button_cos.grid(row=1, column=1)
button_tan.grid(row=1, column=2)
button_log.grid(row=1, column=3)
button_exp.grid(row=1, column=4)

# Additional advanced function buttons placement
button_sqrt.grid(row=2, column=3)
button_cbrt.grid(row=2, column=4)
button_ln.grid(row=3, column=3)
button_exp2.grid(row=3, column=4)
button_exp3.grid(row=4, column=3)
button_abs.grid(row=4, column=4)
button_floor.grid(row=5, column=3)
button_ceil.grid(row=5, column=4)
button_degrees.grid(row=6, column=3)
button_radians.grid(row=6, column=4)

# Run the application
root.mainloop()
