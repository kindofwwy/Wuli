class Phy:
    '''
    逻辑：创建点→以下循环→计算力→计算加速度→计算速度→计算位置
    '''

    def __init__(self, m, v, p, r=None, color="black", e=0):
        '''
        创建一个点
        :param m: float 质量大小，取正数
        :param v: list[x,y,z] x,y,z为float 速度，矢量
        :param p: list[x,y,z] x,y,z为float 位置
        :param color: str or tuple(r,g,b) 点的颜色
        :param r: float 点的半径
        :param e: float 电荷
        a: list[x,y,z] 加速度，矢量
        '''
        self.m = m
        self.v = v
        self.p = p
        self.a = [0, 0, 0]
        if r is None:
            r = m ** 0.3
        self.r = r
        self.axianshi = self.a
        self.color = color
        self.e=e
        Phy.biao.append(self)

    biao = []  # 这个表里记录了所有被创建的点，计算时会遍历它

    def __str__(self):
        return f"m={self.m},v={self.v},p={self.p},a={self.axianshi}"

    def force(self, li):
        '''
        对某点施力
        :param li: list[x,y,z] x,y,z为float 力，矢量
        :return: None 直接修改a，无返回
        '''
        self.a[0] += li[0] / self.m
        self.a[1] += li[1] / self.m
        self.a[2] += li[2] / self.m

    def force2(self, lisize, p):
        '''
        对某点施力，不同的是，这里只需要提供力的大小和对象位置
        :param lisize: float 力的大小
        :param p: list[x,y,z] 力的方向
        :return: None 直接修改a，无返回
        '''
        mdx = [p[0] - self.p[0], p[1] - self.p[1], p[2] - self.p[2]]
        odx = ((p[0] - self.p[0]) ** 2 + (p[1] - self.p[1]) ** 2 + (p[2] - self.p[2]) ** 2) ** 0.5
        li = [lisize * mdx[0] / odx, lisize * mdx[1] / odx, lisize * mdx[2] / odx]
        self.force(li)

    def resilience(self, x=None, k=100, other=None, string=False):
        '''
        对某两个点施以弹力
        :param x: float 弹簧原长 None 默认当前长度为原长
        :param k: float 劲度系数
        :param other: Phy 弹簧的另一个点
        :param string: bool 弹力模型为线型（True）或杆型（False）
        :return: None 直接修改a，无返回
        '''
        if x is None and (not ((self, other) in Phy.rbook.keys())):
            Phy.rbook[(self, other)] = ((other.p[0] - self.p[0]) ** 2 + (other.p[1] - self.p[1]) ** 2 + (
                        other.p[2] - self.p[2]) ** 2) ** 0.5
            x = Phy.rbook[(self, other)]
        elif x is None:
            x = Phy.rbook[(self, other)]

        dx = ((other.p[0] - self.p[0]) ** 2 + (other.p[1] - self.p[1]) ** 2 + (other.p[2] - self.p[2]) ** 2) ** 0.5 - x
        if dx<0 and string is True:
            lisize=0
        else:
            lisize = dx * k
        self.force2(lisize, other.p)
        other.force2(lisize, self.p)
        if not((self, other) in Phy.rbiao):
            Phy.rbiao.append((self, other))

    rbook = {}  # 用来储存弹簧的长度，向x填入None时用

    rbiao = []  # 用来储存需要连成弹簧的点，显示用，显示后要清空！

    @classmethod
    def rread(cls,biao):
        '''
        将弹力列表中的内容转为弹力
        :param biao: [{"self":Phy, "other":Phy, "x":float, "k":float, "string":bool},...]
        :return: None
        '''
        for i in biao:
            i["self"].resilience(i["x"],i["k"],i["other"],i["string"])

    def bounce(self, k, other="*"):
        '''
        对指定点施以弹力（撞击时）
        :param k: float 劲度系数
        :param other: "*" 或 Phy 施力的另一个物体，当为"*"时指对所有点
        :return: None 直接修改a，无返回
        '''
        if other == "*":
            for i in Phy.biao:
                if i == self:
                    continue
                elif (((i.p[0] - self.p[0]) ** 2 + (i.p[1] - self.p[1]) ** 2 + (
                        i.p[2] - self.p[2]) ** 2) ** 0.5) - self.r - i.r <= 0:
                    self.resilience(self.r + i.r, k / 2, i)
        else:
            if (((other.p[0] - self.p[0]) ** 2 + (other.p[1] - self.p[1]) ** 2 + (
                    other.p[2] - self.p[2]) ** 2) ** 0.5) - self.r - other.r <= 0:
                self.resilience(self.r + other.r, k, other)

    @classmethod
    def gravity(cls, g):
        '''
        对全部点施以引力
        :param g: float 引力常数
        :return: None 直接修改a，无返回
        '''
        for oout in Phy.biao:
            for oin in Phy.biao:
                if oout == oin:
                    continue
                r = ((oout.p[0] - oin.p[0]) ** 2 + (oout.p[1] - oin.p[1]) ** 2 + (oout.p[2] - oin.p[2]) ** 2) ** 0.5
                G = g * oout.m * oin.m / (r ** 2)
                oout.force2(G, oin.p)

    @classmethod
    def coulomb(cls,k):
        '''
        对全部点施以静电力
        :param k: 静电力常量
        :return: None 直接修改a，无返回
        '''
        for oout in Phy.biao:
            for oin in Phy.biao:
                if oout == oin:
                    continue
                r = ((oout.p[0] - oin.p[0]) ** 2 + (oout.p[1] - oin.p[1]) ** 2 + (oout.p[2] - oin.p[2]) ** 2) ** 0.5
                f = -k * oout.e * oin.e / (r ** 2)
                oout.force2(f, oin.p)

    def electrostatic(self,k):
        '''
        对某点施以静电力
        :param k: 静电力常量
        :return: None 直接修改a，无返回
        '''
        for i in Phy.biao:
            if i==self:
                continue
            r = ((self.p[0]-i.p[0])**2+(self.p[1]-i.p[1])**2+(self.p[2]-i.p[2])**2)**0.5
            if r==0:
                r=10e-9
            f = -k*self.e*i.e/r**2
            self.force2(f,i.p)

    @classmethod
    def momentum(cls):
        '''
        计算全局动量和
        :return: list[x,y,z] 矢量
        '''
        dongliang = [0, 0, 0]
        for i in Phy.biao:
            dongliang[0] += i.v[0] * i.m
            dongliang[1] += i.v[1] * i.m
            dongliang[2] += i.v[2] * i.m
        return dongliang

    @classmethod
    def run(cls, t):
        '''
        运行当前模型（力的应该在run之前运算）
        :param t: float 运行一帧的时间
        :return: None 直接修改每个点的v、p、a，无返回
        '''
        for dian in Phy.biao:
            dian.v[0] = dian.v[0] + dian.a[0] * t
            dian.v[1] = dian.v[1] + dian.a[1] * t
            dian.v[2] = dian.v[2] + dian.a[2] * t
            dian.p[0] = dian.p[0] + dian.v[0] * t
            dian.p[1] = dian.p[1] + dian.v[1] * t
            dian.p[2] = dian.p[2] + dian.v[2] * t
            dian.axianshi = dian.a[:]
            dian.a = [0, 0, 0]

    @classmethod
    def hprun(cls,t):
        '''
        以更高精度运行当前模型（建议在恒力模型中使用，力的应该在run之前运算）
        :param t: float 运行一帧的时间
        :return: None 直接修改每个点的v、p、a，无返回
        '''
        for dian in Phy.biao:

            dian.p[0] = dian.p[0] + dian.v[0] * t + 0.5*dian.a[0] * t ** 2
            dian.p[1] = dian.p[1] + dian.v[1] * t + 0.5*dian.a[1] * t ** 2
            dian.p[2] = dian.p[2] + dian.v[2] * t + 0.5*dian.a[2] * t ** 2
            dian.v[0] = dian.v[0] + dian.a[0] * t
            dian.v[1] = dian.v[1] + dian.a[1] * t
            dian.v[2] = dian.v[2] + dian.a[2] * t
            dian.axianshi = dian.a[:]
            dian.a = [0, 0, 0]

    @classmethod
    def tready(cls):
        '''
        在使用显示模块前需要调用这个函数
        :return: None
        '''
        import turtle
        turtle.tracer(0)
        turtle.penup()
        turtle.hideturtle()

    @classmethod
    def saveone(cls):
        m=[]
        v=[]
        p=[]
        r=[]
        color=[]
        axianshi=[]
        rbiao=[]
        for i in Phy.biao:
            m.append(i.m)
            v.append(tuple(i.v))
            p.append(tuple(i.p))
            r.append(i.r)
            color.append(i.color)
            axianshi.append(i.axianshi)
        for j in Phy.rbiao:
            rbiao.append((Phy.biao.index(j[0]),Phy.biao.index(j[1])))
        m=tuple(m)
        v = tuple(v)
        p = tuple(p)
        r = tuple(r)
        color = tuple(color)
        axianshi = tuple(axianshi)
        rbiao=tuple(rbiao)

        z=(m,v,p,r,color,axianshi,rbiao)
        return z

    @classmethod
    def readone(cls,z):
        Phy.biao = []
        Phy.rbiao = []

        for j in range(len(z[0])):
            a=Phy(z[0][j],z[1][j],z[2][j],z[3][j],z[4][j])

        for i2 in range(len(Phy.biao)):
            Phy.biao[i2].axianshi=z[5][i2]

        for k in z[6]:
            Phy.rbiao.append((Phy.biao[k[0]],Phy.biao[k[1]]))

    zhenshu = 0  # 显示过的帧数

    @classmethod
    def xianxing(cls,d,x):
        '''
        线性变换
        :param d: list[x,y,z] 原坐标
        :param x: list[[x,y,z],[x,y,z],[x,y,z]] 矩阵
        :return: list[x,y,z] 变换后坐标
        '''
        return [d[0]*x[0][0]+d[1]*x[1][0]+d[2]*x[2][0],
                d[0]*x[0][1]+d[1]*x[1][1]+d[2]*x[2][1],
                d[0]*x[0][2]+d[1]*x[1][2]+d[2]*x[2][2]]

    @classmethod
    def shijiaoshi(cls,d,fm,to):    #测试中
        '''
        视角矢量
        :param d: list[x,y,z] 需要变换的点的坐标
        :param fm: list[x,y,z] 出发点坐标
        :param to: list[x,y,z] 看向点坐标
        :return: list[x,y,z] 变换后点坐标
        '''
        d1=[d[0]-fm[0],d[1]-fm[1],d[2]-fm[2]]
        dis=(to[0]**2+to[1]**2+to[2]**2)**0.5
        dis2=(to[0]**2+to[1]**2)**0.5

        m=[[to[1]/dis2,to[0]/dis2,0],
           [to[2]*to[0]/dis2,to[2]*to[1]/dis2,dis2],
           [to[0]/dis,to[1]/dis,to[2]/dis]]
        return Phy.xianxing(d1,m)

    @classmethod
    def tplay(cls, fps=1, a=False, v=False, c=None, x=None):
        '''
        使用turtle的显示模块（只显示1帧，需和run一起循环调用）
        :param fps: int 跳过的帧数
        :param a: bool 是否显示加速度标
        :param v: bool 是否显示速度标
        :param c: Phy 参考系
        :param x: list[[x,y,z],[x,y,z],[x,y,z]] 线性变换矩阵
        :return: None
        '''
        if c is None:
            c=DingPhy(0,[0,0,0],[0,0,0],0)
        if x is None:
            x=[[1,0,0],[0,1,0],[0,0,1]]
        if Phy.zhenshu % fps == 0:
            import turtle
            for i in Phy.rbiao:
                turtle.color("black")
                dr0=Phy.xianxing([i[0].p[0]-c.p[0],
                                  i[0].p[1]-c.p[1],
                                  i[0].p[2]-c.p[2]],x)
                dr1 = Phy.xianxing([i[1].p[0] - c.p[0],
                                    i[1].p[1] - c.p[1],
                                    i[1].p[2] - c.p[2]], x)
                turtle.goto(dr0[0], dr0[1])
                turtle.pendown()
                turtle.goto(dr1[0], dr1[1])
                turtle.penup()
            Phy.rbiao = []

            for i in Phy.biao:
                d=Phy.xianxing([i.p[0]-c.p[0],
                                i.p[1]-c.p[1],
                                i.p[2]-c.p[2]],x)
                turtle.goto(d[0], d[1])
                turtle.dot(i.r * 2, i.color)
                if a == True:
                    da=Phy.xianxing([i.p[0]-c.p[0] + i.axianshi[0]* 1-c.axianshi[0],
                                     i.p[1]-c.p[1] + i.axianshi[1]* 1-c.axianshi[1],
                                     i.p[2]-c.p[2] + i.axianshi[2]* 1-c.axianshi[2]],x)
                    turtle.pencolor("red")
                    turtle.goto(d[0], d[1])
                    turtle.pendown()
                    turtle.goto(da[0] , da[1] )
                    turtle.penup()
                    turtle.pencolor("black")
                if v == True:
                    dv=Phy.xianxing([i.p[0]-c.p[0] + i.v[0]* 1-c.v[0],
                            i.p[1]-c.p[1] + i.v[1]* 1-c.v[1],
                            i.p[2]-c.p[2] + i.v[2]* 1-c.v[2]],x)
                    turtle.pencolor("blue")
                    turtle.goto(d[0], d[1])
                    turtle.pendown()
                    turtle.goto(dv[0] , dv[1] )
                    turtle.penup()
                    turtle.pencolor("black")

            turtle.update()
            turtle.clear()
        Phy.zhenshu += 1

    class tgraph:
        '''
        使用turtle实现的图表显示，使用前先创建对象
        在循环里使用draw
        '''
        def __init__(self):
            self.biao=[]
            self.zhenshu=0

        def clean(self):
            '''
            清空图表
            :return: None
            '''
            self.__init__()

        def draw(self,inx,iny,dis,chang=200,kx=1,ky=1,tiao=1,color="black",phyon=True,bi=False):
            '''
            使用turtle实现的图表显示
            :param inx: float 点的x坐标，若希望图表不会移动，此处为None
            :param iny: float 点的y坐标
            :param dis: list[x,y] 坐标原点位置
            :param chang: float 图表长度
            :param kx: float x放大系数
            :param ky: float y放大系数
            :param tiao: float 每隔多少次采样
            :param color: list(r,g,b) 颜色
            :param phyon: bool 是否使用Phy.tplay
            :param bi: bool 是否在点之间画线
            :return: None
            '''
            import turtle
            if phyon is False:
                Phy.tready()

            if self.zhenshu%tiao==0:
                if inx is None:
                    self.biao.append([len(self.biao), iny])
                else:
                    self.biao.append([inx, iny])
            if len(self.biao) > chang:
                self.biao.pop(0)

            if inx is None:
                if bi is True:
                    turtle.pencolor(color)
                    turtle.goto(dis[0], dis[1] + self.biao[0][1] * ky)
                    turtle.pendown()
                for i in range(len(self.biao)):
                    turtle.goto(dis[0] + i * kx, dis[1] + self.biao[i][1] * ky)
                    turtle.dot(2, color)
                if bi is True:
                    turtle.penup()
            else:
                if bi is True:
                    turtle.pencolor(color)
                    turtle.goto(dis[0] + self.biao[0][0] * kx, dis[1] + self.biao[0][1] * ky)
                    turtle.pendown()
                for i in range(len(self.biao)):
                    turtle.goto(dis[0] + self.biao[i][0] * kx, dis[1] + self.biao[i][1] * ky)
                    turtle.dot(2, color)
                if bi is True:
                    turtle.penup()

            if phyon is False:
                turtle.update()
                turtle.clear()
            self.zhenshu+=1


