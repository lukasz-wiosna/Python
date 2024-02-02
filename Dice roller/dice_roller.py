import tkinter as tk
import random

root = tk.Tk()
root.title("Dice Roller")
root.geometry("250x170")
root.configure(background = "gray")

def roll():
    print("Rolling")
    number_generated.set(str(random.randint(1, 6)))

number_generated = tk.StringVar()
number_generated.set("1 to 6")

label = tk.Label(root, textvariable = number_generated, background = "gray", font = ("Helvetica", 25), pady = 20)
label.pack()

button = tk.Button(root, text = "Roll", pady = 10, padx = 10, font = ("Helvetica", 20), background = "gray", highlightbackground = "red", highlightcolor = "red", activebackground = "black", activeforeground = "white", command = roll)
button.pack()

root.mainloop()