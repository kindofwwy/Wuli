from wuli import *
import random

Changjing.tready()
Changjing.k=1
a=[]
for i in range(100):
    a.append(object())
    a[-1].fang(random.randint(500,800),
               [random.randint(-10000,10000),
                random.randint(-10000,10000),
                random.randint(0,200)],
               [0,0,-2],
               color=(random.randint(0,10)/10,random.randint(0,10)/10,random.randint(0,10)/10))
    Changjing.biaoupdate()
while True:
    Changjing.play(0.05)
    for i in a:
        if i.p[2]<=0:
            a.remove(i)
            a.append(object())
            a[-1].fang(random.randint(500, 800),
                       [random.randint(-10000, 10000), random.randint(-10000, 10000), 200],
                       [0, 0, -2],color=(random.randint(0,10)/10,random.randint(0,10)/10,random.randint(0,10)/10))
    Changjing.biaoupdate()
    Changjing.keymove()
    
