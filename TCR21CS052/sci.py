from tkinter import *
from tkinter import messagebox
import math

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_input.set(operator)

def btnEquals():
    global operator
    try:
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator = str(sumup)
    except:
        text_input.set("Error")
        operator = ""

def scientificFunction(func):
    global operator
    try:
        if func == 'sqrt':
            result = math.sqrt(eval(operator))
        elif func == 'log':
            result = math.log(eval(operator))
        elif func == 'exp':
            result = math.exp(eval(operator))
        elif func == 'sin':
            result = math.sin(math.radians(eval(operator)))
        elif func == 'cos':
            result = math.cos(math.radians(eval(operator)))
        elif func == 'tan':
            result = math.tan(math.radians(eval(operator)))
        text_input.set(result)
        operator = str(result)
    except:
        text_input.set("Error")
        operator = ""

def create_matrix_A():
    global n, m, matrix_A_entries

    try:
        n = int(row1.get())
        m = int(col1.get())
        if n <= 0 or m <= 0:
            messagebox.showerror("Input Error", "Rows and columns must be greater than zero.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values for rows and columns.")
        return

    matrix_A_entries = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix_A_entries[i][j] = Entry(matrix_frame, width=8, bg="black", fg="green")
            matrix_A_entries[i][j].grid(row=30+i, column=j, padx=5, pady=5)
            matrix_A_entries[i][j].bind("<FocusIn>", lambda event, widget=matrix_A_entries[i][j]: on_entry_focus_in(event, widget))
            matrix_A_entries[i][j].bind("<FocusOut>", lambda event, widget=matrix_A_entries[i][j]: on_entry_focus_out(event, widget))
    matrix_A_entries[0][0].focus()

def create_matrix_B():
    global p, q, matrix_B_entries
    try:
        p = int(row2.get())
        q = int(col2.get())
        if p <= 0 or q <= 0:
            messagebox.showerror("Input Error", "Rows and columns must be greater than zero.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values for rows and columns.")
        return

    matrix_B_entries = [[0 for j in range(q)] for i in range(p)]
    for i in range(p):
        for j in range(q):
            matrix_B_entries[i][j] = Entry(matrix_frame, width=8, bg="black", fg="green")
            matrix_B_entries[i][j].grid(row=30+i, column=j+80, padx=5, pady=5)
            matrix_B_entries[i][j].bind("<FocusIn>", lambda event, widget=matrix_B_entries[i][j]: on_entry_focus_in(event, widget))
            matrix_B_entries[i][j].bind("<FocusOut>", lambda event, widget=matrix_B_entries[i][j]: on_entry_focus_out(event, widget))
    matrix_B_entries[0][0].focus()

def add_matrices():
    global n, m, p, q, matrix_A_entries, matrix_B_entries, matrix_result_entries
    try:
        if not (n and m and p and q):
            messagebox.showerror("Dimension Error", "Please create matrices A and B first.")
            return

        if n != p or m != q:
            messagebox.showerror("Dimension Error", "Matrices A and B must have the same dimensions to perform addition.")
        else:
            matrix_result_entries = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    result = int(matrix_A_entries[i][j].get()) + int(matrix_B_entries[i][j].get())
                    matrix_result_entries[i][j] = Label(matrix_frame, text=str(result), width=8, relief="solid", bg="black", fg="green")
                    matrix_result_entries[i][j].grid(row=40+i, column=j+5, padx=5, pady=5)

    except:
        messagebox.showerror("Initialization error","please create A and B")
    

def subtract_matrices():
    global n, m, p, q, matrix_A_entries, matrix_B_entries, matrix_result_entries
    try:
        if not (n and m and p and q):
            messagebox.showerror("Dimension Error", "Please create matrices A and B first.")
            return

        if n != p or m != q:
            messagebox.showerror("Dimension Error", "Matrices A and B must have the same dimensions to perform subtraction.")
        else:
            matrix_result_entries = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    result = int(matrix_A_entries[i][j].get()) - int(matrix_B_entries[i][j].get())
                    matrix_result_entries[i][j] = Label(matrix_frame, text=str(result), width=8, relief="solid", bg="black", fg="green")
                    matrix_result_entries[i][j].grid(row=40+i, column=j+5, padx=5, pady=5)
    except:
        messagebox.showerror("Initialization error","please create A and B")




    
