#PIDtest P=red I=green D=blue
from wuli import *
import turtle

def rey(x,y):
    global y1,b,c,d
    y1=y
    b.clean()
    c.clean()
    d.clean()

Phy.tready()
t=0.05
y1=0
lei=0
a=Phy(10,[0,0,0],[0,0,0],r=10)
k1=0.5
k2=-2
k3=0.0008
b=Phy.tgraph()
c=Phy.tgraph()
d=Phy.tgraph()
while True:

    cha=y1-a.p[1]
    v=a.v[1]
    lei+=cha
    print(lei*k3)
    a.force([0,k1*cha +k2*v +k3*lei,0])

    a.force([0,-10,0])
    Phy.run(t)
    Phy.tplay()
    turtle.onscreenclick(rey)
    turtle.goto(0,y1)
    turtle.dot(30,"red")
    b.draw(None,k1*cha,[100,0],color="red",tiao=80,kx=10,ky=3,bi=True,chang=50)
    c.draw(None, k2*v, [100, 0], color="blue", tiao=80, kx=10,ky=3, bi=True,chang=50)
    d.draw(None, k3*lei, [100, 0], color="green", tiao=80, kx=10,ky=3, bi=True,chang=50)
    turtle.listen()