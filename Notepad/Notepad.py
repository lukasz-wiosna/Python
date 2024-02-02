import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title('Notes')

def Open():
    root.filename = filedialog.askopenfilename(
        initialdir = "/",
        title = "Select file",
        filetypes = (("txt files", "*.txt"), ("all files", "*.*"))
    )
    file = open(root.filename)
    textarea.insert("end", file.read())
    
    
def Save():
    pass
    
def SaveAs():
    root.filename = filedialog.asksaveasfile(mode="w", defaultextension="*.txt")
    if root.filename is None:
        return
    file_to_save = str(textarea.get(1.0, END))
    root.filename.write(file_to_save)
    root.filename.close()
    
def Close():
    message = messagebox.askquestion("Notepad", "Do you want to save")
    if message == "yes":
        SaveAs()
    else:
        root.destroy()

textarea = ScrolledText(root)
textarea.pack()

menu = Menu(root)
file = Menu(menu, tearoff = 0)
menu.add_cascade(label="File", menu=file)
file.add_command(label="Open", command=Open)
file.add_command(label="Save", command=Save)
file.add_command(label="Save As...", command=SaveAs)
file.add_separator()
file.add_command(label="Close", command=Close)


root.config(menu=menu)


root.mainloop()