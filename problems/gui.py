from tkinter import *
import requests  
from tkinter.messagebox import * 
#from io import BytesIO  
res = ''
# создание окна
root = Tk()
root.geometry('300x300')
root.title('Test Internet')

# отступ перед Entry
Label(text='\t').grid(row=0, column=0)

# создание Entry
e1 = Entry()
e1.grid(row=0, column=1)

# Label
#Label(text=res).grid(row=1, column=0)
def PRbutton(Ent):
    global res, st
    URL = Ent.get()
    Label(text='\t\t\t').grid(row=2, columnspan=3)
    #Label(text='\t\t\t').grid(row=2, columnspan=3)
    Label(text='\t\t\t').grid(row=3, columnspan=3)
    try:
        res = requests.get(URL)       
        
        Label(text=res).grid(row=1, columnspan=3)
        #Label(text='{}'.format(res.headers)).grid(row=2, columnspan=3)
        Label(text='in utf-8 {} bit'.format(len(requests.get(URL).text) * 8)).grid(row=2, columnspan=3)
        #Label(text='in ascii {} bit'.format(len(requests.get(URL).text) * 7)).grid(row=3, columnspan=3)
        Label(text='in utf-32 {} bit'.format(len(requests.get(URL).text) * 32)).grid(row=3, columnspan=3)
    except:
        showerror('Error!', '{} is URL or wrong URL'.format(URL))
        
# создание кнопки
cmd = lambda x=e1: PRbutton(x) 
Button(text=' Test ', command=cmd).grid(row=0, column=2)

root.mainloop()