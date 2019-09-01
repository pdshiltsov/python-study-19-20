from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.geometry('300x400')

Label(text='1').grid(row = 1, column = 2)
Entry().grid(row = 1, column = 1)

win.mainloop()

