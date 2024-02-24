from wuli import *
import random
biao=[]
xrange=(-500,500)
yrange=(-500,500)
zrange=(-500,500)
vrange=(0,0)
mrange=(10,50)
star_num=50    # 生成多少颗星
for i in range(star_num):
    biao.append(Phy(m=random.uniform(mrange[0],mrange[1]),
                    v=[random.uniform(vrange[0],vrange[1]),
                       random.uniform(vrange[0],vrange[1]),
                       random.uniform(vrange[0],vrange[1])],
                    p=[random.uniform(xrange[0],xrange[1]),
                       random.uniform(yrange[0],yrange[1]),
                       random.uniform(zrange[0],zrange[1])]
                    ))

c=Phy.camera()
Phy.tready()
while True:
    Phy.gravity(10)
    Phy.run(0.01)
    c.tplay(zuobiaoxian=True,v=True)
    c.movecam()


