from wuli import *
import turtle
class d(Phy):
    biao=[]
    def __init__(self,c,b,m=1,v=(0,0,0),p=(0,0,0),color="black"):
        super().__init__(m,v,p,r=5,color=color)
        self.c=c
        self.b=b
        d.biao.append(self)

    def gop(self,t):
        self.c.resilience(other=self,k=0)
        self.b.resilience(other=self,k=0)
        self.p=[self.c.p[0]*(1-t)+self.b.p[0]*t,
                self.c.p[1]*(1-t)+self.b.p[1]*t,
                self.c.p[2]*(1-t)+self.b.p[2]*t]

    @classmethod
    def go(cls,t):
        for i in d.biao:
            i.gop(t)

def make(biao):
    b2=[]
    for i in range(0,len(biao)-1):
        a=d(biao[i],biao[i+1],color=[1/(len(biao)-1),0,0])
        b2.append(a)
    if len(b2)>1:
        make(b2)
def dot(x,y):
    global db
    db.append(Phy(1,[0,0,0],[x,y,0],r=5))
def sw():
    global s
    s=int(not(s))

s=0
Phy.tready()
while True:
    db=[]
    Phy.biao=[]
    d.biao=[]
    while s==0:
        turtle.onscreenclick(dot)
        turtle.onkey(sw," ")
        Phy.tplay()
        turtle.listen()
    make(db)
    d.biao[-1].color="red"
    t=-0.5
    dt=0.0011
    e=Phy.tgraph()
    while s:
        d.go(t)
        e.draw(d.biao[-1].p[0],d.biao[-1].p[1],[0,0],tiao=50,color="red",bi=True)
        turtle.onkey(sw, " ")
        Phy.tplay()
        turtle.listen()
        t+=dt
