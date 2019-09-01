from tkinter import *
a = 0
root = Tk()
canvas =  Canvas(root, width=500, height=700)

Flag = False

def Plus(): 
    global a
    a += 1
def Minus():
    global a
    a -= 1
def Umnoshit():
    global a
    a *= 2

def Del():
    global a 
    a = a // 2

def Exit():
    global Flag
    Flag = True
    Label(canvas, text='You can Exit and do not have errors', font=20).place(x=200, y=300)
    

b = Button(canvas, text='+1', command=Plus).place(x=150, y=200)
b1 = Button(canvas, text='-1', command=Minus).place(x=200, y=200)
b2 = Button(canvas, text='*2', command=Umnoshit).place(x=250, y=200)
b3 = Button(canvas, text='/2', command=Del).place(x=300, y=200)
b4 = Button(canvas, text='Exit', command=Exit).place(x=250, y=350)


canvas.pack()
while True:
    Label(canvas, text=a, font=20).place(x=100, y=100)
    if Flag == True:
        break
    canvas.update()
root.mainloop()