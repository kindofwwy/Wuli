from wuli import *
import turtle,random

class triangle:
    tbiao=[]
    def __init__(self,p1,p2,p3,color):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.color=color
        triangle.tbiao.append(self)

    light=[0.3,1,0]
    cam=Phy.camera()

    def pointto(self):
        a=[self.p2[0]-self.p1[0],self.p2[1]-self.p1[1],self.p2[2]-self.p1[2]]
        b=[self.p3[0]-self.p1[0],self.p3[1]-self.p1[1],self.p3[2]-self.p1[2]]
        l=[(a[1]*b[2]-b[1]*a[2]),
           -(a[0]*b[2]-b[0]*a[2]),
           (a[0]*b[1]-b[0]*a[1])]
        x=(l[0]**2+l[1]**2+l[2]**2)**0.5
        return [l[0]/x,l[1]/x,l[2]/x]


    def draw(self,fx=True):
        fa=self.pointto()
        xi=fa[0]*triangle.light[0]+fa[1]*triangle.light[1]+fa[2]*triangle.light[2]
        color=[min(1,max(0,self.color[0]*xi)),
               min(1,max(0,self.color[1]*xi)),
               min(1,max(0,self.color[2]*xi))]
        turtle.pu()
        turtle.fillcolor(color)
        p1=triangle.cam.cdotpos(self.p1)
        p2=triangle.cam.cdotpos(self.p2)
        p3=triangle.cam.cdotpos(self.p3)
        if p1 is None or p2 is None or p3 is None:
            return
        turtle.goto(p1)
        turtle.begin_fill()
        turtle.goto(p2)
        turtle.goto(p3)
        turtle.goto(p1)
        turtle.end_fill()

        if fx:
            f0=triangle.cam.cdotpos(self.centre())
            f1=triangle.cam.cdotpos([self.centre()[0]+fa[0]*100,
                                     self.centre()[1]+fa[1]*100,
                                     self.centre()[2]+fa[2]*100])
            if f0 is None or f1 is None:
                return
            turtle.goto(f0)
            turtle.pd()
            turtle.goto(f1)
            turtle.pu()

    def centre(self):
        return [(self.p1[0]+self.p2[0]+self.p3[0])/3,
                (self.p1[1]+self.p2[1]+self.p3[1])/3,
                (self.p1[2]+self.p2[2]+self.p3[2])/3,]

    @classmethod
    def drawall(cls):
        triangle.tbiao.sort(key=lambda x:triangle.cam.dotposspace(x.centre())[2],reverse=True)
        for i in triangle.tbiao:
            i.draw()


diannum=12  #顶点数量
sannum=6    #三角形数量
c=[1,1,0]
pl2=[[random.randint(-100,100) for i in range(3)] for j in range(diannum)]
t=[random.sample(pl2,3) for k in range(sannum)]
tb2=[triangle(m[0],m[1],m[2],c) for m in t]

buchang=0.02
def l():
   triangle.light[0]+=buchang
def r():
    triangle.light[0]-=buchang
def u():
    triangle.light[2]+=buchang
def d():
    triangle.light[2]-=buchang
def f():
    triangle.light[1]+=buchang
def b():
    triangle.light[1]-=buchang

def drawlight():
    beg=[0,200,0]
    l0=triangle.cam.cdotpos(beg)
    l1=triangle.cam.cdotpos([beg[0]+triangle.light[0]*100,
                             beg[1]+triangle.light[1]*100,
                             beg[2]+triangle.light[2]*100])
    if l0 is None or l1 is None:
        return
    turtle.goto(l0)
    turtle.pd()
    turtle.goto(l1)
    turtle.pu()

Phy.tready()
while True:
    triangle.drawall()
    drawlight()
    turtle.update()
    turtle.clear()
    turtle.onkeypress(u, key="i")
    turtle.onkeypress(d, key="k")
    turtle.onkeypress(l, key="j")
    turtle.onkeypress(r, key="l")
    turtle.onkeypress(f, key="=")
    turtle.onkeypress(b, key="-")
    triangle.cam.movecam(stepsize=5)