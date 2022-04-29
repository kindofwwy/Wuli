from wuli import *
import random,turtle
def r(x,y):
    biao[random.randint(0,7)].force2(10000000,[x,y,0])
    
Phy.tready()
f=3000000
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
'''
biao[1].force([0,f,0])
biao[5].force([0,f,0])
biao[3].force([0,-f,0])
biao[7].force([0,-f,0])

biao[1].force([0,f,0])
biao[2].force([0,f,0])
biao[7].force([0,-f,0])
biao[4].force([0,-f,0])
'''

while True:
    for i in range(3):
        biao[i].resilience(100,1000000,biao[i+1])
        biao[i+4].resilience(100,1000000,biao[i+5])
        biao[i].resilience(100,1000000,biao[i+4])
    biao[3].resilience(100,1000000,biao[0])
    biao[7].resilience(100,1000000,biao[4])
    biao[3].resilience(100,1000000,biao[7])

    biao[0].resilience(141.42135,1000000,biao[5])
    biao[0].resilience(141.42135,1000000,biao[7])
    biao[0].resilience(141.42135,1000000,biao[2])
    biao[1].resilience(141.42135,1000000,biao[4])
    biao[1].resilience(141.42135,1000000,biao[6])
    biao[1].resilience(141.42135,1000000,biao[3])
    biao[2].resilience(141.42135,1000000,biao[5])
    biao[2].resilience(141.42135,1000000,biao[7])
    biao[3].resilience(141.42135,1000000,biao[6])
    biao[3].resilience(141.42135,1000000,biao[4])
    biao[4].resilience(141.42135,1000000,biao[6])
    biao[5].resilience(141.42135,1000000,biao[7])

    for i in biao:
        i.force([-i.v[0]*5,-i.v[1]*5,-i.v[2]*5])
    
    Phy.run(0.001)
    Phy.tplay()
    turtle.onscreenclick(r)
