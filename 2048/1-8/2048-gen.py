def goup(event):
    for y in range(7):
        for x in sq:
            v=c.coords(x)
            while len(c.find_overlapping(v[0]+1,v[1],v[2]-1,v[3]-1))<2 and v[1]>0:
                c.move(x,0,-1)
                v=c.coords(x)
    makesq()
def godown(event):
    for y in range(7):
        for x in sq:
            v=c.coords(x)
            while len(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]))<2 and v[3]<400:
                c.move(x,0,1)
                v=c.coords(x)
    makesq()
def goleft(event):
    for y in range(7):
        for x in sq:
            v=c.coords(x)
            while len(c.find_overlapping(v[0],v[1]+1,v[2]-1,v[3]-1))<2 and v[0]>0:
                c.move(x,-1,0)
                v=c.coords(x)
    makesq()
def goright(event):
    for y in range(7):
        for x in sq:
            v=c.coords(x)
            while len(c.find_overlapping(v[0]+1,v[1]+1,v[2],v[3]-1))<2 and v[2]<400:
                c.move(x,1,0)
                v=c.coords(x)
    makesq()
def gsq():
    if len(sq)>63: return True
    m=randrange(0,8)*50
    n=randrange(0,8)*50
    if [m,n,m+50,n+50] in [c.coords(xx) for xx in sq]:
        while [m,n,m+50,n+50] in [c.coords(xx) for xx in sq]:
            m=randrange(0,8)*50
            n=randrange(0,8)*50
    sq.append(c.create_rectangle((m,n,m+50,n+50),fill=e[0]))
def makesq():
    if gsq():
        tx=c.create_text(200,200,text='Game over',font='Arial')
from time import sleep
import tkinter
from random import randrange
t=tkinter.Tk()
f=tkinter.Frame(t)
t.bind('<Up>',goup)
t.bind('<Down>',godown)
t.bind('<Left>',goleft)
t.bind('<Right>',goright)
f.pack()
t.resizable(0,0)
l=tkinter.StringVar()
s=tkinter.Label(f,width=36,font='Arial',textvariable=l)
l.set('Score:')
s.pack()
c=tkinter.Canvas(f,width=400,height=400,bg='#ffffff')
c.pack()
e=[]
sq=[]
r=randrange(128,256)
g=randrange(128,256)
b=randrange(128,256)
for x in range(20):
    cp='#'+('%x'%r).rjust(2,'0')+('%x'%g).rjust(2,'0')+('%x'%b).rjust(2,'0')
    e.append(cp)
    r/=1.1
    g/=1.1
    b/=1.1
    r=int(r)
    g=int(g)
    b=int(b)
makesq()
