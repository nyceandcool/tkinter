# Frames
from tkinter import *
from tkinter import ttk
root = Tk()
frame =ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief = RIDGE) # other properties are: FLAT, RAISED, SUNKEN, SOLID, RIDGE, GROOVE
#add widget
ttk.Button(frame, text = 'Click Me').grid()
frame.config(padding = (30,15))
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()


