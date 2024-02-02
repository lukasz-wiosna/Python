from tkinter import *

root = Tk()
root.title("Form")
root.geometry("500x400")

fields = "First Name: \t", "Last Name: \t", "Course Name: \t", "Country: \t\t"

def built_form(root, fields):
    entries = []
    for field in fields:
        frame = Frame(root)
        frame.pack(side = TOP)
        label = Label(frame, text = field, pady = 20, font = ("Helvetica", 17))
        label.pack(side = LEFT)
        entry = Entry(frame)
        entry.pack(side = RIGHT)
        entries.append((field, entry))
        
    return entries
    
entries = built_form(root, fields)

def print_form(entries):
    for entry in entries:
       print("%s%s"%(entry[0], entry[1].get()))
    #print(entries)

button = Button(root, text = "Print", command = (lambda e = entries : print_form(entries)),
    font = ("Helvetica", 17))
button.pack()

root.mainloop()