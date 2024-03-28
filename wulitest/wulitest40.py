from wuli import *

def dis(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5

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
        a=[self.p2.p[0]-self.p1.p[0],self.p2.p[1]-self.p1.p[1],self.p2.p[2]-self.p1.p[2]]
        b=[self.p3.p[0]-self.p1.p[0],self.p3.p[1]-self.p1.p[1],self.p3.p[2]-self.p1.p[2]]
        l=[(a[1]*b[2]-b[1]*a[2]),
           -(a[0]*b[2]-b[0]*a[2]),
           (a[0]*b[1]-b[0]*a[1])]
        if l[0]*triangle.light[0]+l[1]*triangle.light[1]+l[2]*triangle.light[2]<0:
            l=[-l[0],-l[1],-l[2]]
        x=(l[0]**2+l[1]**2+l[2]**2)**0.5
        return [l[0]/x,l[1]/x,l[2]/x]


    def draw(self,fx=False):
        fa=self.pointto()
        xi=fa[0]*triangle.light[0]+fa[1]*triangle.light[1]+fa[2]*triangle.light[2]
        color=[min(1,max(0,self.color[0]*xi)),
               min(1,max(0,self.color[1]*xi)),
               min(1,max(0,self.color[2]*xi))]
        turtle.pu()
        turtle.fillcolor(color)
        p1=triangle.cam.cdotpos(self.p1.p)
        p2=triangle.cam.cdotpos(self.p2.p)
        p3=triangle.cam.cdotpos(self.p3.p)
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
        return [(self.p1.p[0]+self.p2.p[0]+self.p3.p[0])/3,
                (self.p1.p[1]+self.p2.p[1]+self.p3.p[1])/3,
                (self.p1.p[2]+self.p2.p[2]+self.p3.p[2])/3,]

    @classmethod
    def drawall(cls):
        triangle.tbiao.sort(key=lambda x:triangle.cam.dotposspace(x.centre())[2],reverse=True)
        for i in triangle.tbiao:
            i.draw()

class wing:
    wingbiao=[]
    wrbiao=[]
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        wing.wingbiao.append(self)
        rbiao=[[self.p1,self.p2],
               [self.p1,self.p3],
               [self.p2,self.p3],]
        for i in rbiao:
            if i in wing.wrbiao or i.reverse() in wing.wrbiao:
                continue
            wing.wrbiao.append(i)

    def windspeed(self):
        return [-(self.p1.v[0]+self.p2.v[0]+self.p3.v[0])/3,
                -(self.p1.v[1]+self.p2.v[1]+self.p3.v[1])/3,
                -(self.p1.v[2]+self.p2.v[2]+self.p3.v[2])/3]

    def pointto(self):
        a=[self.p2.p[0]-self.p1.p[0],self.p2.p[1]-self.p1.p[1],self.p2.p[2]-self.p1.p[2]]
        b=[self.p3.p[0]-self.p1.p[0],self.p3.p[1]-self.p1.p[1],self.p3.p[2]-self.p1.p[2]]
        l=[(a[1]*b[2]-b[1]*a[2]),
           -(a[0]*b[2]-b[0]*a[2]),
           (a[0]*b[1]-b[0]*a[1])]
        x=(l[0]**2+l[1]**2+l[2]**2)**0.5
        return l

    def fly(self,airk=1.0,drgk=1.0):
        zhu=self.pointto()
        wind=self.windspeed()
        if wind==[0,0,0]:
            return
        winds=(wind[0]**2+wind[1]**2+wind[2]**2)**0.5
        lift=(zhu[0]*wind[0]+zhu[1]*wind[1]+zhu[2]*wind[2])*winds*airk
        drag=abs(zhu[0]*wind[0]+zhu[1]*wind[1]+zhu[2]*wind[2])*winds*drgk
        self.p1.force2(lift, [self.p1.p[0] + zhu[0],
                              self.p1.p[1] + zhu[1],
                              self.p1.p[2] + zhu[2]])
        self.p2.force2(lift, [self.p2.p[0] + zhu[0],
                              self.p2.p[1] + zhu[1],
                              self.p2.p[2] + zhu[2]])
        self.p3.force2(lift, [self.p3.p[0] + zhu[0],
                              self.p3.p[1] + zhu[1],
                              self.p3.p[2] + zhu[2]])
        self.p1.force2(drag, [self.p1.p[0] + wind[0],
                              self.p1.p[1] + wind[1],
                              self.p1.p[2] + wind[2]])
        self.p2.force2(drag, [self.p2.p[0] + wind[0],
                              self.p2.p[1] + wind[1],
                              self.p2.p[2] + wind[2]])
        self.p3.force2(drag, [self.p3.p[0] + wind[0],
                              self.p3.p[1] + wind[1],
                              self.p3.p[2] + wind[2]])

    def wing2tri(self,color):
        return triangle(self.p1,self.p2,self.p3,color)

    @classmethod
    def flyall(cls,airk=1.0,drgk=1.0):
        for i in wing.wingbiao:
            i.fly(airk,drgk)

    @classmethod
    def strengthen(cls,k=1000):
        for i in wing.wrbiao:
            i[0].resilience(other=i[1],k=k)

class plane:
    def __init__(self,pos,l=250,h=50,r=60,k=10,c=None):
        '''

        :param pos: 机头坐标
        :param l: 机身长
        :param h: 机身高
        :param r: 翼展
        :param k: 翼根-中线距离
        :param c: color
        '''
        if c is None:
            c=[0.7,0.7,0.7]
        self.plist=[Phy(5,[0,0,0],pos),
                    Phy(1,[0,0,0],[pos[0]+k,pos[1],pos[2]-l]),
                    Phy(1,[0,0,0],[pos[0]+k+r,pos[1],pos[2]-l]),
                    Phy(1,[0,0,0],[pos[0],pos[1]-h,pos[2]-l]),
                    Phy(1,[0,0,0],[-(pos[0]+k),pos[1],pos[2]-l]),
                    Phy(1,[0,0,0],[-(pos[0]+k+r),pos[1],pos[2]-l])]
        self.tlist=[triangle(self.plist[0],self.plist[1],self.plist[2],c),  #主翼
                    triangle(self.plist[0],self.plist[1],self.plist[3],c),
                    triangle(self.plist[0],self.plist[4],self.plist[3],c),
                    triangle(self.plist[0],self.plist[4],self.plist[5],c)]  #主翼
        self.wlist=[wing(self.plist[0],self.plist[1],self.plist[2]),
                    wing(self.plist[0],self.plist[4],self.plist[5])]

    def doforce(self,airk=1.0,drgk=1.0,enk=0.1):
        for i in self.wlist:
            i.fly(airk,drgk)
        self.plist[0].a=[self.plist[0].a[0]/4,self.plist[0].a[1]/4,self.plist[0].a[2]/4]
        for i in self.plist[1:]:
            self.plist[0].resilience(k=1000,other=i)
        self.plist[1].resilience(k=1000, other=self.plist[2])
        self.plist[1].resilience(k=1000, other=self.plist[3])
        self.plist[4].resilience(k=1000, other=self.plist[3])
        self.plist[4].resilience(k=1000, other=self.plist[5])
        self.plist[3].resilience(k=1000, other=self.plist[2])
        self.plist[3].resilience(k=1000, other=self.plist[5])
        self.plist[4].resilience(k=1000, other=self.plist[1])

        f = [-((self.plist[1].p[0] + self.plist[4].p[0]) / 2 - self.plist[0].p[0])*enk,
             -((self.plist[1].p[1] + self.plist[4].p[1]) / 2 - self.plist[0].p[1])*enk,
             -((self.plist[1].p[2] + self.plist[4].p[2]) / 2 - self.plist[0].p[2])*enk]
        for i in self.plist:
            i.force(f)

class plane2:
    def __init__(self,pos,l1,l2,l3,l4,h,w1,w2,wh,f1,f2,c=None):
        if c is None:
            c=[0.7,0.7,0.7]
        self.plist=[Phy(2,[0,0,0],pos),
                    Phy(2,[0,0,0],[pos[0],pos[1],pos[2]-l1]),
                    Phy(2,[0,0,0],[pos[0],pos[1]+h,pos[2]-l1]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2]),
                    Phy(1,[0,0,0],[pos[0],pos[1]+h,pos[2]-l1-l2]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2-l3]),
                    Phy(1,[0,0,0],[pos[0],pos[1]+h,pos[2]-l1-l2-l3]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2-l3-l4]),
                    Phy(1,[0,0,0],[pos[0]-w1,pos[1],pos[2]-l1-l2]),
                    Phy(1,[0,0,0],[pos[0]+w1,pos[1],pos[2]-l1-l2]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2-f1]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2-f1]),
                    Phy(1,[0,0,0],[pos[0]-w2,pos[1],pos[2]-l1-l2-l3-l4]),
                    Phy(1,[0,0,0],[pos[0]+w2,pos[1],pos[2]-l1-l2-l3-l4]),
                    Phy(1,[0,0,0],[pos[0],pos[1]+wh,pos[2]-l1-l2-l3-l4]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2-l3-l4-f2]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2-l3-l4-f2]),
                    Phy(1,[0,0,0],[pos[0],pos[1],pos[2]-l1-l2-l3-l4-f2])]
        self.wlist=[wing(self.plist[0],self.plist[1],self.plist[2]),
                    wing(self.plist[1],self.plist[2],self.plist[3]),
                    wing(self.plist[1],self.plist[3],self.plist[4]),
                    wing(self.plist[3],self.plist[4],self.plist[5]),
                    wing(self.plist[3],self.plist[5],self.plist[6]),
                    wing(self.plist[5],self.plist[6],self.plist[7]),    #到此为机身
                    wing(self.plist[5],self.plist[7],self.plist[14]),   #垂直尾翼
                    wing(self.plist[1],self.plist[3],self.plist[8]),
                    wing(self.plist[1],self.plist[3],self.plist[9]),    #到此为主翼
                    wing(self.plist[3],self.plist[8],self.plist[10]),
                    wing(self.plist[3],self.plist[9],self.plist[11]),   #到此为襟翼
                    wing(self.plist[5],self.plist[7],self.plist[12]),
                    wing(self.plist[5],self.plist[7],self.plist[13]),   #到此为水平尾翼
                    wing(self.plist[7],self.plist[12],self.plist[15]),
                    wing(self.plist[7],self.plist[13],self.plist[16]),  #到此为平尾活动翼面
                    wing(self.plist[7],self.plist[14],self.plist[17])]  #垂尾活动翼面
        self.tlist=[i.wing2tri(c) for i in self.wlist]
        self.clist=[dis(self.plist[4].p,self.plist[10].p),
                    dis(self.plist[4].p,self.plist[11].p),
                    dis(self.plist[14].p,self.plist[15].p),
                    dis(self.plist[14].p,self.plist[16].p),
                    dis(self.plist[12].p,self.plist[17].p)]

    def doforce(self, airk=1.0, drgk=1.0, enk=0.1):
        wing.strengthen()
        self.plist[2].resilience(other=self.plist[4],k=1000)
        self.plist[4].resilience(other=self.plist[6], k=1000)
        self.plist[6].resilience(other=self.plist[14], k=1000)
        self.plist[4].resilience(other=self.plist[8], k=1000)
        self.plist[4].resilience(other=self.plist[9], k=1000)
        self.plist[14].resilience(other=self.plist[12], k=1000)
        self.plist[14].resilience(other=self.plist[13], k=1000)
        self.plist[0].resilience(other=self.plist[8], k=1000)
        self.plist[0].resilience(other=self.plist[9], k=1000)
        self.plist[5].resilience(other=self.plist[8], k=1000)
        self.plist[5].resilience(other=self.plist[9], k=1000)
        self.plist[3].resilience(other=self.plist[12], k=1000)
        self.plist[3].resilience(other=self.plist[13], k=1000)
        self.plist[8].resilience(other=self.plist[12], k=1000)
        self.plist[9].resilience(other=self.plist[13], k=1000)


        self.plist[4].resilience(x=self.clist[0], other=self.plist[10], k=1000)
        self.plist[4].resilience(x=self.clist[1], other=self.plist[11], k=1000)
        self.plist[14].resilience(x=self.clist[2], other=self.plist[15], k=1000)
        self.plist[14].resilience(x=self.clist[3], other=self.plist[16], k=1000)
        self.plist[12].resilience(x=self.clist[4], other=self.plist[17], k=1000)

        for i in self.wlist:
            i.fly(airk,drgk)
        f=[(self.plist[0].p[0]-self.plist[7].p[0])*enk,
           (self.plist[0].p[1]-self.plist[7].p[1])*enk,
           (self.plist[0].p[2]-self.plist[7].p[2])*enk]
        for i in self.plist:
            i.force(f)

