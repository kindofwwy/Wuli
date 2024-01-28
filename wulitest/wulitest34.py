from wuli import *
import random,turtle

staramount=3        #行星数量
drawfreq=20         #绘制跳过帧数
tiao=3              #轨迹绘制精度（越小越精细）
chang=1000          #轨迹最大长度
orbrange=(10,300)   #行星轨道半径范围
rrange=(3,10)       #行星半径范围


class Star:

    center=Phy(1000,[0,0,0],[0,0,0],color="white")
    centertrack=Phy.tgraph()
    starlist=[]
    zhen=0

    def __init__(self,orb,r,color):
        self.star=Phy(1,[0,(Star.center.m/orb)**0.5,0],[orb,0,0],r,color)
        self.track=Phy.tgraph()
        self.color=color
        Star.starlist.append(self)

    @classmethod
    def drawtrack(cls,c,chang=1000,drawfreq=20,tiao=10):
        if Star.zhen%drawfreq==0:
            Star.centertrack.draw(Star.center.p[0]-c.p[0],Star.center.p[1]-c.p[1],[0,0],chang,tiao=tiao,color=Star.center.color,bi=True)
            for i in Star.starlist:
                i.track.draw(i.star.p[0]-c.p[0],i.star.p[1]-c.p[1],[0,0],chang,tiao=tiao,color=i.color,bi=True)
        elif Star.zhen%tiao==0:
            Star.centertrack.biao.append([Star.center.p[0]-c.p[0],Star.center.p[1]-c.p[1]])
            for i in Star.starlist:
                i.track.biao.append([i.star.p[0]-c.p[0],i.star.p[1]-c.p[1]])
        Star.zhen+=1

    @classmethod
    def cleantrack(cls):
        Star.centertrack.clean()
        for i in Star.starlist:
            i.track.clean()

Phy.tready()
turtle.bgcolor("black")
l=[Star(orb=random.randint(orbrange[0],orbrange[1]),r=random.randint(rrange[0],rrange[1]),
        color=(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
        for i in range(staramount)]

pos=0
c=Phy.biao[pos%len(Phy.biao)]
def changeinc():
    global pos,c
    pos+=1
    c=Phy.biao[pos%len(Phy.biao)]
    Star.cleantrack()
def changedec():
    global pos,c
    if pos<=0:
        return
    pos-=1
    c=Phy.biao[pos%len(Phy.biao)]
    Star.cleantrack()

while True:
    turtle.onkeypress(changeinc,key="Right")
    turtle.onkeypress(changedec,key="Left")
    turtle.listen()
    Phy.gravity(1)
    Phy.run(0.5)
    Star.drawtrack(c=c,drawfreq=drawfreq,tiao=tiao,chang=chang)
    Phy.tplay(c=c,fps=drawfreq)