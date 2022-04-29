from wuli import *
Phy.tready()
a=Phy(5,[0,0,0],[50,50,0])
b=Phy(5,[0,0,0],[-50,50,0])
c=Phy(5,[0,0,0],[-50,-50,0])
d=Phy(5,[0,0,0],[50,-50,0])
a.force([6000000,0,0])
d.force([6000000,0,0])
while True:
    if a.p[0]>900:
        a.p[0]-=2000
        b.p[0] -= 2000
        c.p[0] -= 2000
        d.p[0] -= 2000
    a.resilience(100,100000,b)
    b.resilience(100,100000,c)
    c.resilience(100, 100000, d)
    d.resilience(100, 100000, a)
    a.resilience(141,100000,c)
    Phy.run(0.001)
    Phy.tplay()
