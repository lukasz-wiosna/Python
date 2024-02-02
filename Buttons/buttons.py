import tkinter
from tkinter import ttk
import random

def generate_string(root):
    new_title = ""
    for index in range(10):
        new_title = new_title + chr(ord("A") + random.randrange(26))
    root.title(new_title)

def main():
    root = tkinter.Tk()
    root.title("Random String Generator")
    root.geometry("350x200")
    
    frame = ttk.Frame(root)
    frame.grid()
    
    label = ttk.Label(frame, text = "Welcome to the App")
    label.grid()
    
    button = ttk.Button(frame, text = "Generate the String")
    button.grid()
    button["command"] = lambda: generate_string(root)
    
    exit_button = ttk.Button(frame, text = "Exit", command = root.destroy)
    exit_button.grid()
    
    root.mainloop()
    
main()