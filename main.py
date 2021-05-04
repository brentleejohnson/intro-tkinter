# Tkinter
"""
import tkinter as tk


top = tk.Tk()


def hello_callback():
    tk.Message("Test", "Test")


b = tk.Button(text="Hello World", command=hello_callback)

b.pack()


top.mainloop()
"""


# Window Based Program
from tkinter import *
window = Tk()
window.title("GUI Lessons")
window.geometry("500x200")
lb_1 = Label(window, bg="pink", fg="blue", text="Another lion")
lb_1.pack()
window.mainloop()
