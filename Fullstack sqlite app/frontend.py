from tkinter import *
import backend
root = Tk()
root.title("Online School")
root.geometry("540x350")

name = Label(root, text = "Course Name:", padx = 10, pady = 10, font = ("Helvetica", 12))
name.grid(row = 0, column = 0)
name_text = StringVar()
name_entry = Entry(root, textvariable = name_text)
name_entry.grid(row = 0, column = 1)

author = Label(root, text = "Author:", padx = 10, pady = 10, font = ("Helvetica", 12))
author.grid(row = 0, column = 2)
author_text = StringVar()
author_entry = Entry(root, textvariable = author_text)
author_entry.grid(row = 0, column = 3)

category = Label(root, text = "Category:", padx = 10, pady = 10, font = ("Helvetica", 12))
category.grid(row = 1, column = 0)
category_text = StringVar()
category_entry = Entry(root, textvariable = category_text)
category_entry.grid(row = 1, column = 1)

price = Label(root, text = "Price:", padx = 10, pady = 10, font = ("Helvetica", 12))
price.grid(row = 1, column = 2)
price_text = StringVar()
price_entry = Entry(root, textvariable = price_text)
price_entry.grid(row = 1, column = 3)

def get_selected_row(event):
    global selected_row
    index = listbox.curselection()[0]
    if index:
        selected_row = listbox.get(index)
        
listbox = Listbox(root, height = 10, width = 70)
listbox.grid(row = 6, column = 0, rowspan = 4, columnspan = 4)
listbox.bind("<<ListboxSelect>>", get_selected_row)

def create_entry():
    backend.create(name_text.get(), category_text.get(), author_text.get(), price_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (name_text.get(), category_text.get(), author_text.get(), price_text.get()))
    

create_entry_button = Button(root, text = "Create Course", command = create_entry, font = ("Helvetica", 12))
create_entry_button.grid(row = 3, column = 0, padx = 5, pady = 5)

def read_all():
    global list_row
    listrow = []
    listbox.delete(0, END)
    for row in backend.read_all():
        listbox.insert(END, row)

read_all_button = Button(root, text = "Show All courses", command = read_all, font = ("Helvetica", 12))
read_all_button.grid(row = 3, column = 1, padx = 5)

def update_course():
    backend.update(listbox.get(listbox.curselection()[0])[0], name_text.get(), category_text.get(), author_text.get(), price_text.get())

update_button = Button(root, text = "Update Course", command = update_course, font = ("Helvetica", 12))
update_button.grid(row = 3, column = 2, padx = 5)

def delete_course():
    backend.delete(listbox.get(listbox.curselection()[0])[0])
    read_all()
    
delete_button = Button(root, text = "Delete Course", command = delete_course, font = ("Helvetica", 12))
delete_button.grid(row = 3, column = 3, padx = 5)

def search():
    listbox.delete(0, END)
    for row in backend.search(name_text.get(), category_text.get(), author_text.get(), price_text.get()):
        listbox.insert(END, row)

search_button = Button(root, text = "Search course", command = search, font = ("Helvetica", 12))
search_button.grid(row = 4, column = 1, columnspan = 2, pady = 10, padx = 10)

root.mainloop()