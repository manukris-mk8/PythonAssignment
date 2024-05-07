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
    ("sin", "white"), ("cos", "white"), ("tan", "white"), ("log", "white"),
    ("ln", "white"), ("sqrt", "white"), ("exp", "white"), ("%", "white"),
    ("!", "white"), ("(", "white"), (")", "white"), ("C", "lightcoral"),
    ("7", "grey"), ("8", "grey"), ("9", "grey"), ("/", "lightcoral"),
    ("4", "grey"), ("5", "grey"), ("6", "grey"), ("*", "lightcoral"),
    ("1", "grey"), ("2", "grey"), ("3", "grey"), ("-", "lightcoral"),
    (".", "grey"), ("0", "grey"), ("=", "green"), ("+", "lightcoral")
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
