import tkinter as tk
from tkinter import *

class TaskList(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        
        self.title("Task List")
        self.configure(bg="#0C1323")
        
        frame = tk.Frame(width = 350)
        frame.pack()
        
        instructions = tk.Label(self, text="Enter items into input field:", padx=20, pady=20, font = ("Arial", 16), fg="#FFFFFF", bg="#0C1323")
        self.tasks.append(instructions)
        
        for task in self.tasks:
            task.pack()
        
        self.new_task = tk.Text(self, height = 1, width = 40)
        self.new_task.pack(padx = 20, pady = 20)
        self.new_task.focus_set()
        
        self.bind("<Return>", self.add_task)
        
        self.colors = [
            {
                "bg": "#E15F14"
            },
            {
                "bg": "#0C1323"
            }
        ]
        
    def add_task(self, event=None):
        task_text = self.new_task.get(1.0, tk.END).strip()
        
        task_label = tk.Label(self, text=task_text, padx=10, pady=2, fg="#FFFFFF")
        
        _, task_color = divmod(len(self.tasks), 2)
        
        task_label.configure(bg=self.colors[task_color]["bg"])
        
        task_label.pack(fill = BOTH, expand = True)
        self.tasks.append(task_label)
        
        self.new_task.delete(1.0, tk.END)
        
        
        
if __name__ =="__main__":
    task_list = TaskList()
    task_list.mainloop()
        