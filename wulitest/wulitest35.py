from wuli import *
import random
Phy.tready()

def arc(cur,dr,lr=0,mi=1.0):
    biao = []
    for y in range((round(-dr/mi)),round(dr/mi+1)):
        biao.append(Phy(1,[0,0,0],[(cur**2-(y*mi)**2)**0.5-cur+lr,y*mi,0],r=1))
    return biao

def sphere(cur,dr,lr=0):
    biao=[]
    for z in range(-dr,dr+1):
        for y in range(-dr,dr+1):
            biao.append(Phy(1,[0,0,0],[(cur**2-z**2-y**2)**0.5-cur+lr,y,z],r=1))
    return biao


def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5

def isontrack(light, point):
    t=(point.p[0]-light.p[0])/light.v[0]
    if t<0:
        return False
    return distance([point.p[0],light.p[1]+t*light.v[1],light.p[2]+t*light.v[2]],point.p)<1

def findmirror(light,mirrorlist=None):
    ontrackdict = {}
    if mirrorlist is None:
        mirrorlist=Phy.biao
    for i in mirrorlist:
        if i == light:
            continue
        if isontrack(light, i):
            ontrackdict[distance(light.p, i.p)] = i
    if ontrackdict == {}:
        return None
    return ontrackdict[min(ontrackdict.keys())]

def jumptomirror(light,mirror,tdis):
    t = max(abs(mirror.p[0] - light.p[0]) / light.v[0] - tdis, 0)
    light.p = [light.p[0] + light.v[0] * t,
               light.p[1] + light.v[1] * t,
               light.p[2] + light.v[2] * t]

def directlight(dr,lr,amount):
    r=dr*2/(amount+1)
    r0=-dr+r
    lightlist=[]
    for i in range(amount):
        lightlist.append(Phy(1,[1,0,0],[lr,r0,0],r=2))
        r0+=r
    return lightlist

#sphere(300,100,100)
mirrorlist=arc(110,100,100,0.5)
lightr=50
lr=-100
while True:
    lightlist=directlight(80,-100,8)
    ltracklist=[Phy.tgraph() for i in range(len(lightlist))]
    [ltracklist[i].biao.append(lightlist[i].p[:2]) for i in range(len(lightlist))]

    # print("s1 随机发射")
    # light=Phy(1,[1,random.uniform(-2,2),0],
    #           [lr,random.uniform(-lightr,lightr),0],r=5)

    while True:
        print("s2 寻找最近镜子点")
        #mp=findmirror(light)     #最近镜子点
        mplist=[findmirror(i) for i in lightlist]

        print("s3 跳至最近镜子点附近")
        #jumptomirror(light,mp,7)
        [jumptomirror(lightlist[i],mplist[i],4) for i in range(len(lightlist))]

        print("s4 模拟反射")
        # v0=light.v[:]
        zhen=0
        while True:
            # if light.v!=v0 and light.a==[0,0,0]:
            #     print("p")
            #     pass
            for i in lightlist:
                i.bounce(100,mirrorlist)
            for i in mirrorlist:
                i.a = [0, 0, 0]
            Phy.run(0.005)
            if zhen%500==0:
                Phy.tplay(v=True,vzoom=40,x=[[2.5,0,0],[0,2.5,0],[0,0,2.5]])
                [ltracklist[i].draw(lightlist[i].p[0],lightlist[i].p[1],[0,0],kx=2.5,ky=2.5,bi=True)
                 for i in range(len(lightlist))]
            zhen+=1

    Phy.biao.pop()



