import tkinter
from random import randrange
t=tkinter.Tk()
f=tkinter.Frame(t)
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
    print(cp)
    m=randrange(0,8)*50
    n=randrange(0,8)*50
    sq.append(c.create_polygon((m,n,m,n+50,m+50,n+50,m+50,n),fill=cp))
    e.append(c.create_text(m+25,n+25,text=str(x+1),font='Arial',width=30))
    r/=1.1
    g/=1.1
    b/=1.1
    r=int(r)
    g=int(g)
    b=int(b)
print([c.coords(x) for x in sq])
print([c.find_overlapping(c.coords(x)[0],c.coords(x)[1],c.coords(x)[4],c.coords(x)[5]) for x in sq])
