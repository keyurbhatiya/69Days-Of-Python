################################## Day 47: 69 Days of Python #####################################


# thinker Menubutton
from tkinter import *  
  
top = Tk()  
  
top.geometry("200x250")  
  
menubutton = Menubutton(top, text = "Language", relief = FLAT)  
  
menubutton.grid()  
  
menubutton.menu = Menu(menubutton)  
  
menubutton["menu"]=menubutton.menu  
  
menubutton.menu.add_checkbutton(label = "Hindi", variable=IntVar())  
  
menubutton.menu.add_checkbutton(label = "English", variable = IntVar())  
  
menubutton.pack()  
  
top.mainloop() 



# MENU

from tkinter import Toplevel, Button, Tk, Menu  
  
top = Tk()  
menubar = Menu(top)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=top.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
  
top.config(menu=menubar)  
top.mainloop() 



# Tkinter Message

from tkinter import *  
  
top = Tk()  
top.geometry("100x100")  
var = StringVar()  
msg = Message( top, text = "Welcome to Javatpoint")  
  
msg.pack()  
top.mainloop()



# Tkinter messagebox
from tkinter import *  
  
from tkinter import messagebox  
  
top = Tk()  
  
top.geometry("100x100")      
  
messagebox.showinfo("info","Hi,theire")  
# messagebox.showwarning("warning","Warning")  
# messagebox.showerror("error","Error")
# messagebox.askquestion("question","Question")  
# messagebox.askyesno("yesno","Yes no")  
# messagebox.askyesnocancel("yesnocancel","Yesnocancel")  
# messagebox.askretrycancel("retrycancel","Retrycancel")
  
top.mainloop() 