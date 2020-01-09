import tkinter
from random import randrange
t=tkinter.Tk()
t.resizable(0,0)
l=tkinter.StringVar()
s=tkinter.Label(t,width=36,font='Arial',textvariable=l)
l.set('Score:')
s.pack()
c=tkinter.Canvas(t,width=400,height=400,bg='#ffffff')
c.pack()
sq=[]
r=randrange(0,256)
g=randrange(0,256)
b=randrange(0,256)
for x in range(20):
    cp='#'+('%x'%r).rjust(2,'0')+('%x'%g).rjust(2,'0')+('%x'%b).rjust(2,'0')
    print(cp)
    m=randrange(0,8)*50
    n=randrange(0,8)*50
    sq.append(c.create_polygon((m,n,m,n+50,m+50,n+50,m+50,n),fill=cp))
    r/=1.1
    g/=1.1
    b/=1.1
    r=int(r)
    g=int(g)
    b=int(b)

