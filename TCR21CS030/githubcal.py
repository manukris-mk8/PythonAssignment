import tkinter as tk
import math

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            result_label.config(text="Cannot divide by zero!")
        else:
            result = float(entry1.get()) / num2
            result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def square():
    try:
        result = float(entry1.get()) ** 2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter a valid number")

def cube():
    try:
        result = float(entry1.get()) ** 3
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter a valid number")

def cos():
    try:
        result = math.cos(math.radians(float(entry1.get())))
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter a valid number")

def sin():
    try:
        result = math.sin(math.radians(float(entry1.get())))
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter a valid number")

def square_root():
    try:
        result = math.sqrt(float(entry1.get()))
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter a valid number")
    except ValueError:
        result_label.config(text="Cannot compute square root of a negative number")

root = tk.Tk()
root.title("Scientific Calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text="+", command=add)
add_button.pack()

subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.pack()

divide_button = tk.Button(root, text="/", command=divide)
divide_button.pack()

square_button = tk.Button(root, text="Square", command=square)
square_button.pack()

cube_button = tk.Button(root, text="Cube", command=cube)
cube_button.pack()

cos_button = tk.Button(root, text="Cos", command=cos)
cos_button.pack()

sin_button = tk.Button(root, text="Sin", command=sin)
sin_button.pack()

sqrt_button = tk.Button(root, text="Square Root", command=square_root)
sqrt_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()