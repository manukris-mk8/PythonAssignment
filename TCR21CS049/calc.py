import tkinter as tk
import math

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"sin({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"cos({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tan():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"tan({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def asin():
    try:
        result = math.degrees(math.asin(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"asin({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def acos():
    try:
        result = math.degrees(math.acos(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"acos({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def atan():
    try:
        result = math.degrees(math.atan(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"atan({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def ln():
    try:
        result = math.log(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"ln({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
def log():
    try:
        result = math.log10(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"log({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def log_base():
    try:
        base = float(input("Enter the base: "))
        result = math.log(float(entry.get()), base)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"log{base}({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def exp():
    try:
        result = math.exp(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"exp({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"√{entry.get()} = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square():
    try:
        result = math.pow(float(entry.get()), 2)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"({entry.get()})^2 = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
def cube():
    try:
        result = math.pow(float(entry.get()), 3)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"({entry.get()})^3 = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
def power():
    try:
        power = float(input("Enter the power: "))
        result = math.pow(float(entry.get()), power)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"({entry.get()})^{power} = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
def n_root():
    try:
        n = float(input("Enter the root: "))
        result = math.pow(float(entry.get()), 1/n)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"ⁿ√{entry.get()} = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def factorial():
    try:
        result = math.factorial(int(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{entry.get()}! = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{entry.get()}% = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def deg_to_rad():
    try:
        result = math.radians(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"deg_to_rad({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
def rad_to_deg():
    try:
        result = math.degrees(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"rad_to_deg({entry.get()}) = {result}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        

        
def pi():
    entry.insert(tk.END, str(math.pi))

def e():
    entry.insert(tk.END, str(math.e))



root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6)


trig_funcs = [("sin", sin), ("cos", cos), ("tan", tan),
              ("asin", asin), ("acos", acos), ("atan", atan)]
for i, (name, func) in enumerate(trig_funcs):
    btn = tk.Button(root, text=name, padx=20, pady=10, command=func)
    btn.grid(row=1, column=i)


log_funcs = [("ln", ln), ("log", log), ("log𝑏", log_base)]
for i, (name, func) in enumerate(log_funcs):
    btn = tk.Button(root, text=name, padx=20, pady=10, command=func)
    btn.grid(row=2, column=i)


exp_funcs = [("exp", exp), ("e^x", lambda: entry.insert(tk.END, "e**")),
             ("√x", sqrt), ("x^2", square), ("x^3", cube),
             ("x^y", power), ("ⁿ√x", n_root)]
for i, (name, func) in enumerate(exp_funcs):
    btn = tk.Button(root, text=name, padx=20, pady=10, command=func)
    btn.grid(row=3, column=i)


btn_factorial = tk.Button(root, text="n!", padx=20, pady=10, command=factorial)
btn_factorial.grid(row=4, column=0)


btn_percentage = tk.Button(root, text="%", padx=20, pady=10, command=percentage)
btn_percentage.grid(row=4, column=1)


angle_funcs = [("Deg to Rad", deg_to_rad), ("Rad to Deg", rad_to_deg)]
for i, (name, func) in enumerate(angle_funcs):
    btn = tk.Button(root, text=name, padx=20, pady=10, command=func)
    btn.grid(row=4, column=i+2)


btn_pi = tk.Button(root, text="π", padx=20, pady=10, command=pi)
btn_pi.grid(row=5, column=0)
btn_e = tk.Button(root, text="𝑒", padx=20, pady=10, command=e)
btn_e.grid(row=5, column=1)




button_numbers = [
    ("7", 6, 0), ("8", 6, 1), ("9", 6, 2),
    ("4", 7, 0), ("5", 7, 1), ("6", 7, 2),
    ("1", 8, 0), ("2", 8, 1), ("3", 8, 2),
    ("0", 9, 1), (".", 9, 2)
]

for (text, row, column) in button_numbers:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=column)


button_equal = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
button_equal.grid(row=9, column=3, columnspan=2)


button_clear = tk.Button(root, text="C", padx=20, pady=10, command=clear)
button_clear.grid(row=6, column=3, columnspan=2)

root.mainloop()
