from tkinter import *
from time import sleep
how_balls = 10
def DrawCircule(x, y, r): 
    c.create_oval(x - r, y - r, x + r, y + r, fill='green')
    
def DrawSnake():
    global table_x, table_y, how_balls
    i = 0
    while i < how_balls:
        DrawCircule(table_x[i], table_y[i], 25)
        i += 1
    
table_x = [0] * how_balls
table_y = [100] * how_balls

root = Tk()

root.title('Snake')

c = Canvas(root, width=1000, height=600)

c.pack()

c.configure(bg='black')

i = 0
while i < how_balls:    
    table_x[i] = i * 50 + 300
    i += 1

sleeping = 0.1 
DrawSnake()
k = 0 
while k < 5:
    DrawSnake()
    sleep(sleeping)
    c.update()
    c.delete('all')
    
    table_x.pop()
    table_y.pop()
    table_x.insert(0, table_x[0] - 50)
    table_y.insert(0, table_y[0])
    k += 1

k = 0
while k < 5:
    DrawSnake()
    sleep(sleeping)
    c.update()
    c.delete('all')
    table_x.pop()
    table_y.pop()
    
    table_x.insert(0, table_x[0])
    table_y.insert(0, table_y[0] + 50)    

    k += 1

k = 0
while k < 5:
    DrawSnake()
    sleep(sleeping)
    c.update()
    c.delete('all')
    table_x.pop()
    table_y.pop()
    
    table_x.insert(0, table_x[0] + 50)
    table_y.insert(0, table_y[0])    

    k += 1
    
k = 0
while k < 5:
    DrawSnake()
    sleep(sleeping)
    c.update()
    c.delete('all')
    table_x.pop()
    table_y.pop()
    
    table_x.insert(0, table_x[0])
    table_y.insert(0, table_y[0] - 50)    

    k += 1

DrawSnake()
sleep(0.5)
c.update()

def left():
    global table_x, table_y, sleeping
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
    
        table_x.pop()
        table_y.pop()
        table_x.insert(0, table_x[0] - 50)
        table_y.insert(0, table_y[0])
        k += 1

def down():
    global table_x, table_y, sleeping
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
        table_x.pop()
        table_y.pop()
        
        table_x.insert(0, table_x[0])
        table_y.insert(0, table_y[0] + 50)    
    
        k += 1
def right():
    global table_x, table_y, sleeping
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
        table_x.pop()
        table_y.pop()
        
        table_x.insert(0, table_x[0] + 50)
        table_y.insert(0, table_y[0])    
    
        k += 1
def up():
    global table_x, table_y, sleeping
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
        table_x.pop()
        table_y.pop()
        
        table_x.insert(0, table_x[0])
        table_y.insert(0, table_y[0] - 50)    
    
        k += 1
while True:        
    left()
    down()
    right()
    up()
    
    
DrawSnake()
root.mainloop() 