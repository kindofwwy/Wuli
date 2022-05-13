from wuli import *
import turtle
def su():
    b.force2(5,[b.v[0]+b.p[0],b.v[1]+b.p[1],b.v[2]+b.p[2]])
def sd():
    b.force2(5,[-b.v[0]+b.p[0],-b.v[1]+b.p[1],-b.v[2]+b.p[2]])

Phy.tready()
g=1
m=10000
r=100
r2=300
a=Phy(m,[0,0,0],[0,0,0],r=30)
b=Phy(1,[0,(g*m/r)**0.5,0],[r,0,0],r=5,color="red")
c=Phy(100,[0,(g*m/r2)**0.5,0],[r2,0,0],r=10)
e=Phy.tgraph()
while True:
    Phy.gravity(g)
    a.bounce(100,b)
    b.bounce(100,c)
    Phy.run(0.1)
    Phy.tplay(v=True,a=True,c=a)
    e.draw(b.p[0],b.p[1],[-a.p[0],-a.p[1]],chang=30,tiao=20,bi=True,color="red")
    turtle.onkeypress(su,"=")
    turtle.onkeypress(sd,"-")
    turtle.listen()

