from wuli import *
import turtle
Phy.tready()
def o(a):
    return (a[0]**2+a[1]**2+a[2]**2)**0.5
def z(x,y):
    global onc
    if onc==True:
        onc= False
    else:
        onc=True
a=Phy(1,[20,0,0],[0,-100,0],5,color="red")
b=Phy(1,[10,0,0],[0,-50,0],5,color="blue")
c=Phy(1,[0,0,0],[0,0,0],5)
onc=True
while True:
    turtle.onscreenclick(z)
    if onc:
        a.force2(a.m*(o(a.v)/o(a.p))**2*o(a.p),[0,0,0])
    b.force2(b.m*(o(b.v)/o(b.p))**2*o(b.p),[0,0,0])
    c.resilience(0,0,b)
    b.resilience(0,0,a)
    Phy.run(0.005)
    Phy.tplay(v=True,a=True,c=b)
