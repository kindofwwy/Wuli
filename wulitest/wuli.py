import turtle
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

    def __repr__(self):
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
        :param string: bool 弹力模型为绳型（True）或杆型（False）
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
        :param other: "*" 或 list[Phy,Phy...] 被碰撞的另一组物体，当为"*"时指对所有点
        :return: None 直接修改a，无返回
        '''
        if other == "*":
            other=Phy.biao
        for i in other:
            if i == self:
                continue
            elif (((i.p[0] - self.p[0]) ** 2 + (i.p[1] - self.p[1]) ** 2 + (
                    i.p[2] - self.p[2]) ** 2) ** 0.5) - self.r - i.r <= 0:
                self.resilience(self.r + i.r, k / 2, i)


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

            dian.p[0] = dian.p[0] + dian.v[0] * t + 0.5 * dian.a[0] * t ** 2
            dian.p[1] = dian.p[1] + dian.v[1] * t + 0.5 * dian.a[1] * t ** 2
            dian.p[2] = dian.p[2] + dian.v[2] * t + 0.5 * dian.a[2] * t ** 2
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
        '''
        保存当前的状态（包括所有的点，其质量、位置、速度和加速度、半径、颜色，以及rbiao）为一个元组
        :return: tuple((m0,m1...),(v0,v1...),(p0,p1...),(r0,r1...),(color0,color1...),(a0,a1...),rbiao)
        '''
        m=[]
        v=[]
        p=[]
        r=[]
        color=[]
        axianshi=[]
        rbiao=[]
        for i in Phy.biao:
            m.append(i.m)
            v.append(i.v)
            p.append(i.p)
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
        '''
        读取saveone中返回的元组，将当前环境设置为元组中的状态
        :param z: tuple((m0,m1...),(v0,v1...),(p0,p1...),(r0,r1...),(color0,color1...),(a0,a1...),rbiao)
        :return: None 修改Phy中的biao和rbiao，无返回
        '''
        Phy.biao = []
        Phy.rbiao = []

        for j in range(len(z[0])):
            Phy(z[0][j],z[1][j],z[2][j],z[3][j],z[4][j])

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
    def reference(cls,d1,dr):
        '''
        参考系变化
        :param d1: list[x,y,z] 被变化坐标
        :param dr: list[x,y,z] 参考系点
        :return: list[x,y,z] 变化后坐标
        '''
        return [d1[0]-dr[0],d1[1]-dr[1],d1[2]-dr[2]]

    @classmethod
    def perspective(cls,d,cam,k):
        '''
        透视变换
        :param d: list[x,y,z] 被变换的点
        :param cam: list[x,y,z] 相机坐标，相机朝向z轴正半轴方向
        :param k: float 放大倍率
        :return: list[x,y] 变换后位置
        '''
        d2=Phy.reference(d,cam)
        d2[2]=0.00001 if d2[2]==0 else d[2]
        d2=[d2[0]*k/d2[2],d2[1]*k/d2[2]]
        return d2

    @classmethod
    def shijiaox(cls,fm,to):
        '''
        视角矢量x，在x-z平面上旋转坐标轴，旋转至出发点正对着看向点（x方向上）
        :param fm: list[x,y,z] 出发点坐标
        :param to: list[x,y,z] 看向点坐标
        :return: list[[x,y,z],[x,y,z],[x,y,z]] 变换矩阵
        '''
        zl = ((to[0] - fm[0]) ** 2 + (to[2] - fm[2]) ** 2) ** 0.5
        zx = -(to[0] - fm[0]) / zl
        zz = (to[2] - fm[2]) / zl
        rz = (zx ** 2 + zz ** 2) ** 0.5

        xx = zz / rz
        xy = 0
        xz = -zx / rz
        m=[[xx,xy,xz],
           [0,1,0],
           [zx,0,zz]]
        return m

    @classmethod
    def shijiaoy(cls,fm,to):
        '''
        视角矢量y，在y-z平面上旋转坐标轴，旋转至出发点正对着看向点（y方向上）
        :param fm: list[x,y,z] 出发点坐标
        :param to: list[x,y,z] 看向点坐标
        :return: list[[x,y,z],[x,y,z],[x,y,z]] 变换矩阵
        '''
        zl = ((to[1] - fm[1]) ** 2 + (to[2] - fm[2]) ** 2) ** 0.5
        zy = -(to[1] - fm[1]) / zl
        zz = (to[2] - fm[2]) / zl
        rz = (zy ** 2 + zz ** 2) ** 0.5

        yx = 0
        yy = zz / rz
        yz = -zy / rz
        m = [[1, 0, 0],
             [yx, yy, yz],
             [0, zy, zz]]
        return m


    @classmethod
    def shijiaoshi(cls,fm,to):
        '''
        视角矢量，旋转坐标轴，旋转至出发点正对着看向点
        :param fm: list[x,y,z] 出发点坐标
        :param to: list[x,y,z] 看向点坐标
        :return: list[[x,y,z],[x,y,z],[x,y,z]] 变换矩阵
        '''
        # zl=((to[0]-fm[0])**2+(to[1]-fm[1])**2+(to[2]-fm[2])**2)**0.5
        # zx=-(to[0]-fm[0])/zl
        # zy=-(to[1]-fm[1])/zl
        # zz=(to[2]-fm[2])/zl
        # rz=(zx**2+zz**2)**0.5
        # xx=zz/rz
        # xy=0
        # xz=-zx/rz
        # yz=-(xx*zy-zx*xy)
        # yx=-(xy*zz-zy*xz)
        # yy=(xx*zz-zx*xz)
        # m=[[xx,xy,xz],
        #    [yx,yy,yz],
        #    [zx,zy,zz]]
        mx=Phy.shijiaox(fm,to)
        fm=Phy.xianxing(fm,mx)
        to=Phy.xianxing(to,mx)
        my=Phy.shijiaoy(fm,to)
        m=[Phy.xianxing(mx[0],my),
           Phy.xianxing(mx[1],my),
           Phy.xianxing(mx[2],my)]
        return m

    @classmethod
    def dotpos(cls,pos,c=None,x=None):
        '''
        计算并返回坐标点经过一系列变换后的位置
        :param pos: list[x,y,z] 坐标点位置
        :param c: list[x,y,z] 参考系
        :param x: list[[x,y,z],[x,y,z],[x,y,z]] 线性变换矩阵
        :return: list[x,y,z] 坐标点变换后位置
        '''
        if c is None:
            c=[0,0,0]
        if x is None:
            x=[[1,0,0],[0,1,0],[0,0,1]]
        return Phy.xianxing(Phy.reference(pos,c),x)


    @classmethod
    def tplay(cls, fps=1, a=False, v=False, c=None, x=None, azoom=1, vzoom=1, k=None):
        '''
        使用turtle的显示模块（只显示1帧，需和run一起循环调用）
        :param fps: int 跳过的帧数
        :param a: bool 是否显示加速度标
        :param v: bool 是否显示速度标
        :param c: Phy 参考系
        :param x: list[[x,y,z],[x,y,z],[x,y,z]] 线性变换矩阵
        :param azoom: float 加速度标缩放系数
        :param vzoom: float 速度标缩放系数
        :param k: float 透视变换放大系数，为None时不进行透视变换
        :return: None
        '''
        toushi=lambda x:Phy.perspective(x,[0,0,0],k) if k is not None else x
        if c is None:
            c=DingPhy(0,[0,0,0],[0,0,0],0)
        if x is None:
            x=[[1,0,0],[0,1,0],[0,0,1]]
        if Phy.zhenshu % fps == 0:
            #import turtle
            for i in Phy.rbiao:     #弹簧绘制
                turtle.color("black")
                dr0=Phy.dotpos(i[0].p,c.p,x)
                dr1=Phy.dotpos(i[1].p,c.p,x)
                if k is not None and (dr0[2]<=0 or dr1[2]<=0) :
                    continue
                dr0=toushi(dr0)
                dr1=toushi(dr1)
                turtle.goto(dr0[0], dr0[1])
                turtle.pendown()
                turtle.goto(dr1[0], dr1[1])
                turtle.penup()
            Phy.rbiao = []

            for i in Phy.biao:      #点绘制
                d=Phy.dotpos(i.p,c.p,x)
                if k is not None and d[2]<=0:
                    continue
                d2=toushi(d)
                turtle.goto(d2[0], d2[1])
                turtle.dot(i.r*2/d[2]*k if k is not None else i.r*2, i.color)
                if a == True:
                    da=Phy.xianxing([i.p[0]-c.p[0] + (i.axianshi[0]* 1-c.axianshi[0])*azoom,
                                     i.p[1]-c.p[1] + (i.axianshi[1]* 1-c.axianshi[1])*azoom,
                                     i.p[2]-c.p[2] + (i.axianshi[2]* 1-c.axianshi[2])*azoom],x)
                    if k is not None and da[2]<=0:
                        continue
                    da=toushi(da)
                    turtle.pencolor("red")
                    turtle.goto(d2[0], d2[1])
                    turtle.pendown()
                    turtle.goto(da[0], da[1])
                    turtle.penup()
                    turtle.pencolor("black")
                if v == True:
                    dv=Phy.xianxing([i.p[0]-c.p[0] + (i.v[0]* 1-c.v[0])* vzoom,
                            i.p[1]-c.p[1] + (i.v[1]* 1-c.v[1])* vzoom,
                            i.p[2]-c.p[2] + (i.v[2]* 1-c.v[2])* vzoom],x)
                    if k is not None and dv[2]<=0:
                        continue
                    dv=toushi(dv)
                    turtle.pencolor("blue")
                    turtle.goto(d2[0], d2[1])
                    turtle.pendown()
                    turtle.goto(dv[0], dv[1])
                    turtle.penup()
                    turtle.pencolor("black")

            turtle.update()
            turtle.clear()
        Phy.zhenshu += 1

    class camera:
        def __init__(self,campos=None,lookpos=None,fix=True,k=300):
            '''
            创建一个相机
            :param campos: list[x,y,z] 相机位置
            :param lookpos: list[x,y,z] 注视点坐标
            :param fix: bool 相机是否固定（不受到Phy的影响）
            :param k: float 画面放大系数
            '''
            if campos is None:
                campos=[0,0,-300]
            if lookpos is None:
                lookpos=[0,0,0]
            if fix:
                self.cam=DingPhy(1,[0,0,0],campos)
            else:
                self.cam=Phy(1,[0,0,0], campos)
            l=((lookpos[0]-campos[0])**2+(lookpos[1]-campos[1])**2+(lookpos[2]-campos[2])**2)**0.5
            self.relalookpos=[(lookpos[0]-campos[0])/l, # 相对注视点坐标
                              (lookpos[1]-campos[1])/l,
                              (lookpos[2]-campos[2])/l]
            self.k=k

        def setlookpos(self,lookpos):
            '''
            设置相机视角
            :param lookpos: list[x,y,z] 注视点坐标
            :return: None
            '''
            l = ((lookpos[0] - self.cam.p[0]) ** 2 + (lookpos[1] - self.cam.p[1]) ** 2 + (lookpos[2] - self.cam.p[2]) ** 2) ** 0.5
            self.relalookpos = [(lookpos[0] - self.cam.p[0]) / l,
                                (lookpos[1] - self.cam.p[1]) / l,
                                (lookpos[2] - self.cam.p[2]) / l]

        def dotposspace(self,pos):
            x = Phy.shijiaoshi(self.cam.p, [self.relalookpos[0] + self.cam.p[0],
                                            self.relalookpos[1] + self.cam.p[1],
                                            self.relalookpos[2] + self.cam.p[2]])
            d = Phy.dotpos(pos, self.cam.p, x)
            return d

        def cdotpos(self,pos):
            '''
            返回一个点被相机拍到后在屏幕上的位置
            :param pos: list[x,y,z] 点的坐标
            :return: list[x,y] or None 在屏幕上的坐标，当无法进行透视变换时返回None
            '''
            x = Phy.shijiaoshi(self.cam.p, [self.relalookpos[0] + self.cam.p[0],
                                            self.relalookpos[1] + self.cam.p[1],
                                            self.relalookpos[2] + self.cam.p[2]])
            d=Phy.dotpos(pos,self.cam.p,x)
            if d[2]>0:
                return Phy.perspective(d,[0,0,0],self.k)
            return None

        @classmethod
        def tready(self):
            '''
            请使用前调用
            :return: None
            '''
            Phy.tready()

        def tplay(self,a=False,v=False,azoom=1,vzoom=1,zuobiaoxian=False):
            '''
            使用turtle的相机显示模块（只显示1帧，需循环调用）
            :param a: bool 是否显示加速度标
            :param v: bool 是否显示速度标
            :param azoom: float 加速度标放大系数
            :param vzoom: float 速度标放大系数
            :param zuobiaoxian: bool 是否显示迷你坐标线
            :return: None
            '''
            x = Phy.shijiaoshi(self.cam.p, [self.relalookpos[0] + self.cam.p[0],
                                            self.relalookpos[1] + self.cam.p[1],
                                            self.relalookpos[2] + self.cam.p[2]])
            if zuobiaoxian:
                xian = [Phy.xianxing([100, 0, 0], x),
                        Phy.xianxing([0, 100, 0], x),
                        Phy.xianxing([0, 0, 100], x)]
                turtle.goto(xian[2][0], xian[2][1])
                turtle.dot(3, "red")
                for i in range(len(xian)):
                    turtle.pencolor("black")
                    turtle.goto(0, 0)
                    turtle.pd()
                    turtle.goto(xian[i][0], xian[i][1])
                    turtle.pu()
            Phy.tplay(a=a,v=v,azoom=azoom,vzoom=vzoom,c=self.cam,x=x,k=self.k)

        def movecam(self, stepsize=1, camstepsize=0.02):
            '''
            通过turtle键盘控制移动相机与转换视角
            前进：w
            后退：s
            左移：a
            右移：d
            上移：空格
            下移：左Control
            左转：左箭头
            右转：右箭头
            上仰：上箭头
            下俯：下箭头
            放大：]
            缩小：[
            :param stepsize: float 相机移动步长
            :param camstepsize: float 相机视角转动步长
            :return: None
            '''
            def fw():
                dl = (self.relalookpos[0] ** 2 + self.relalookpos[2] ** 2) ** 0.5
                self.cam.p[0] += self.relalookpos[0] / dl * stepsize
                self.cam.p[2] += self.relalookpos[2] / dl * stepsize
            def bw():
                dl = (self.relalookpos[0] ** 2 + self.relalookpos[2] ** 2) ** 0.5
                self.cam.p[0] -= self.relalookpos[0] / dl * stepsize
                self.cam.p[2] -= self.relalookpos[2] / dl * stepsize
            def le():
                dl = (self.relalookpos[0] ** 2 + self.relalookpos[2] ** 2) ** 0.5
                self.cam.p[0] -= self.relalookpos[2] / dl * stepsize
                self.cam.p[2] -= -self.relalookpos[0] / dl * stepsize
            def ri():
                dl = (self.relalookpos[0] ** 2 + self.relalookpos[2] ** 2) ** 0.5
                self.cam.p[0] += self.relalookpos[2] / dl * stepsize
                self.cam.p[2] += -self.relalookpos[0] / dl * stepsize
            def zp():
                self.cam.p[1] += stepsize
            def zn():
                self.cam.p[1] -= stepsize
            def cu():
                self.relalookpos[1] += camstepsize
            def cd():
                self.relalookpos[1] -= camstepsize
            def cl():
                dl = (self.relalookpos[0] ** 2 + self.relalookpos[2] ** 2) ** 0.5
                self.relalookpos[0] -= self.relalookpos[2] / dl * camstepsize
                self.relalookpos[2] -= -self.relalookpos[0] / dl * camstepsize
            def cr():
                dl = (self.relalookpos[0] ** 2 + self.relalookpos[2] ** 2) ** 0.5
                self.relalookpos[0] += self.relalookpos[2] / dl * camstepsize
                self.relalookpos[2] += -self.relalookpos[0] / dl * camstepsize
            def zp2():
                self.relalookpos[2] += camstepsize
            def zn2():
                self.relalookpos[2] -= camstepsize
            def zin():
                self.k*=1.1
            def zout():
                self.k*=0.9

            turtle.onkeypress(fw, key="w")
            turtle.onkeypress(bw, key="s")
            turtle.onkeypress(le, key="a")
            turtle.onkeypress(ri, key="d")
            turtle.onkeypress(zp, key="space")
            turtle.onkeypress(zn, key="Control_L")
            turtle.onkeypress(cu, key="Up")
            turtle.onkeypress(cd, key="Down")
            turtle.onkeypress(cl, key="Left")
            turtle.onkeypress(cr, key="Right")
            turtle.onkeypress(zp2, key="u")
            turtle.onkeypress(zn2, key="o")
            turtle.onkeypress(zin, key="]")
            turtle.onkeypress(zout, key="[")
            turtle.listen()

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
            while len(self.biao) > chang:
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
        self.axianshi = [0,0,0]
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


