# using '*' asterick, will import all of the functions and variables from the base Tkinter package
# Along with their names, and this allows them to be called by name
#CREATING THE TOP WINDOW 
from tkinter import *
from tkinter import ttk
root = Tk() # this create the parent or root window for other widgets 'Top level window'

# CREATING A BUTTON
button = ttk.Button(root, text= 'Click Me') #call the 'ttk' constructor method

#DISPLAY THE BUTTON USING THE PACK METHOD
button.pack()

button['text'] #to see the value of button we created we use

button['text'] = 'Press Me' # opition 1.Assigning a new value to a property or use the code below
button.config(text = 'Push Me')# opition 2.Assigning a new value to a property
button.config() # Reveals the dictionary of all the properties
str(button) # to reveals the underlining tk name 
str(root)# reveals the root 






