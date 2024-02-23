from wuli import *
import random,turtle

def zuobiaoxian(x):
    xian=[Phy.xianxing([100,0,0],x),
          Phy.xianxing([0,100,0],x),
          Phy.xianxing([0,0,100],x)]
    turtle.goto(xian[2][0],xian[2][1])
    turtle.dot(3,"red")
    for i in range(len(xian)):
        turtle.pencolor("black")
        turtle.goto(0,0)
        turtle.pd()
        turtle.goto(xian[i][0],xian[i][1])
        turtle.pu()


def r(x,y):
    biao[random.randint(0,7)].force2(10000000,[x,y,0])

def fw():
    dl=(d[0]**2+d[2]**2)**0.5
    d0.p[0] += d[0] / dl *buchang
    d0.p[2] += d[2] / dl *buchang
def bw():
    dl = (d[0]**2+d[2]**2)**0.5
    d0.p[0] -= d[0] / dl *buchang
    d0.p[2] -= d[2] / dl *buchang
def le():
    dl = (d[0]**2+d[2]**2)**0.5
    d0.p[0] -= d[2] / dl *buchang
    d0.p[2] -= -d[0] / dl *buchang
def ri():
    dl = (d[0]**2+d[2]**2)**0.5
    d0.p[0] += d[2] / dl *buchang
    d0.p[2] += -d[0] / dl *buchang
def zp():
    d0.p[1]+=buchang
def zn():
    d0.p[1]-=buchang

def cu():
    d[1]+=cbuchang
def cd():
    d[1]-=cbuchang
def cl():
    dl = (d[0] ** 2 + d[2] ** 2) ** 0.5
    d[0] -= d[2] / dl*cbuchang
    d[2] -= -d[0] / dl*cbuchang
def cr():
    dl = (d[0] ** 2 + d[2] ** 2) ** 0.5
    d[0] += d[2] / dl*cbuchang
    d[2] += -d[0] / dl*cbuchang
def zp2():
    d[2]+=cbuchang
def zn2():
    d[2]-=cbuchang


d=[0,0,10]
d0=Phy(1, [0, 0, 0], [0, 0, -300])
cbuchang=0.5
buchang=5

dp=Phy(1,[0,0,0],[d[0] + d0.p[0], d[1] + d0.p[1], d[2] + d0.p[2]],r=5,color="red")

Phy.tready()
a=[50,50,50]
biao=[]
for i in range(8):
    biao.append(Phy(5,[0,0,0],a[:]))
    if i%4==0:
        a[1]-=100
    elif i%4==1:
        a[0]-=100
    elif i%4==2:
        a[1]+=100
    elif i%4==3:
        a[0]+=100
        a[2]-=100

k=1000000
while True:
    for i in range(3):
        biao[i].resilience(None,k,biao[i+1])
        biao[i+4].resilience(None,k,biao[i+5])
        biao[i].resilience(None,k,biao[i+4])
    biao[3].resilience(None,k,biao[0])
    biao[7].resilience(None,k,biao[4])
    biao[3].resilience(None,k,biao[7])
    biao[0].resilience(None,k,biao[5])
    biao[0].resilience(None,k,biao[7])
    biao[0].resilience(None,k,biao[2])
    biao[1].resilience(None,k,biao[4])
    biao[1].resilience(None,k,biao[6])
    biao[1].resilience(None,k,biao[3])
    biao[2].resilience(None,k,biao[5])
    biao[2].resilience(None,k,biao[7])
    biao[3].resilience(None,k,biao[6])
    biao[3].resilience(None,k,biao[4])
    biao[4].resilience(None,k,biao[6])
    biao[5].resilience(None,k,biao[7])

    for i in biao:
        i.force([-i.v[0]*5,-i.v[1]*5,-i.v[2]*5])

    x=Phy.shijiaoshi(d0.p, [d[0] + d0.p[0], d[1] + d0.p[1], d[2] + d0.p[2]])
    dp.p=[d[0] + d0.p[0], d[1] + d0.p[1], d[2] + d0.p[2]]

    Phy.run(0.001)

    Phy.tplay(x=x, c=d0, k=500)
    turtle.onscreenclick(r)
    turtle.onkeypress(fw, key="w")
    turtle.onkeypress(bw, key="s")
    turtle.onkeypress(le, key="a")
    turtle.onkeypress(ri, key="d")
    turtle.onkeypress(zp, key="q")
    turtle.onkeypress(zn, key="e")

    turtle.onkeypress(cu, key="i")
    turtle.onkeypress(cd, key="k")
    turtle.onkeypress(cl, key="j")
    turtle.onkeypress(cr, key="l")
    turtle.onkeypress(zp2, key="u")
    turtle.onkeypress(zn2, key="o")
    turtle.listen()
    zuobiaoxian(x)

