from wuli import *

Phy.tready()
a=Phy(5,[0,50,0],[0,0,0],r=5,color="green")
b=DingPhy(1,[0,0,0],[0,-150,0])
f=DingPhy(1,[0,0,0],[0,150,0])
c=Phy.tgraph()
d=Phy.tgraph()
e=Phy.tgraph()

while True:
    a.resilience(100,2,b)
    a.resilience(100,2,f)
    Phy.run(0.06)

    d.draw(None,a.p[1],[-100,0],chang=100,color="green",bi=True,)
    c.draw(None,a.axianshi[1],[-100,0],chang=100,color="red",bi=True)
    e.draw(None,a.v[1],[-100,0],chang=100,color="blue",bi=True)
    Phy.tplay()