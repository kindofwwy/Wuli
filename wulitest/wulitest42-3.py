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

def maket(biao4,deep=0):
    if deep>n:
        return
    b=[d(biao4[0],biao4[1]),
       d(biao4[2],biao4[0]),
       d(biao4[3],biao4[0]),
       d(biao4[1],biao4[2]),
       d(biao4[1],biao4[3]),
       d(biao4[2],biao4[3])]
    maket([biao4[0],b[0],b[1],b[2]],deep+1)
    maket([b[0],biao4[1],b[3],b[4]],deep+1)
    maket([b[1],b[3],biao4[2],b[5]],deep+1)
    maket([b[2],b[4],b[5],biao4[3]],deep+1)

Phy.tready()
a=300
n=2
db=[Phy(1,[0,0,0],[0,a,0]),
    Phy(1,[0,0,0],[0,-a/(3*2**0.5),-4/(3*2**0.5)*a]),
    Phy(1,[0,0,0],[-2*a/6**0.5,-a/(3*2**0.5),a*2**0.5/3]),
    Phy(1,[0,0,0],[2*a/6**0.5,-a/(3*2**0.5),a*2**0.5/3])]
maket(db)
c=Phy.camera([0,0,-500])
t=0.513
dt=0.0011
while True:
    d.go(t)
    c.tplay()
    c.movecam(15,0.05)
    t+=dt
    if t>1 or t<0:
        dt=-dt