class DingPhy(Phy): #定点，不参与力的计算
    def __init__(self, m, v, p, r=None, color="black"):
        self.m = m
        self.v = v
        self.p = p
        self.a = [0, 0, 0]
        if r is None:
            r = m ** 0.3
        self.r = r
        self.axianshi = self.a
        self.color = color

class Changjing:
    '''
    场景，运行object
    '''

    allbiao = [] #装着所有object的表
    camara = [0, 0, -1] #相机位置
    k = 1 #镜头放大参数

    @classmethod
    def tready(cls):
        '''
        在使用显示模块前需要调用这个函数
        :return: None
        '''
        import turtle
        turtle.tracer(0)
        turtle.penup()
        turtle.hideturtle()

    @classmethod
    def view(cls, p, camara, k):
        '''
        小孔成像变换
        :param p: list[x,y,z]被拍摄点位置
        :param camara: list[x,y,z]摄相机位置
        :param k: float镜头放大参数（k>0）
        :return: tuple(dx, dy)变换后坐标
        '''
        viewlength = camara[2] - p[2]
        if viewlength==0:
            viewlength=0.0000001
        dx = (camara[0] - p[0]) / viewlength * k
        dy = (camara[1] - p[1]) / viewlength * k
        return (dx, dy)

    @classmethod
    def biaoupdate(cls):
        '''
        调整图形渲染顺序，每次更新allbiao后需调用
        :return: None
        '''
        Changjing.allbiao.sort(key=lambda x: x.p[2], reverse=True)

    @classmethod
    def play(cls,t):
        '''
        使用turtle的显示模块（只显示1帧，需和run一起循环调用）
        :param t: 运行1帧中的时间
        :return: None
        '''
        import turtle
        for i in Changjing.allbiao:
            if i.p[2] <=Changjing.camara[2]:
                continue
            i.draw()
        turtle.update()
        turtle.clear()
        Phy.run(t)

    @classmethod
    def keymove(cls):
        import turtle
        def zf():
            Changjing.k *= 1.1

        def zb():
            Changjing.k *= 0.9

        def f():
            Changjing.camara[2] += 1

        def b():
            Changjing.camara[2] -= 1

        def l():
            Changjing.camara[0] -= 100

        def r():
            Changjing.camara[0] += 100

        def u():
            Changjing.camara[1] += 100

        def d():
            Changjing.camara[1] -= 100

        def reset(x, y):
            Changjing.k = 1
            Changjing.camara = [0, 0, -1]

        turtle.onkeypress(zf, key="=")
        turtle.onkeypress(zb, key="-")
        turtle.onkeypress(f, key="w")
        turtle.onkeypress(b, key="s")
        turtle.onkeypress(l, key="Left")
        turtle.onkeypress(r, key="Right")
        turtle.onkeypress(u, key="Up")
        turtle.onkeypress(d, key="Down")
        turtle.onscreenclick(reset)
        turtle.listen()

