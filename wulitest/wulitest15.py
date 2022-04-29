from wuli import *
from random import randint
Changjing.tready()
Changjing.camara=[7000,1000,0]
o=[]

def t(c,tc,maxdis,yuan):
    # tc=最后方颜色 c=最前方颜色
    # maxdis=fanwei[2] yuan=dot[2]
    color = (c[0] + (tc[0] - c[0]) / maxdis * yuan,
             c[1] + (tc[1] - c[1]) / maxdis * yuan,
             c[2] + (tc[2] - c[2]) / maxdis * yuan)
    for i in color:
        if i<0:
            return c
        elif i>1:
            return tc
    return color

maxdis=800
fanwei=200000

for i in range(400):
    x=randint(-fanwei,fanwei)
    o.append(object())
    h = (x * 0.01) ** 2 if (x * 0.01) ** 2 < 100000 else randint(50000, 100000)
    h=randint(100,200) if (x * 0.01) ** 2 <100 else h
    d = (x * 0.005) ** 2 if (x * 0.005) ** 2 < 50000 else randint(20000, 50000)
    d=randint(100,200) if (x * 0.005) ** 2 <100 else d
    o[-1].cfang(d,h,
                [x,0,randint(0,maxdis)],
                [0,0,-1])
Changjing.biaoupdate()
while True:
    for i in o:
        i.color=t([0,0,0],[1,1,1],maxdis,i.p[2]-Changjing.camara[2])
        if i.p[2]<=0:
            o.remove(i)
            x = randint(-fanwei, fanwei)
            o.append(object())
            h = (x * 0.01) ** 2 if (x * 0.01) ** 2 < 90000 else randint(25000, 90000)
            h = randint(100, 200) if (x * 0.01) ** 2 < 100 else h
            d = (x * 0.005) ** 2 if (x * 0.005) ** 2 < 50000 else randint(10000, 50000)
            d = randint(100, 200) if (x * 0.005) ** 2 < 100 else d
            o[-1].tri(d, h,
                      [x, 0, maxdis],
                      [0, 0, -1])
    Changjing.biaoupdate()
    Changjing.play(0.5)
    Changjing.keymove()
