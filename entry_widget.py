#Entry Widgets
from tkinter import *
from tkinter import ttk
root = Tk()
entry = ttk.Entry(root, width = 30)
entry.pack()

#other commands
# entry.delete(0,1) this deletes the 2nd letter
#entry.delete(0, END) this deletes all the letters
#entry.insert(0, 'Enter your password') displays a message that says "Enter your password"
#entry.config(show = '*') hides the characters or numbers the user is entering 'good for hiding passwords
#entry.get() displays 
#entry.state(['disabled'])
#entry.state([!'disabled'])
entry.state(['readonly'])