def multiply_matrices():
    global n, m, p, q, matrix_A_entries, matrix_B_entries, matrix_result_entries
    try:
        if not (n and m and p and q):
            messagebox.showerror("Dimension Error", "Please create matrices A and B first.")
            return

        if m != p:
            messagebox.showerror("Dimension Error", "Number of columns in matrix A must equal number of rows in matrix B for multiplication.")
        else:
            matrix_result_entries = [[0 for j in range(q)] for i in range(n)]
            for i in range(n):
                for j in range(q):
                    result = 0
                    for k in range(m):
                        result += int(matrix_A_entries[i][k].get()) * int(matrix_B_entries[k][j].get())
                matrix_result_entries[i][j] = Label(matrix_frame, text=str(result), width=8, relief="solid", bg="black", fg="green")
                matrix_result_entries[i][j].grid(row=40+i, column=j+5, padx=5, pady=5)
    except:
        messagebox.showerror("Initialization error","please create A and B")




def reset_matrices():
    global matrix_A_entries, matrix_B_entries, matrix_result_entries, row1, row2, col1, col2
    for i in range(len(matrix_A_entries)):
        for j in range(len(matrix_A_entries[0])):
            matrix_A_entries[i][j].destroy()
    for i in range(len(matrix_B_entries)):
        for j in range(len(matrix_B_entries[0])):
            matrix_B_entries[i][j].destroy()
    
    for i in range(n):
            for j in range(q):
                matrix_result_entries[i][j] = Label(matrix_frame, text="", width=8, relief="solid", bg="black", fg="green")
                matrix_result_entries[i][j].grid(row=40+i, column=j+5, padx=5, pady=5)
    row1.delete(0, END)
    col1.delete(0, END)
    row2.delete(0, END)
    col2.delete(0, END)

def switch_frame():
    if cal.winfo_ismapped():
        cal.pack_forget()
        cal2.pack()
    else:
        cal2.pack_forget()
        cal.pack()

def on_entry_focus_in(event, widget):
    widget.configure(bg="light gray")

def on_entry_focus_out(event, widget):
    widget.configure(bg="black")

window = Tk()
window.title("Matrix Calculator")
window.configure(background="black")

cal = Frame()
cal.configure(bg="black")
n, m, p, q = 0, 0, 0, 0
row1, row2, col1, col2 = None, None, None, None

matrix_A_entries = []
matrix_B_entries = []
matrix_result_entries = []

label1 = Label(cal, text="Matrix A:", bg="black", fg="green", font=("Arial", 14))
label1.grid(row=0, column=0, padx=5, pady=5)
label2 = Label(cal, text="Matrix B:", bg="black", fg="green", font=("Arial", 14))
label2.grid(row=0, column=12, padx=5, pady=5)

row1label = Label(cal, text="Number of rows:", bg="black", fg="green", font=("Arial", 12))
row1label.grid(row=1, column=0, padx=5, pady=5)
row2label = Label(cal, text="Number of rows:", bg="black", fg="green", font=("Arial", 12))
row2label.grid(row=1, column=12, padx=5, pady=5)

row1 = Entry(cal, bg="black", fg="green", font=("Arial", 12))
row1.grid(row=2, column=0, padx=5, pady=5)
row1.bind("<FocusIn>", lambda event, widget=row1: on_entry_focus_in(event, widget))
row1.bind("<FocusOut>", lambda event, widget=row1: on_entry_focus_out(event, widget))

row2 = Entry(cal, bg="black", fg="green", font=("Arial", 12))
row2.grid(row=2, column=12, padx=5, pady=5)
row2.bind("<FocusIn>", lambda event, widget=row2: on_entry_focus_in(event, widget))
row2.bind("<FocusOut>", lambda event, widget=row2: on_entry_focus_out(event, widget))

col1label = Label(cal, text="Number of columns:", bg="black", fg="green", font=("Arial", 12))
col1label.grid(row=3, column=0, padx=5, pady=5)
col2label = Label(cal, text="Number of columns:", bg="black", fg="green", font=("Arial", 12))
col2label.grid(row=3, column=12, padx=5, pady=5)

