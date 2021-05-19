from tkinter import Tk
from tkinter import Label
import time
import sys

root = Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("%H:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)

digi_clock = Label(root, font=("arial",50),bg="white",fg="blue")
digi_clock.pack()


present_time()
root.mainloop()

