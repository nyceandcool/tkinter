#compo box and spin button
from tkinter import *
from tkinter import ttk
root = Tk()
month = StringVar() #variable
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
#enter the values
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'))
#selecting a value
month.get()
'Mar'
month.set('Dec')
month.set('Not a month')
month.get()
# Spin Box
year = StringVar()
Spinbox(root, from_ =1990, to = 2014, textvariable = year).pack() #'from_' has an underscore because the word 'from ' is protected

