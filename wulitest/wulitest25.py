from wuli import *
import turtle


def shijiaoshi(to):
    dis = (to[0] ** 2 + to[1] ** 2 + to[2] ** 2) ** 0.5
    dis2 = (to[0] ** 2 + to[1] ** 2) ** 0.5

    m = [[to[1] / dis2, to[0] / dis2, 0],
         [to[2] * to[0] / dis2, to[2] * to[1] / dis2, dis2],
         [to[0] / dis, to[1] / dis, to[2] / dis]]
    return m

xy=[1,1,1]

def go(x,y):
    global xy
    xy=[x*0.01,y*0.01,1]


def zuobiaoxian(xian):
    for i in range(len(xian)):
        if i==0:
            turtle.pencolor("red")
        elif i==1:
            turtle.pencolor("green")
        elif i==2:
            turtle.pencolor("blue")
        turtle.goto(0,0)
        turtle.pd()
        turtle.goto(xian[i][0]*100,xian[i][1]*100)
        turtle.pu()

Phy.tready()

while True:

    turtle.onscreenclick(go)

    zuobiaoxian(shijiaoshi(xy))
    turtle.update()
    turtle.clear()
