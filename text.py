from tkinter import *
root = Tk()
text = Text(root, width = 40, height = 10)
text.pack()
#control where text should appear 'wrap'
text.config(wrap = 'word')
text.get('1.0', 'end')

