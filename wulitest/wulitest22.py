from wuli import *
import turtle
turtle.bgcolor(0,0,0)
def s(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**0.5
Phy.tready()
k=50
r=7
biao=[]
for i in range(-r,r+1):
    for j in range(-r,r+1):
        if i%2==0:
            biao.append(Phy(3, [0, 0, 0], [j*k, i * (3 ** 0.5)*0.5*k, 0],5))
        else:
            biao.append(Phy(3, [0, 0, 0], [(j+0.5) * k, i * (3 ** 0.5)*0.5 * k, 0], 5))
biao[round(len(biao)/2)].v=[0,0,100]
biao.pop(2*r+1)
biao.pop(-1)
tanhuang=[]
for i in biao:
    for j in biao:
        if i==j:
            continue
        for l in tanhuang:
            if i in l and j in l:
                continue
        if s(i.p,j.p)<= k+1:
            tanhuang.append([i,j])


while True:
    for i in tanhuang:
        i[0].resilience(None,100,i[1])
    for i in biao:
        if i.axianshi!=[0,0,0]:
            i.color="red"
    Phy.run(0.02)
    Phy.tplay(a=True)