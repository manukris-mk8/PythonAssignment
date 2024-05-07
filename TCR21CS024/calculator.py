import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.entry = tk.Entry(master, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5)


        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('√', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('π', 5, 3), ('^', 5, 4)
        ]


        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=20, pady=10, command=lambda: self.button_click(text))
        button.grid(row=row, column=col)

    def button_click(self, value):
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif value == 'π':
            self.entry.insert(tk.END, math.pi)
        elif value == '√':
            self.entry.insert(tk.END, 'sqrt(')
        elif value == '^':
            self.entry.insert(tk.END, '**')
        elif value == 'sin':
            self.entry.insert(tk.END, 'math.sin(')
        elif value == 'cos':
            self.entry.insert(tk.END, 'math.cos(')
        elif value == 'tan':
            self.entry.insert(tk.END, 'math.tan(')
        else:
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
