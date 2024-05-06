import tkinter as tk
import math

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "sin":
        entry.insert(tk.END, "math.sin(math.radians(")
    elif text == "cos":
        entry.insert(tk.END, "math.cos(math.radians(")
    elif text == "tan":
        entry.insert(tk.END, "math.tan(math.radians(")
    elif text == "log":
        entry.insert(tk.END, "math.log10(")
    elif text == "ln":
        entry.insert(tk.END, "math.log(")
    elif text == "sqrt":
        entry.insert(tk.END, "math.sqrt(")
    elif text == "exp":
        entry.insert(tk.END, "math.exp(")
    elif text == "%":
        entry.insert(tk.END, "/100*")
    elif text == "!":
        entry.insert(tk.END, "math.factorial(")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

buttons = [
    ("sin", "lightblue"), ("cos", "lightblue"), ("tan", "lightblue"), ("log", "lightblue"),
    ("ln", "lightblue"), ("sqrt", "lightblue"), ("exp", "lightblue"), ("%", "lightblue"),
    ("!", "lightblue"), ("(", "lightblue"), (")", "lightblue"), ("C", "lightcoral"),
    ("7", "lightgrey"), ("8", "lightgrey"), ("9", "lightgrey"), ("/", "lightcoral"),
    ("4", "lightgrey"), ("5", "lightgrey"), ("6", "lightgrey"), ("*", "lightcoral"),
    ("1", "lightgrey"), ("2", "lightgrey"), ("3", "lightgrey"), ("-", "lightcoral"),
    (".", "lightgrey"), ("0", "lightgrey"), ("=", "lightgreen"), ("+", "lightcoral")
]

row = 1
col = 0
for button_text, color in buttons:
    tk.Button(root, text=button_text, font=("Helvetica", 12), padx=20, pady=10, bg=color).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col >= 4 :
        col = 0
        row += 1

for widget in root.winfo_children():
    widget.bind("<Button-1>", button_click)

root.mainloop()
