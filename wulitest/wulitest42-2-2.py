from wuli import *
import turtle
class d(Phy):
    biao=[]
    def __init__(self,c,b,m=1,v=(0,0,0),p=(0,0,0),color="black"):
        super().__init__(m,v,p,r=1,color=color)
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

def maket(biao3,deep=0):
    if deep>n:
        return
    a=d(biao3[0],biao3[1])
    b=d(biao3[1],biao3[2])
    c=d(biao3[2],biao3[0])
    maket([a,b,c],deep+1)

Phy.tready()
a=400
n=20
db=[Phy(1,[0,0,0],[0,a,0]),
    Phy(1,[0,0,0],[3**0.5*a/2,-a/2,0]),
    Phy(1,[0,0,0],[-3**0.5*a/2,-a/2,0])]
maket(db)
t=0.013
dt=0.0051
while True:
    d.go(t)
    Phy.tplay()
    t+=dt
    if t>1 or t<0:
        dt=-dt