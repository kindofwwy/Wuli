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

def xp():
    d[0]+=0.1
def xn():
    d[0]-=0.1
def yp():
    d[1]+=0.1
def yn():
    d[1]-=0.1


d=[0,0,10]

    
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

    x=Phy.shijiaoshi([0,0,0],d)

    Phy.run(0.001)
    Phy.tplay(x=x)
    turtle.onscreenclick(r)
    turtle.onkeypress(xp, key="d")
    turtle.onkeypress(xn, key="a")
    turtle.onkeypress(yp, key="w")
    turtle.onkeypress(yn, key="s")
    turtle.listen()
    zuobiaoxian(x)

