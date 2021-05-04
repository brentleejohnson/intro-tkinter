# Import the 'tkinter' module
import tkinter as tk


window = tk.Tk()
window["background"]="white"

# create the title for the window
window.title("add,subtract,multiply and exit")
window.geometry("400x200")

# creating the add subtract multiply and exit buttons widget(btn)
btn1 = tk.Button(window, text="Add")
btn2 = tk.Button(window, text="Clear")
btn3 = tk.Button(window, text="Exit")


# Adding the widgets, in order to the keyword
btn1.pack()
btn2.pack()
btn3.pack()

# Finally, draw the window + start the app
window.mainloop()
