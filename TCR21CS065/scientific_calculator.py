import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Color Scheme
        bg_color = "#E3F2FD"  # Light blue
        btn_color = "#2196F3"  # Blue
        btn_hover_color = "#1976D2"  # Darker blue
        text_color = "black"  # Black text color

        # Styling
        master.geometry("400x600")
        master.configure(bg=bg_color)

        # Display
        self.display = tk.Entry(master, width=30, font=('Arial', 14), borderwidth=5, bg=bg_color, fg=text_color)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Button Grid
        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('^', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('=', 5, 3),
            ('Matrix 1', 6, 0), ('Matrix 2', 6, 1),
            ('Multiply', 6, 2), ('Add', 6, 3),
            ('Subtract', 7, 2), ('Clear', 7, 3)
        ]

        for (text, row, column) in buttons:
            btn = tk.Button(master, text=text, command=lambda t=text: self.click(t), padx=15, pady=15, font=('Arial', 12),
                            bg=btn_color, fg=text_color, activebackground=btn_hover_color, activeforeground=text_color)
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

        # Matrix Entry Fields
        self.matrix_entry1 = tk.Entry(master, width=10, font=('Arial', 12), borderwidth=2)
        self.matrix_entry1.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

        self.matrix_entry2 = tk.Entry(master, width=10, font=('Arial', 12), borderwidth=2)
        self.matrix_entry2.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")

        # History Display
        self.history_display = tk.Text(master, height=5, width=30, font=('Arial', 12), borderwidth=2, bg=bg_color, fg=text_color)
        self.history_display.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Configure Grid
        for i in range(8):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

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

        elif button == '^':
            self.display.insert(tk.END, '**')

        elif button == 'sin':
            try:
                num = float(current)
                result = math.sin(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'cos':
            try:
                num = float(current)
                result = math.cos(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'tan':
            try:
                num = float(current)
                result = math.tan(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'Multiply':
            matrix1_str = self.matrix_entry1.get()
            matrix2_str = self.matrix_entry2.get()

            try:
                matrix1 = eval(matrix1_str)
                matrix2 = eval(matrix2_str)

                result = self.perform_matrix_multiply(matrix1, matrix2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Matrix multiplication failed: " + str(e))

        elif button == 'Add':
            matrix1_str = self.matrix_entry1.get()
            matrix2_str = self.matrix_entry2.get()

            try:
                matrix1 = eval(matrix1_str)
                matrix2 = eval(matrix2_str)

                result = self.perform_matrix_addition(matrix1, matrix2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Matrix addition failed: " + str(e))

        elif button == 'Subtract':
            matrix1_str = self.matrix_entry1.get()
            matrix2_str = self.matrix_entry2.get()

            try:
                matrix1 = eval(matrix1_str)
                matrix2 = eval(matrix2_str)

                result = self.perform_matrix_subtraction(matrix1, matrix2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Matrix subtraction failed: " + str(e))

        else:
            self.display.insert(tk.END, button)

    def perform_matrix_multiply(self, matrix1, matrix2):
        result = [[sum(a*b for a,b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
        return result

    def perform_matrix_addition(self, matrix1, matrix2):
        result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result

    def perform_matrix_subtraction(self, matrix1, matrix2):
        result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
