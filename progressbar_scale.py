from tkinter import *
from tkinter import ttk
root = Tk()
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()
# if your not sure of the steps you can use the 'indeterminate'
progressbar.config(mode = 'indeterminate')
progressbar.start()
progressbar.stop()
#if you know the steps use this code below
progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
progressbar.config(value = 8.0)
progressbar.step()#increment by 1
progressbar.step(5)
#auto increment
value = DoubleVar()
progressbar.config(variable = value)
scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
scale.pack()
scale.set(4.2)
scale.get()
#
