################################## Day 44: 69 Days of Python #####################################

# Python Tkinter

# Tkinter is a Python interface to the Tk GUI toolkit.

# Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.
# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

# Tkinter is the de facto standard GUI library for Python.
# It is a thin object-oriented layer on top of Tcl/Tk.

# Tkinter installation
# pip install tkinter

# import tkinter
import tkinter as tk

# Create a window
window = tk.Tk()

# Create a label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Run the window
window.mainloop()

# Output:
# Hello, Tkinter!

# Tkinter widgets

# Label
# Button
# Entry
# Frame
# Checkbutton
# Radiobutton
# Listbox
# Scrollbar
# Canvas
# Menubar
# Message
# Spinbox
# Scale

# pack() method
# The pack() method is used to add a widget to the window. It is used to add a widget to the window.

# example

from tkinter import *  
parent = Tk()  
redbutton = Button(parent, text = "Red", fg = "red")  
redbutton.pack( side = LEFT)  
greenbutton = Button(parent, text = "Black", fg = "black")  
greenbutton.pack( side = RIGHT )  
bluebutton = Button(parent, text = "Blue", fg = "blue")  
bluebutton.pack( side = TOP )  
blackbutton = Button(parent, text = "Green", fg = "red")  
blackbutton.pack( side = BOTTOM)  
parent.mainloop() 


# grid() method


from tkinter import *  
parent = Tk()  
name = Label(parent,text = "Name").grid(row = 0, column = 0)  
e1 = Entry(parent).grid(row = 0, column = 1)  
password = Label(parent,text = "Password").grid(row = 1, column = 0)  
e2 = Entry(parent).grid(row = 1, column = 1)  
submit = Button(parent, text = "Submit").grid(row = 4, column = 0)  
parent.mainloop()  

# place() method

from tkinter import *  
top = Tk()  
top.geometry("400x250")  
name = Label(top, text = "Name").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30, y = 90)  
password = Label(top, text = "Password").place(x = 30, y = 130)  
e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 95, y = 130)  
top.mainloop()  

''' Next Topic: Tkinter Button ---> Day_45.py '''