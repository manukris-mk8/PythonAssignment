import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.equation = ""
        
        self.entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16), relief=tk.RIDGE)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=10, sticky='nsew')
        
        self.create_buttons()
        self.bind_keys()
        
        self.root.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.root.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('sin', 4, 4),
            ('cos', 5, 0), ('tan', 5, 1), ('√', 5, 2), ('^', 5, 3), ('π', 5, 4),
            ('asin', 6, 0), ('acos', 6, 1), ('atan', 6, 2), ('log', 6, 3), ('exp', 6, 4),
            ('%', 7, 0)
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: self.on_button_click(t), relief=tk.RIDGE)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    
    def bind_keys(self):
        self.root.bind("<Key>", self.key_pressed)
        
    def key_pressed(self, event):
        key = event.char
        allowed_chars = '1234567890./*-+()=π^'
        if key in allowed_chars:
            self.on_button_click(key)
    
    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.equation)
                self.equation = str(result)
            except:
                self.equation = "Error"
        elif value == 'C':
            self.equation = ""
        elif value == '√':
            self.equation += 'math.sqrt('
        elif value in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan'):
            self.equation += f'math.{value}('
        elif value == 'π':
            self.equation += 'math.pi'
        elif value == '^':
            self.equation += '**'
        elif value == 'log':
            self.equation += 'math.log('
        elif value == 'exp':
            self.equation += 'math.exp('
        elif value == '%':
            self.equation += '/100'
        else:
            self.equation += value
        
        self.update_entry()
    
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.equation)

root = tk.Tk()
root.geometry("400x500")
root.config(bg="#f0f0f0")
calc = ScientificCalculator(root)
root.mainloop()
