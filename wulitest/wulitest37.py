from wuli import *
import random,turtle
biao=[]
xrange=(-500,500)
yrange=(-500,500)
zrange=(-300,5000)
vrange=(0,0)
mrange=(10,50)
rrange=(5,20)
star_num=20
for i in range(star_num):
    m = random.uniform(mrange[0], mrange[1])
    v = [random.uniform(vrange[0], vrange[1]),
         random.uniform(vrange[0], vrange[1]),
         random.uniform(vrange[0], vrange[1])]
    p = [random.uniform(xrange[0], xrange[1]),
         random.uniform(yrange[0], yrange[1]),
         random.uniform(zrange[0], zrange[1])]
    c=(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    r=random.uniform(rrange[0],rrange[1])
    biao.append(Phy(m,v,p,r,c))
    biao.append(Phy(m,[-v[1],v[0],v[2]],[-p[1],p[0],p[2]],r,c))
    biao.append(Phy(m,[-v[0],-v[1],v[2]],[-p[0],-p[1],p[2]],r,c))
    biao.append(Phy(m,[v[1],-v[0],v[2]],[p[1],-p[0],p[2]],r,c))

c=Phy.camera()
Phy.tready()
turtle.bgcolor("black")
while True:
    Phy.gravity(10)
    Phy.run(0.1)
    c.tplay()
    c.movecam(stepsize=5)


