#create top level window
from tkinter import *
root = Tk()
window = Toplevel(root)
window.title('New Window')
window.lower()#arranges the window backwards
window.lift(root)#lift the window
#window.state('zoomed') #expands the window to the maximum size
#window.state('withdraw')#it is withdrawn from the screen
#window.state('iconic')
#window.state('normal')
#window.state()
#window.iconify()
#window.deiconify()
#expanding the window
#window.geometry('640x480+50+100')# changes the size of the window
#preventing the user from resizing the window
#window.resizable(False, False)
#restricting the minimizing size
window.maxsize(640,480)
window.minsize(200,200)
window.resizable(True,True)
#destroy method
#root.destroy()


