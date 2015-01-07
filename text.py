from tkinter import *
root = Tk()
text = Text(root, width = 40, height = 10)
text.pack()
#control where text should appear 'wrap'
text.config(wrap = 'word')
text.get('1.0', 'end')
text.get('1.0', '1.end')
text.insert('1.0 + 2 lines', 'Insert message')
text.insert('1.0 + 2 lines lineend',  ' and\nmore and\nmore...')
text.delete('1.0')
text.delete('1.0', '1.0 lineend')
text.delete('1.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is the first line.')
text.config(state = 'disabled')
text.delete('1.0', 'end')
text.config(state = 'normal')

