import tkinter as tk
from tkinter import *
import parser
from math import factorial
from math import sqrt

root = Tk()
root.title('Calculator')

# i variable tracks current position in display filed
i = 0

# this function receives the digit as parameter and displays in the display field
def get_variables(num):
    global i
    display.insert(i, num)
    i+=1

# this function is for mapping operator buttons
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

# this is function for AC button    
def clear_all():
    display.delete(0, END)

# mapping undo button
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

# mapping = button        
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")
        
# mapping factorial button

def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")
        
# mapping square root button

def squareroot():
    entire_string = display.get()
    try:
        result = sqrt(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")
        
# input field
display = Entry(root, font = ("Arial", 18, "bold"), width = 25)
display.grid(column = 0, row = 1, columnspan = 8, padx = 2, pady = 10, sticky = N+E+W+S)

# buttons
btn1 = tk.Button(root, text = "1", command = lambda : get_variables(1), font = ("Arial", 15), width = 4, height = 2)
btn1.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = N+S+E+W)
btn2 = tk.Button(root, text = "2", command = lambda : get_variables(2), font = ("Arial", 15), width = 4, height = 2)
btn2.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = N+S+E+W)
btn3 = tk.Button(root, text = "3", command = lambda : get_variables(3), font = ("Arial", 15), width = 4, height = 2)
btn3.grid(row = 2, column = 2, padx = 2, pady = 2, sticky = N+S+E+W)

btn4 = tk.Button(root, text = "4", command = lambda : get_variables(4), font = ("Arial", 15), width = 4, height = 2)
btn4.grid(row = 3, column = 0, padx = 2, pady = 2, sticky = N+S+E+W)
btn5 = tk.Button(root, text = "5", command = lambda : get_variables(5), font = ("Arial", 15), width = 4, height = 2)
btn5.grid(row = 3, column = 1, padx = 2, pady = 2, sticky = N+S+E+W)
btn6 = tk.Button(root, text = "6", command = lambda : get_variables(6), font = ("Arial", 15), width = 4, height = 2)
btn6.grid(row = 3, column = 2, padx = 2, pady = 2, sticky = N+S+E+W)

btn7 = tk.Button(root, text = "7", command = lambda : get_variables(7), font = ("Arial", 15), width = 4, height = 2)
btn7.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = N+S+E+W)
btn8 = tk.Button(root, text = "8", command = lambda : get_variables(8), font = ("Arial", 15), width = 4, height = 2)
btn8.grid(row = 4, column = 1, padx = 2, pady = 2, sticky = N+S+E+W)
btn9 = tk.Button(root, text = "9", command = lambda : get_variables(9), font = ("Arial", 15), width = 4, height = 2)
btn9.grid(row = 4, column = 2, padx = 2, pady = 2, sticky = N+S+E+W)

# other buttons
btn_ac = tk.Button(root, text = "AC", command = lambda : clear_all(), font = ("Arial", 15), width = 4, height = 2)
btn_ac.grid(row = 5, column = 0, padx = 2, pady = 2, sticky = N+S+E+W)
btn0 = tk.Button(root, text = "0", command = lambda : get_variables(0), font = ("Arial", 15), width = 4, height = 2)
btn0.grid(row = 5, column = 1, padx = 2, pady = 2, sticky = N+S+E+W)
btn_dot = tk.Button(root, text = ".", command = lambda : get_variables("."), font = ("Arial", 15), width = 4, height = 2)
btn_dot.grid(row = 5, column = 2, padx = 2, pady = 2, sticky = N+S+E+W)

# operations buttons
btn_add = tk.Button(root, text = "+", command = lambda : get_operation("+"), font = ("Arial", 15), width = 4, height = 2)
btn_add.grid(row = 2, column = 4, padx = 2, pady = 2, sticky = N+S+E+W)
btn_substr = tk.Button(root, text = "-", command = lambda : get_operation("-"), font = ("Arial", 15), width = 4, height = 2)
btn_substr.grid(row = 3, column = 4, padx = 2, pady = 2, sticky = N+S+E+W)
btn_multiply = tk.Button(root, text = "×", command = lambda : get_operation("*"), font = ("Arial", 15), width = 4, height = 2)
btn_multiply.grid(row = 4, column = 4, padx = 2, pady = 2, sticky = N+S+E+W)
btn_divide = tk.Button(root, text = "÷", command = lambda : get_operation("/"), font = ("Arial", 15), width = 4, height = 2)
btn_divide.grid(row = 5, column = 4, padx = 2, pady = 2, sticky = N+S+E+W)


btn_pi = tk.Button(root, text = "π", command = lambda : get_operation("*3.14"), font = ("Arial", 15), width = 4, height = 2)
btn_pi.grid(row = 2, column = 5, padx = 2, pady = 2, sticky = N+S+E+W)
btn_percent = tk.Button(root, text = "%", command = lambda : get_operation("%"), font = ("Arial", 15), width = 4, height = 2)
btn_percent.grid(row = 3, column = 5, padx = 2, pady = 2, sticky = N+S+E+W)
btn_bracket = tk.Button(root, text = "(", command = lambda : get_operation("("), font = ("Arial", 15), width = 4, height = 2)
btn_bracket.grid(row = 4, column = 5, padx = 2, pady = 2, sticky = N+S+E+W)
btn_exp = tk.Button(root, text = "x²", command = lambda : get_operation("**"), font = ("Arial", 15), width = 4, height = 2)
btn_exp.grid(row = 5, column = 5, padx = 2, pady = 2, sticky = N+S+E+W)

btn_undo = tk.Button(root, text = "↺", command = lambda : undo(), font = ("Arial", 15), width = 4, height = 2)
btn_undo.grid(row = 2, column = 6, padx = 2, pady = 2, sticky = N+S+E+W)
btn_factorial = tk.Button(root, text = "n!", command = lambda : fact(), font = ("Arial", 15), width = 4, height = 2)
btn_factorial.grid(row = 3, column = 6, padx = 2, pady = 2, sticky = N+S+E+W)
btn_bracket1 = tk.Button(root, text = ")", command = lambda : get_operation(")"), font = ("Arial", 15), width = 4, height = 2)
btn_bracket1.grid(row = 4, column = 6, padx = 2, pady = 2, sticky = N+S+E+W)
btn_sqrt = tk.Button(root, text = "√", command = lambda : squareroot(), font = ("Arial", 15), width = 4, height = 2)
btn_sqrt.grid(row = 5, column = 6, padx = 2, pady = 2, sticky = N+S+E+W)
btn_calc = tk.Button(root, text = "=", command = lambda : calculate(), font = ("Arial", 15), width = 4, height = 2)
btn_calc.grid(row = 6, column = 0, columnspan = 7, padx = 2, pady = 2, sticky = N+S+E+W)

root.mainloop()

