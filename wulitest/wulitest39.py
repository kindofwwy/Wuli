from wuli import *

buchang=20
r=5
a=Phy(100,[0,0,0],[0,0,0],r=80)
b=[]
for z in range(-r,r+1):
    b.append([])
    for x in range(-r, r+1):
        b[-1].append(Phy(1, [0, 0, 0], [x * buchang, 90, z * buchang], r=2 ,color="red"))



c=Phy.camera()
Phy.tready()
while True:
    for z in range(0,2*r+1):
        for x in range(0,2*r+1):
            if x <2*r:
                b[z][x].resilience(k=1000,other=b[z][x+1])
            if z <2*r:
                b[z][x].resilience(k=1000,other=b[z+1][x])
            b[z][x].bounce(1000)
            b[z][x].force([0,-10,0])

    a.a=[0,0,0]
    Phy.run(0.02)
    Phy.biao.sort(key=lambda x:c.dotposspace(x.p)[2],reverse=True)
    c.tplay()
    c.movecam(stepsize=10)