col1 = Entry(cal, bg="black", fg="green", font=("Arial", 12))
col1.grid(row=4, column=0, padx=5, pady=5)
col1.bind("<FocusIn>", lambda event, widget=col1: on_entry_focus_in(event, widget))
col1.bind("<FocusOut>", lambda event, widget=col1: on_entry_focus_out(event, widget))
col2 = Entry(cal, bg="black", fg="green", font=("Arial", 12))
col2.grid(row=4, column=12, padx=5, pady=5)
col2.bind("<FocusIn>", lambda event, widget=col2: on_entry_focus_in(event, widget))
col2.bind("<FocusOut>", lambda event, widget=col2: on_entry_focus_out(event, widget))

createButton1 = Button(cal, text="Create A", padx=10, pady=5, bg="black", fg="green", font=("Arial", 12), command=create_matrix_A)
createButton1.grid(row=5, column=0, padx=5, pady=5)
createButton2 = Button(cal, text="Create B", padx=10, pady=5, bg="black", fg="green", font=("Arial", 12), command=create_matrix_B)
createButton2.grid(row=5, column=12, padx=5, pady=5)

addButton = Button(cal, text="ADD", padx=10, pady=5, bg="black", fg="green", font=("Arial", 12), command=add_matrices)
addButton.grid(row=6, column=0, padx=5, pady=5)
SubButton = Button(cal, text="SUBTRACT", padx=10, pady=5, bg="black", fg="green", font=("Arial", 12), command=subtract_matrices)
SubButton.grid(row=6, column=6, padx=5, pady=5)
MulButton = Button(cal, text="MULTIPLY", padx=10, pady=5, bg="black", fg="green", font=("Arial", 12), command=multiply_matrices)
MulButton.grid(row=6, column=12, padx=5, pady=5)

ResetButton = Button(cal, text="RESET", padx=10, pady=5, bg="black", fg="green", font=("Arial", 12), command=reset_matrices)
ResetButton.grid(row=7, column=6, padx=5, pady=5)

BackButton=Button(cal,text="BACK",padx=10,pady=5,bg="black",fg="green",font=("Arial",12),command=switch_frame)
BackButton.grid(row=0, column=6, padx=5, pady=5)

cal2 = Frame()
cal2.configure(background="black")
cal2.pack()

operator = ""
text_input = StringVar()
text_display = Entry(cal2, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="black", fg="green", justify="right",width=33)
text_display.grid(row=0, column=0, columnspan=6)
text_display.focus()

buttons_numeric = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
row_num = 1
col_num = 0
for i in range(len(buttons_numeric)):
    Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 20, 'bold'), text=buttons_numeric[i], command=lambda x=buttons_numeric[i]: btnClick(x)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

operations = ['+', '-', '*', '/']
row_op = 1
col_op = 3
for op in operations:
    Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 20, 'bold'), text=op, command=lambda x=op: btnClick(x)).grid(row=row_op, column=col_op)
    row_op += 1

Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 20, 'bold'), text="=", command=btnEquals).grid(row=4, column=5, columnspan=5)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 20, 'bold'), text="C", command=btnClear).grid(row=4, column=0)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 20, 'bold'), text="0", command=lambda: btnClick("0")).grid(row=4, column=1)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 20, 'bold'), text=".", command=lambda: btnClick(".")).grid(row=4, column=4)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 20, 'bold'), text="M", command=switch_frame).grid(row=4, column=2)

Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 18, 'bold'), text="sqrt", command=lambda: scientificFunction('sqrt')).grid(row=1, column=4)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 18, 'bold'), text="log", command=lambda: scientificFunction('log')).grid(row=2, column=4)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 18, 'bold'), text="exp", command=lambda: scientificFunction('exp')).grid(row=3, column=4)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 18, 'bold'), text="sin", command=lambda: scientificFunction('sin')).grid(row=1, column=5)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 18, 'bold'), text="cos", command=lambda: scientificFunction('cos')).grid(row=2, column=5)
Button(cal2, padx=16, bd=8, fg="green", bg="black", font=('arial', 18, 'bold'), text="tan", command=lambda: scientificFunction('tan')).grid(row=3, column=5)

matrix_frame = Frame(cal, bg="black")
matrix_frame.grid(row=10, column=0, columnspan=6, padx=5, pady=5)

window.mainloop()