def control(plane,k=1):
    def u():
        plane.plist[0].v[1]+=k
    def d():
        plane.plist[0].v[1]-=k
    def l():
        plane.plist[0].v[0]-=k
    def r():
        plane.plist[0].v[0]+=k
    turtle.onkeypress(u,"i")
    turtle.onkeypress(d,"k")
    turtle.onkeypress(l,"j")
    turtle.onkeypress(r,"l")

def control2(a2,k=0.2):
    def pitchu():
        a2.clist[2]+=-k
        a2.clist[3]+=-k
    def pitchd():
        a2.clist[2]+=k
        a2.clist[3]+=k
    def yawpl():
        a2.clist[4]+=-k
    def yawpr():
        a2.clist[4]+=k
    def rolll():
        a2.clist[0]+=-k
        a2.clist[1]+=k
    def rollr():
        a2.clist[0]+=k
        a2.clist[1]+=-k
    turtle.onkeypress(pitchu,"k")
    turtle.onkeypress(pitchd,"i")
    turtle.onkeypress(yawpl,"j")
    turtle.onkeypress(yawpr, "l")
    turtle.onkeypress(rolll, "u")
    turtle.onkeypress(rollr, "o")


Phy.tready()
# a=plane([0,0,100])
# for i in a.plist:
#     i.v=[0,0,0.01]

a=plane2([0,0,300],100,100,200,50,50,200,100,100,25,50)
b=0.1
while True:
    a.doforce(airk=0.0002,drgk=0.0001,enk=0.2)
    for i in a.plist:
        i.force([0,-8*i.m,0])
        if i.v==[0,0,0]:
            continue
        i.force2(i.v[0]**2*b+i.v[1]**2*b+i.v[2]**2*b,[i.p[0]-i.v[0],
                                                      i.p[1]-i.v[1],
                                                      i.p[2]-i.v[2]])
    Phy.run(0.01)
    print(f"v={(a.plist[0].v[0]**2+a.plist[0].v[1]**2+a.plist[0].v[2]**2)**0.5},h={a.plist[0].p[1]}")
    triangle.drawall()
    #triangle.cam.tplay()
    turtle.update()
    turtle.clear()
    #triangle.cam.setlookpos(a.plist[0].p)
    triangle.cam.movecam(stepsize=20)
    control2(a)
    # control(a)