#creating a checkbutton
from tkinter import *
from tkinter import ttk
root = Tk()
checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
checkbutton.pack()
spam = StringVar() #create variable
spam.set('SPAM!')
spam.get()
checkbutton.config(variable = spam, onvalue = 'SPAM Please', offvalue = 'Boo SPAM')
# create a radiobutton
breakfast = StringVar()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = 'SPAM').pack()
#multiplying radiobuttons
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast, value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast, value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = 'SPAM').pack()
# text variable
checkbutton.config(textvariable = breakfast)
