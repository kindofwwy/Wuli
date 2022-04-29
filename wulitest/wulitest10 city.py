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
    #tc=最后方颜色 c=最前方颜色
    color=[c[0]+(tc[0]-c[0])/maxdis*yuan,
           c[1]+(tc[1]-c[1])/maxdis*yuan,
           c[2]+(tc[2]-c[2])/maxdis*yuan]
    turtle.goto(p)
    turtle.fillcolor(color[0],color[1],color[2])
    turtle.begin_fill()
    turtle.goto(p[0],p[1]+pingyi)
    turtle.goto(p[0],p[1]+gao+pingyi)
    turtle.goto(p[0]+kuan, p[1] + gao+pingyi)
    turtle.goto(p[0] + kuan, p[1]+pingyi)
    turtle.goto(p[0],p[1]+pingyi)
    turtle.end_fill()
def sun():
    if sd.p[1]<=30:
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
    gcolor = [tcolor[0] / maxdis * 10,
              tcolor[1] / maxdis * 10,
              0.1+(tcolor[2]-0.1) / maxdis * 10]
    turtle.fillcolor(gcolor)
    turtle.goto(-1000, pingyi)
    turtle.begin_fill()
    turtle.goto(1000, pingyi)
    turtle.goto(1000, pingyi-500)
    turtle.goto(-1000, pingyi-500)
    turtle.end_fill()
def sky():
    turtle.fillcolor(tcolor)
    turtle.goto(-1000, pingyi)
    turtle.begin_fill()
    turtle.goto(1000, pingyi)
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

def d():
    global h
    h-=10
def u():
    global h
    h+=10

biao=[]
maxdis=20 #山的层数
c=200 #山的数量
f=1 #镜头缩小系数
h=100 #相机高度
far=-2 #相机远近
kuan1=50#山的最低宽度
kuan=100 #山的最高宽度
gao1=50#山的最低高度
gao=80 #山的最高高度
jun=1.0 #山的高度的均匀程度
k=1#山高度放大系数
fenbu=15000 #山分布宽度
v=25 #山的速度
color=(0.0,0.0,0.03) #山的颜色
tcolor=(1,1,1) #大气颜色
pingyi=-100#上下平移
sd=Phy(1,[0,0.5,0],[0,gao1,0])
for i in range(c+1):
    a=(Phy(1,[v,0,0],[random.randint(-fenbu,fenbu),0,random.randint(0,maxdis)]))
    b=(Shan(view(a.p, [0, h, far], f),random.randint(kuan1, kuan),random.randint(round(gao1**jun*k), round(gao**jun*k)),a.p[2]))
    biao.append(Mix(a,b))

biao.sort(key=lambda x: x.Phy.p[2], reverse=True)
while True:
    sky()
    sun()
    ground()
    turtle.onkeypress(u, key="Up")
    turtle.onkeypress(d, key="Down")
    turtle.listen()
    for i in range(c+1):
        biao[i].Shan.p=view(biao[i].Phy.p, [0, h, far], f)
        if biao[i].Phy.p[0]>=fenbu:
            biao.remove(biao[i])
            a=Phy(1, [v, 0, 0], [-fenbu, 0, random.randint(0,maxdis)])
            b=Shan(view(a.p, [0, h, far], f),random.randint(kuan1, kuan),random.randint(round(gao1**jun*k), round(gao**jun*k)),a.p[2])
            biao.append(Mix(a,b))
            biao.sort(key=lambda x: x.Phy.p[2], reverse=True)
            k += 0.03




        biao[i].Shan.tr()

    ch=gao**jun*k
    h+=2 if h<ch else 0


    Phy.run(0.5)
    turtle.update()
    turtle.clear()

