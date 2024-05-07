import tkinter as tk
import math
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = tk.Entry(master, width=50, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('^', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
            ('0', 5, 0), ('C', 5, 1), ('=', 5, 2), ('/', 5, 3),
        ]

        for (text, row, column) in buttons:
            tk.Button(master, text=text, command=lambda t=text: self.click(t)).grid(row=row, column=column, padx=7, pady=7)

    def click(self, button):
        current = self.display.get()

        if button == '=':
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'C':
            self.display.delete(0, tk.END)

        elif button in ('sin', 'cos', 'tan'):
            try:
                num = float(current)
                if button == 'sin':
                    result = math.sin(math.radians(num))  # Convert degrees to radians
                elif button == 'cos':
                    result = math.cos(math.radians(num))  # Convert degrees to radians
                elif button == 'tan':
                    result = math.tan(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == '^':
            self.display.insert(tk.END, '**')

        else:
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
