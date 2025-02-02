################################## Day 45: 69 Days of Python #####################################

# Tkinter Button

# from tkinter import *   
  
# top = Tk()  
  
# top.geometry("200x100")  
  
# b = Button(top,text = "Simple")  
  
# b.pack()  
  
# top.mainloop() 


'''
from tkinter import *
from tkinter import messagebox   
  
top = Tk()  
  
top.geometry("200x100")  
  
def funr():  
    messagebox.showinfo("Hello", "Red Button clicked")  
  
def funb():  
    messagebox.showinfo("Hello", "Blue Button clicked")
  
def fung():  
    messagebox.showinfo("Hello", "Green Button clicked")

def funy():  
    messagebox.showinfo("Hello", "Yellow Button clicked")
  
b1 = Button(top,text = "Red",command = funr,activeforeground = "red",activebackground = "red",pady=10)  
  
b2 = Button(top, text = "Blue",command = funb,activeforeground = "blue",activebackground = "blue",pady=10)  
  
b3 = Button(top, text = "Green",command = fung,activeforeground = "green",activebackground = "green",pady = 10)  
  
b4 = Button(top, text = "Yellow",command = funy,activeforeground = "yellow",activebackground = "yellow",pady = 10)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)  
  
top.mainloop()  
'''

# Tkinter Canvas

# from tkinter import *   
  
# top = Tk()  
  
# top.geometry("200x200")  
  
# #creating a simple canvas  
# c = Canvas(top,bg = "pink",height = "200")  
  
  
# c.pack()  
  
# top.mainloop()  


#  Creating an arc

'''
from tkinter import *   
  
top = Tk()  
  
top.geometry("200x200")  
  
#creating a simple canvas  
c = Canvas(top,bg = "pink",height = "200",width = 200)  
  
arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
  
c.pack()  
  
top.mainloop()
''' 

# Tkinter Checkbutton

'''
from tkinter import *   
  
top = Tk()  
  
top.geometry("200x200")  
  
checkvar1 = IntVar()  
  
checkvar2 = IntVar()  
  
checkvar3 = IntVar()  
  
chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn1.pack()  
  
chkbtn2.pack()  
  
chkbtn3.pack()  
  
top.mainloop()
'''

# Tkinter Entry
from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
name = Label(top, text = "Name").place(x = 30,y = 50)  
  
email = Label(top, text = "Email").place(x = 30, y = 90)  
  
password = Label(top, text = "Password").place(x = 30, y = 130)  
  
sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 170)  
  
e1 = Entry(top).place(x = 80, y = 50)  
  
  
e2 = Entry(top).place(x = 80, y = 90)  
  
  
e3 = Entry(top).place(x = 95, y = 130)  
  
top.mainloop()  


'''Next topic: Tkinter Frame -> Day 46'''

# Task: create a calculator using tkinter