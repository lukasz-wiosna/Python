from tkinter import *
import time

root = Tk()
root.title("Digital Clock")
root.geometry("300x100")

clock = Label(root, text = "Clock", font = ("Helvetica", 50), pady = 20)
clock.pack()

def tick():
    global current_time
    current_time = time.strftime("%H:%M:%S")
    current_time_previous = "0"
    
    if current_time_previous != current_time:
        current_time_previous = current_time
        clock.config(text = current_time)
    
    clock.after(200, tick)
tick()

root = mainloop()