class object:
    '''
    对Phy的封装
    '''
    def __init__(self, color=(0, 0, 0)):
        self.biao = []
        self.color = color
        Changjing.allbiao.append(self)

    def tri(self, d, h, p, v=None, m=1, color="black"):
        '''
        自己变为三角形对象
        :param d: 底边长
        :param h: 高长
        :param p: 位置（左下角）
        :param v: 速度
        :param m: 质量
        :param color: 颜色
        :return: None
        '''
        if v is None:
            v = [0, 0, 0]
        self.biao = [Phy(m, v, [p[0], p[1], p[2]]),
                     Phy(m, v, [p[0] + d, p[1], p[2]]),
                     Phy(m, v, [p[0] + d/2, p[1] + h, p[2]]),
                     Phy(m, v, p),
                     ]
        self.color = color
        self.p=p

    def fang(self, r, p, v=None, m=1, color="black"):
        '''
        自己变为正方形对象
        :param r: 边长
        :param p: 位置（左下角）
        :param v: 速度
        :param m: 质量
        :param color: 颜色
        :return: None
        '''
        if v is None:
            v = [0, 0, 0]
        self.biao = [Phy(m, v, [p[0], p[1], p[2]]),
                     Phy(m, v, [p[0] + r, p[1], p[2]]),
                     Phy(m, v, [p[0] + r, p[1] + r, p[2]]),
                     Phy(m, v, [p[0], p[1] + r, p[2]]),
                     Phy(m, v, p),
                     ]
        self.color = color
        self.p=p

    def cfang(self, c,f, p, v=None, m=1, color="black"):
        '''
        自己变为正方形对象
        :param c: 长
        :param f: 宽
        :param p: 位置（左下角）
        :param v: 速度
        :param m: 质量
        :param color: 颜色
        :return: None
        '''
        if v is None:
            v = [0, 0, 0]
        self.biao = [Phy(m, v, [p[0], p[1], p[2]]),
                     Phy(m, v, [p[0] + c, p[1], p[2]]),
                     Phy(m, v, [p[0] + c, p[1] + f, p[2]]),
                     Phy(m, v, [p[0], p[1] + f, p[2]]),
                     Phy(m, v, p),
                     ]
        self.color = color
        self.p=p

    def draw(self):
        import turtle
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in self.biao:
            turtle.goto(Changjing.view(i.p, Changjing.camara, Changjing.k))
        turtle.end_fill()


