def countsc(score):
    global sc
    sc+=score
    l.set('Score: '+str(sc))
    if score>=2048:
        tx=c.create_text(200,200,text='You got 2048',font='Arial',fill='#ffff00')
def goup(event):
    m=[]
    for x in range(4):
        for y in range(4):
            v=[x*100,y*100,x*100+100,y*100+100]
            if len(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1))>=1:
                m.append(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1)[0])
    for x in range(len(m)):
        v=c.coords(m[x])
        if len(v)>2:
            while len(c.find_overlapping(v[0]+1,v[1],v[2]-1,v[3]-1))<2 and v[1]>0:
                c.move(m[x],0,-1)
                v=c.coords(m[x])
            ov=c.find_overlapping(v[0]+1,v[1],v[2]-1,v[3]-1)
            if len(ov)>=2 and c.itemcget(ov[0],'fill')==c.itemcget(ov[1],'fill'):
                c.itemconfig(ov[0],fill=e[e.index(c.itemcget(ov[0],'fill'))+1])
                countsc(2**e.index(c.itemcget(ov[0],'fill')))
                c.delete(ov[1])
    makesq()
def godown(event):
    m=[]
    for x in range(3,-1,-1):
        for y in range(4):
            v=[x*100,y*100,x*100+100,y*100+100]
            if len(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1))>=1:
                m.append(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1)[0])
    for x in range(len(m)):
        v=c.coords(m[x])
        if len(v)>2:
            while len(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]))<2 and v[3]<400:
                c.move(m[x],0,1)
                v=c.coords(m[x])
            ov=c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3])
            if len(ov)>=2 and c.itemcget(ov[1],'fill')==c.itemcget(ov[0],'fill'):
                c.itemconfig(ov[0],fill=e[e.index(c.itemcget(ov[0],'fill'))+1])
                countsc(2**e.index(c.itemcget(ov[0],'fill')))
                c.delete(ov[1])
    makesq()
def goleft(event):
    m=[]
    for x in range(4):
        for y in range(4):
            v=[x*100,y*100,x*100+100,y*100+100]
            if len(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1))>=1:
                m.append(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1)[0])
    for x in range(len(m)):
        v=c.coords(m[x])
        if len(v)>2:
            while len(c.find_overlapping(v[0],v[1]+1,v[2]-1,v[3]-1))<2 and v[0]>0:
                c.move(m[x],-1,0)
                v=c.coords(m[x])
            ov=c.find_overlapping(v[0],v[1]+1,v[2]-1,v[3]-1)
            if len(ov)>=2 and c.itemcget(ov[0],'fill')==c.itemcget(ov[1],'fill'):
                c.itemconfig(ov[0],fill=e[e.index(c.itemcget(ov[0],'fill'))+1])
                countsc(2**e.index(c.itemcget(ov[0],'fill')))
                c.delete(ov[1])
    makesq()
def goright(event):
    m=[]
    for x in range(4):
        for y in range(3,-1,-1):
            v=[x*100,y*100,x*100+100,y*100+100]
            if len(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1))>=1:
                m.append(c.find_overlapping(v[0]+1,v[1]+1,v[2]-1,v[3]-1)[0])
    for x in range(len(m)):
        v=c.coords(m[x])
        if len(v)>2:
            while len(c.find_overlapping(v[0]+1,v[1]+1,v[2],v[3]-1))<2 and v[2]<400:
                c.move(m[x],1,0)
                v=c.coords(m[x])
            ov=c.find_overlapping(v[0]+1,v[1]+1,v[2],v[3]-1)
            if len(ov)>=2 and c.itemcget(ov[0],'fill')==c.itemcget(ov[1],'fill'):
                c.itemconfig(ov[0],fill=e[e.index(c.itemcget(ov[0],'fill'))+1])
                countsc(2**e.index(c.itemcget(ov[0],'fill')))
                c.delete(ov[1])
    makesq()
def gsq():
    if len(c.find_all())>15: return True
    m=randrange(0,4)*100
    n=randrange(0,4)*100
    if [m,n,m+100,n+100] in [c.coords(xx) for xx in sq]:
        while [m,n,m+100,n+100] in [c.coords(xx) for xx in sq]:
            m=randrange(0,4)*100
            n=randrange(0,4)*100
    sq.append(c.create_rectangle((m,n,m+100,n+100),fill=e[0]))
def makesq():
    if gsq():
        tx=c.create_text(200,200,text='Game over',font='Arial',fill='#ffff00')
from time import sleep
import tkinter
from random import randrange
sc=0
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
l.set('Score: '+str(sc))
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
t.mainloop()
