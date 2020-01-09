import tkinter
from random import randrange
t=tkinter.Tk()
l=tkinter.StringVar()
s=tkinter.Label(t,width=72,font='Arial',textvariable=l)
l.set('Score:')
s.pack()
c=tkinter.Canvas(t,width=800,height=800,bg='#ffffff')
c.pack()
sq=[]
for x in range(10):
    m=randrange(0,8)*100
    n=randrange(0,8)*100
    sq.append(c.create_polygon((m,n,m,n+100,m+100,n+100,m+100,n),fill='#000000'))

