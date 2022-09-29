from wuli import *
import turtle
def su():
    b.force2(5,[b.v[0]+b.p[0],b.v[1]+b.p[1],b.v[2]+b.p[2]])
def sd():
    b.force2(5,[-b.v[0]+b.p[0],-b.v[1]+b.p[1],-b.v[2]+b.p[2]])
    print("a")
def zz():
    global w
    w=0
Phy.tready()
g=1
m=10000
r=100
r2=400
a=Phy(m,[0,0,0],[0,0,0],r=30)
b=Phy(1,[0,(g*m/r)**0.5,0],[r,0,0],r=5,color="red")
e=Phy.tgraph()
w=0
#x=0
t=0.1
while True:
    Phy.gravity(g)
    a.bounce(100,b)
    Phy.run(t)
    Phy.tplay(v=True,a=True,c=a)
    e.draw(b.p[0],b.p[1],[-a.p[0],-a.p[1]],chang=30,tiao=20,bi=True,color="red")
    turtle.onkeypress(su,"=")
    turtle.onkeypress(sd,"-")
    turtle.onkey(zz," ")
    turtle.listen()
    w+=(b.v[0]*t*b.axianshi[0]+b.v[1]*t*b.axianshi[1])
    #x+=((b.v[0]*t)**2+(b.v[1]*t)**2)**0.5
    print(w)
    #print("x",x)


