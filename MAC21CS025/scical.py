from tkinter import *
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        
        self.entry = ttk.Entry(root, justify='right', width=50)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        ttk.Button(root, text='Clear', command=self.clear).grid(row=1, column=0)
        ttk.Button(root, text='Delete', command=self.delete).grid(row=1, column=1)
        ttk.Button(root, text='√', command=lambda: self.on_button_click('sqrt')).grid(row=1, column=2)
        ttk.Button(root, text='x²', command=lambda: self.on_button_click('squared')).grid(row=1, column=3)
        
        ttk.Button(root, text='7', command=lambda: self.on_button_click('7')).grid(row=2, column=0)
        ttk.Button(root, text='8', command=lambda: self.on_button_click('8')).grid(row=2, column=1)
        ttk.Button(root, text='9', command=lambda: self.on_button_click('9')).grid(row=2, column=2)
        ttk.Button(root, text='/', command=lambda: self.on_button_click('/')).grid(row=2, column=3)
        
        ttk.Button(root, text='4', command=lambda: self.on_button_click('4')).grid(row=3, column=0)
        ttk.Button(root, text='5', command=lambda: self.on_button_click('5')).grid(row=3, column=1)
        ttk.Button(root, text='6', command=lambda: self.on_button_click('6')).grid(row=3, column=2)
        ttk.Button(root, text='*', command=lambda: self.on_button_click('*')).grid(row=3, column=3)
        
        ttk.Button(root, text='1', command=lambda: self.on_button_click('1')).grid(row=4, column=0)
        ttk.Button(root, text='2', command=lambda: self.on_button_click('2')).grid(row=4, column=1)
        ttk.Button(root, text='3', command=lambda: self.on_button_click('3')).grid(row=4, column=2)
        ttk.Button(root, text='-', command=lambda: self.on_button_click('-')).grid(row=4, column=3)
        
        ttk.Button(root, text='0', command=lambda: self.on_button_click('0')).grid(row=5, column=0)
        ttk.Button(root, text='.', command=lambda: self.on_button_click('.')).grid(row=5, column=1)
        ttk.Button(root, text='=', command=lambda: self.on_button_click('=')).grid(row=5, column=2)
        ttk.Button(root, text='+', command=lambda: self.on_button_click('+')).grid(row=5, column=3)
        
        ttk.Button(root, text='x³', command=lambda: self.on_button_click('cubed')).grid(row=6, column=0)
        ttk.Button(root, text='sin', command=lambda: self.on_button_click('sin')).grid(row=6, column=1)
        ttk.Button(root, text='cos', command=lambda: self.on_button_click('cos')).grid(row=6, column=2)
        ttk.Button(root, text='tan', command=lambda: self.on_button_click('tan')).grid(row=6, column=3)
        
    def on_button_click(self, char):
        current_text = self.entry.get()
        if char == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, END)
                self.entry.insert(END, str(result))
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
        elif char in ['sqrt', 'squared', 'cubed', 'sin', 'cos', 'tan']:
            try:
                if char == 'sqrt':
                    result = math.sqrt(eval(current_text))
                elif char == 'squared':
                    result = eval(current_text) ** 2
                elif char == 'cubed':
                    result = eval(current_text) ** 3
                elif char == 'sin':
                    result = math.sin(math.radians(eval(current_text)))
                elif char == 'cos':
                    result = math.cos(math.radians(eval(current_text)))
                elif char == 'tan':
                    result = math.tan(math.radians(eval(current_text)))
                    
                self.entry.delete(0, END)
                self.entry.insert(END, str(result))
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, "Error")
        else:
            self.entry.insert(END, char)
            
    def clear(self):
        self.entry.delete(0, END)
        
    def delete(self):
        current_text = self.entry.get()
        self.entry.delete(len(current_text) - 1)

root = Tk()
app = ScientificCalculator(root)
root.mainloop()
