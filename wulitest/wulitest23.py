from wuli import *
import turtle,random
Phy.tready()
a=Phy(1,[0,0,0],[0,0,0],5)

g=50
zhen=0.002
p=[0,0]
xbiao=[]
def d(p):
    turtle.goto(p[0],p[1])
    turtle.dot(2*a.r,"red")
def m(x,y):
    global g,a,zhen,p
    xx=x-a.p[0]
    yy=y-a.p[1]
    t=(xx**2+yy**2)**0.5*0.01
    vx=xx/t
    vy=yy/t+0.5*g*t
    print(f"vx:{vx:.2f},vy:{vy:.2f}")
    ax=(vx-a.v[0])/zhen*a.m
    ay=(vy-a.v[1])/zhen*a.m
    a.force([ax,ay,0])
    p=[x,y]
while True:
    if Phy.zhenshu % 70 == 0:
        xbiao.append(tuple(a.p))
    if len(xbiao)>10:
        xbiao.pop(0)
    for i in xbiao:
        turtle.goto(i[0], i[1])
        turtle.dot(a.r)
    if [round(a.p[0]),round(a.p[1])]==p:
        p=[random.randint(-300,300),random.randint(-300,300)]
        m(p[0],p[1])

    d(p)
    a.force([0,-g,0])
    turtle.onscreenclick(m)

    Phy.hprun(zhen)
    Phy.tplay(fps=5)


