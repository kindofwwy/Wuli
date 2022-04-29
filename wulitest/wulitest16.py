from wuli import *
import random,turtle

def zuobiaoxian(shunxu,x):
    xian=[Phy.xianxing([100,0,0],x),
          Phy.xianxing([0,100,0],x),
          Phy.xianxing([0,0,100],x)]
    for i in range(len(xian)):
        if i==shunxu:
            turtle.pencolor("red")
        else:
            turtle.pencolor("black")
        turtle.goto(0,0)
        turtle.pd()
        turtle.goto(xian[i][0],xian[i][1])
        turtle.pu()




def r(x,y):
    biao[random.randint(0,7)].force2(10000000,[x,y,0])

def xp():
    x[shunxu][0]+=0.1
def xn():
    x[shunxu][0]-=0.1
def yp():
    x[shunxu][1]+=0.1
def yn():
    x[shunxu][1]-=0.1
def zp():
    x[shunxu][2]+=0.1
def zn():
    x[shunxu][2]-=0.1
def xx():
    global shunxu
    shunxu=0
def yy():
    global shunxu
    shunxu=1
def zz():
    global shunxu
    shunxu=2


x=[[1,0,0],[0,1,0],[0,0,1]]
shunxu=0
    
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
    
    Phy.run(0.001)
    Phy.tplay(x=x)
    turtle.onscreenclick(r)
    turtle.onkeypress(xp, key="d")
    turtle.onkeypress(xn, key="a")
    turtle.onkeypress(yp, key="w")
    turtle.onkeypress(yn, key="s")
    turtle.onkeypress(zp, key="q")
    turtle.onkeypress(zn, key="e")
    turtle.onkeypress(xx, key="x")
    turtle.onkeypress(yy, key="y")
    turtle.onkeypress(zz, key="z")
    turtle.listen()
    zuobiaoxian(shunxu,x)

