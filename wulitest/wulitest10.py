from wuli import *
import random,turtle
turtle.tracer(0)
turtle.penup()
turtle.hideturtle()
screen = turtle.Screen()

def view(p,camara,k):
    viewlength=(camara[2]-p[2])*k
    dx = (camara[0] - p[0]) / viewlength
    dy = (camara[1] - p[1]) / viewlength
    return (dx,dy)
def t(p,kuan,gao,yuan,tc,c): #yuan(0,10)
    #color=(0.1,0.5,0.1)
    color=[c[0]+(tc[0]-c[0])/maxdis*yuan,
           c[1]+(tc[1]-c[1])/maxdis*yuan,
           c[2]+(tc[2]-c[2])/maxdis*yuan]
    turtle.goto(p)
    turtle.fillcolor(color[0],color[1],color[2])
    turtle.begin_fill()
    turtle.goto(p[0]+kuan/2,p[1])
    turtle.goto(p[0],p[1]+gao)
    turtle.goto(p[0]-kuan/2,p[1])
    turtle.goto(p)
    turtle.end_fill()
def sun():
    if sd.p[1]<=0:
        sd.v[1]=0.5
    elif sd.p[1] >= 500:
        sd.v[1] = -0.5
    global tcolor
    tcolor=[(sd.p[1]/500)**0.4,(sd.p[1]/500)**0.7,sd.p[1]/500]
    turtle.goto(sd.p[0],sd.p[1])
    turtle.fillcolor((1,(sd.p[1]/500)**0.8,sd.p[1]/500))
    turtle.begin_fill()
    turtle.circle(-50)
    turtle.end_fill()


def ground():
    turtle.fillcolor("#58924d")
    turtle.goto(-1000, 0)
    turtle.begin_fill()
    turtle.goto(1000, 0)
    turtle.goto(1000, -500)
    turtle.goto(-1000, -500)
    turtle.end_fill()
def sky():
    turtle.fillcolor(tcolor)
    turtle.goto(-1000, 0)
    turtle.begin_fill()
    turtle.goto(1000, 0)
    turtle.goto(1000, 500)
    turtle.goto(-1000, 500)
    turtle.end_fill()
class Shan:
    def __init__(self,p,kuan,gao,yuan):
        self.p=p
        self.kuan=kuan
        self.gao=gao
        self.yuan=yuan
    def tr(self):
        t(self.p,self.kuan,self.gao,self.yuan,tcolor,color)

class Mix:
    def __init__(self,Phy,Shan):
        self.Shan=Shan
        self.Phy=Phy

biao=[]
maxdis=20 #山的层数
c=200 #山的数量
f=1 #镜头缩小系数
h=500 #相机高度
far=-2 #相机远近
kuan=250 #山的宽度
gao=300 #山的高度
fenbu=13000 #山分布宽度
color=(0.13,0.54,0.13) #山的颜色
tcolor=(1,1,1) #大气颜色
sd=Phy(1,[0,0.5,0],[0,0,0])
for i in range(c+1):
    a=(Phy(1,[10,0,0],[random.randint(-fenbu,fenbu),0,random.randint(0,maxdis)]))
    b=(Shan(view(a.p, [0, h, far], f),random.randint(100, kuan),random.randint(50, gao),a.p[2]))
    biao.append(Mix(a,b))

biao.sort(key=lambda x: x.Phy.p[2], reverse=True)
while True:
    sky()
    sun()
    ground()

    for i in range(c+1):
        biao[i].Shan.p=view(biao[i].Phy.p, [0, h, far], f)
        if biao[i].Phy.p[0]>=fenbu:
            biao.remove(biao[i])
            a=Phy(1, [10, 0, 0], [-fenbu, 0, random.randint(0,maxdis)])
            b=Shan(view(a.p, [0, h, far], f),random.randint(100, kuan),random.randint(50, gao),a.p[2])
            biao.append(Mix(a,b))
            biao.sort(key=lambda x: x.Phy.p[2], reverse=True)




        biao[i].Shan.tr()
    Phy.run(0.5)

    turtle.update()
    turtle.clear()

