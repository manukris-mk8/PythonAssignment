import tkinter as tk
import numpy as np
import math

def calculate():
    try:
        expression = entry_field.get()
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error: Invalid Input")

def append_text(text):
    if text == "^":
        entry_field.insert(tk.END, "**")  
    else:
        entry_field.insert(tk.END, text)
def clear():
    entry_field.delete(0, tk.END)

def add_matrix():
    perform_matrix_operation(np.add)

def sub_matrix():
    perform_matrix_operation(np.subtract)

def mul_matrix():
    try:
        num1 = np.matrix(eval(num1_entry.get()))
        num2 = np.matrix(eval(num2_entry.get()))
        if num1.shape[1] != num2.shape[0]:
            raise Exception("Invalid input: Matrices are not compatible for multiplication")
        result = np.matmul(num1, num2)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except Exception as e:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error: " + str(e))

def div_matrix():
    perform_matrix_operation(np.divide)

def perform_matrix_operation(operation):
    try:
        num1 = np.matrix(eval(num1_entry.get()))
        num2 = np.matrix(eval(num2_entry.get()))
        result = operation(num1, num2)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except Exception as e:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error: Invalid Input")

def sin_func():
    try:
        num = eval(entry_field.get())
        result = math.sin(math.radians(num))
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error: Invalid Input")

def cos_func():
    try:
        num = eval(entry_field.get())
        result = math.cos(math.radians(num))
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error: Invalid Input")

def tan_func():
    try:
        num = eval(entry_field.get())
        result = math.tan(math.radians(num))
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error: Invalid Input")

def log_func():
    try:
        num = eval(entry_field.get())
        result = math.log(num)
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error: Invalid Input")


root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x480")

background_color = "#dedede"
button_color = "#b0c4de"
button_color2 = "#add8e6"
button_color3 = "#87ceeb"

root.configure(bg=background_color)

entry_field = tk.Entry(root, font=('sans-serif', 14), width=25, bd=5, relief="sunken")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

num1_label = tk.Label(root, text="Enter Matrix 1:", font=('sans-serif', 12), bg=background_color)
num1_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
num1_entry = tk.Entry(root, font=('sans-serif', 12))
num1_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

num2_label = tk.Label(root, text="Enter Matrix 2:", font=('sans-serif', 12), bg=background_color)
num2_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
num2_entry = tk.Entry(root, font=('sans-serif', 12))
num2_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

result_label = tk.Label(root, text="Result:", font=('sans-serif', 12), bg=background_color)
result_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
result_entry = tk.Entry(root, font=('sans-serif', 12), bd=5, relief="sunken")
result_entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

# Matrix operation buttons
add_button = tk.Button(root, text="Add", command=add_matrix, font=('sans-serif', 12), bg=button_color)
add_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

sub_button = tk.Button(root, text="Subtract", command=sub_matrix, font=('sans-serif', 12), bg=button_color2)
sub_button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

mul_button = tk.Button(root, text="Multiply", command=mul_matrix, font=('sans-serif', 12), bg=button_color)
mul_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

div_button = tk.Button(root, text="Divide", command=div_matrix, font=('sans-serif', 12), bg=button_color2)
div_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

#  function buttons
sin_button = tk.Button(root, text="sin", command=sin_func, font=('sans-serif', 12), bg=button_color3)
sin_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

cos_button = tk.Button(root, text="cos", command=cos_func, font=('sans-serif', 12), bg=button_color2)
cos_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

tan_button = tk.Button(root, text="tan", command=tan_func, font=('sans-serif', 12), bg=button_color3)
tan_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

log_button = tk.Button(root, text="log", command=log_func, font=('sans-serif', 12), bg=button_color2)
log_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

# Basic  buttons
buttons = [
    ('7', 7, 0), ('8', 7, 1), ('9', 7, 2), ('/', 7, 3),
    ('4', 8, 0), ('5', 8, 1), ('6', 8, 2), ('*', 8, 3),
    ('1', 9, 0), ('2', 9, 1), ('3', 9, 2), ('-', 9, 3),
    ('0', 10, 0), ('.', 10, 1), ('=', 10, 2), ('+', 10, 3),
    ('(', 11, 0), (')', 11, 1), ('C', 11, 2), ('^', 11, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=('sans-serif', 14), width=5, command=calculate, bg=button_color3)
    elif text == 'C':
        button = tk.Button(root, text=text, font=('sans-serif', 14), width=5, command=clear, bg=button_color3)
    elif text == '^':  
        button = tk.Button(root, text=text, font=('sans-serif', 14), width=5, command=lambda t=text: append_text(t), bg=button_color)    
    else:
        button = tk.Button(root, text=text, font=('sans-serif', 14), width=5, command=lambda t=text: append_text(t), bg=button_color)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


for i in range(12):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
