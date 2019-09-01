from tkinter import *
from time import *
from random import *

point_bonus = False

Count = 0 

X = randrange(25, 975, 25)
Y = randrange(25, 575, 25)

how_balls = 4
def DrawRec(x, y, r): 
    canvas.create_rectangle(x, y, x+r, y+r, outline='green', fill='green')
    
def GameOver():
    global Count
    DrawCanvas()
    DrawBonus()
    DrawSnake()
    DrawCount()
    Label(canvas, text='Game Over', bg='red', font=24).place(x=500, y=300)
    canvas.update()

def DrawCanvas():
    canvas.create_rectangle(0, 0, 1000, 600, outline='snow', fill='snow')
    canvas.create_rectangle(25, 25, 975, 575, outline='black', fill='black')
def DrawSnake():
    '''global table_x, table_y
    i = 0
    while i < len(table_x):
        canvas.create_rectangle(table_x[i], table_y[i], table_x[i] + 25, table_y[i] + 25, outline='green', fill='green')
        i += 1
        '''
    global table_x, table_y, how_balls, point_bonus
    #CLASSIC
    i = 0
    while i < how_balls:
        '''if table_x[i] == 1000:
            table_x[i] = 0
        elif table_x[i] == 0:
            table_x[i] = 1000
        elif table_y[i] == 600:
            table_y[i] = 0
        elif table_y[i] == 0:
            table_y[i] = 600'''
        DrawRec(table_x[i], table_y[i], 25)
        i += 1
        
    
def DrawBonus():
    global point_bonus, X, Y, table_x, table_y, how_balls, Count
    if (table_x[0] == X) and (table_y[0] == Y):
        point_bonus = True
        table_x.append(table_x[-1] + 25)
        table_y.append(table_x[-1])
        how_balls += 1
        Count += 1
    if not point_bonus:
        canvas.create_rectangle(X, Y, X + 25, Y + 25, outline='red', fill='red')    
    else:
        point_bonus = False
        X = randrange(25, 975, 25)
        Y = randrange(25, 575, 25)        
def DrawCount():
    Label(canvas, text=Count).place(x=25, y=575)

def DrawAll():
    DrawCanvas() #Рисуем поле
    DrawSnake() #Рисуем Змейку
    DrawBonus() #Рисуем Бонус
    DrawCount() #Рисуем Счёт
    sleep(0.1)
    canvas.update()
    #canvas.delete('all')

MoveX = -1
MoveY = 0

def left(event):
    global MoveX, MoveY
    MoveX = -1 
    MoveY = 0

def right(event):
    global MoveX, MoveY
    MoveX = 1 
    MoveY = 0
        
def up(event):
    global MoveX, MoveY
    MoveX = 0
    MoveY = -1

def down(event):
    #canvas.create_rectangle(0, 0, 1000, 600, outline='grey7', fill='yellow')
    global MoveX, MoveY
    MoveX = 0 
    MoveY = 1
        


win = Tk()
win.title('NewSnake')
canvas = Canvas(win, width=1000, height=600)
canvas.pack()

win.bind('<Left>', left)
win.bind('<Right>', right)
win.bind('<Up>', up)
win.bind('<Down>', down)

table_x = [300, 325, 350, 375] #массив с координатами по оси X квадратов змейки
table_y = [100, 100, 100, 100] #массив с координатами по оси Y квадратов змейки
flag = False
while True:    
    if (table_x[0] == 0 and MoveX == -1) or (table_x[0] == 1000 and MoveX == 1) or (table_y[0] == 0 and MoveY == -1) or (table_y[0] == 600 and MoveY == 1):
        break
    table_x.insert(0, table_x[0] + MoveX * 25)
    table_y.insert(0, table_y[0] + MoveY * 25)
    table_x.pop()
    table_y.pop()
    
    for i in range(1, len(table_x)):
        if table_x[0] == table_x[i] and table_y[0] == table_y[i]:
            flag = True
    if flag == True:
        break
    
    DrawAll() #рисуем всё
GameOver()
win.mainloop()