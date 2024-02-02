import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Metric Converter")
root.geometry("300x80")
root.resizable(False, False)

main = ttk.Frame(root)
main.grid()

def convert():
    try:
        value = float(meters_value.get())
        feet_value.set('%.3f'%(value * 3.28084))
    except ValueError:
        pass

feet_value = tk.StringVar()
meters_value = tk.StringVar()

feet_label = ttk.Label(main, text = "feet")
feet_label.grid(column = 0, row = 1, padx = 30)
feet_display = ttk.Label(main, textvariable = feet_value)
feet_display.grid(column = 1, row = 1, padx = 30)

meters_label = ttk.Label(main, text = "meters") 
meters_label.grid(column = 0, row = 0, padx = 30, pady = 5)
meters_input = ttk.Entry(main, textvariable = meters_value)
meters_input.grid(column = 1, row = 0, padx = 30, pady = 5)
meters_input.focus()

convert_button = ttk.Button(main, text="Convert", command = convert)
convert_button.grid(column = 0, row = 2, columnspan = 2, padx = 30)

root.mainloop()