from tkinter import *
from time import sleep
from random import randint
how_balls = 15
shir = 25
def DrawRec(x, y, r): 
    c.create_rectangle(x, y, x+r, y+r, outline='green', fill='green')
def DrawSnake():
    global table_x, table_y, how_balls, shir
    i = 0
    while i < how_balls:
        DrawRec(table_x[i], table_y[i], shir)
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
    table_x[i] = i * shir + 300
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
    table_x.insert(0, table_x[0] - shir)
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
    table_y.insert(0, table_y[0] + shir)    

    k += 1

k = 0
while k < 5:
    DrawSnake()
    sleep(sleeping)
    c.update()
    c.delete('all')
    table_x.pop()
    table_y.pop()
    
    table_x.insert(0, table_x[0] + shir)
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
    table_y.insert(0, table_y[0] - shir)    

    k += 1

DrawSnake()
sleep(sleeping)
c.update()

def left():
    global table_x, table_y, sleeping, shir
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
    
        table_x.pop()
        table_y.pop()
        table_x.insert(0, table_x[0] - shir)
        table_y.insert(0, table_y[0])
        k += 1

def down():
    global table_x, table_y, sleeping, shir
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
        table_x.pop()
        table_y.pop()
        
        table_x.insert(0, table_x[0])
        table_y.insert(0, table_y[0] + shir)    
    
        k += 1
def right():
    global table_x, table_y, sleeping, shir
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
        table_x.pop()
        table_y.pop()
        
        table_x.insert(0, table_x[0] + shir)
        table_y.insert(0, table_y[0])    
    
        k += 1
def up():
    global table_x, table_y, sleeping, shir
    k = 0
    while k < 5:
        DrawSnake()
        sleep(sleeping)
        c.update()
        c.delete('all')
        table_x.pop()
        table_y.pop()
        
        table_x.insert(0, table_x[0])
        table_y.insert(0, table_y[0] - shir)    
    
        k += 1
while True:        
    left()
    down()
    right()
    up()
    
    
DrawSnake()
root.mainloop() 