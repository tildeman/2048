import tkinter
from random import randrange
t=tkinter.Tk()
l=tkinter.StringVar()
s=tkinter.Label(t,width=36,font='Arial',textvariable=l)
l.set('Score:')
s.pack()
c=tkinter.Canvas(t,width=400,height=400,bg='#ffffff')
c.pack()
sq=[]
p=randrange(0,16777217)
for x in range(20):
    cp='#'+('%x'%p).rjust(6,'0')
    print(cp)
    m=randrange(0,8)*50
    n=randrange(0,8)*50
    sq.append(c.create_polygon((m,n,m,n+50,m+50,n+50,m+50,n),fill=cp))
    p//=2

