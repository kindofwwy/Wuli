from wuli import *
from math import *
import turtle
def xn():
    global cx,xian
    cx+=0.1
    xx = [[1, 0, 0],
          [0, cos(cx), sin(cx)],
          [0, -sin(cx), cos(cx)]]
    for i in range(len(xian)):
        xian[i]=Phy.xianxing(xian[i],xx)
    cx=0
def xp():
    global cx,xian
    cx-=0.1
    xx = [[1, 0, 0],
          [0, cos(cx), sin(cx)],
          [0, -sin(cx), cos(cx)]]
    for i in range(len(xian)):
        xian[i]=Phy.xianxing(xian[i],xx)
    cx=0
def yn():
    global cy,xian
    cy+=0.1
    yy = [[cos(cy), 0, sin(cy)],
          [0, 1, 0],
          [-sin(cy), 0, cos(cy)]]
    for i in range(len(xian)):
        xian[i]=Phy.xianxing(xian[i],yy)
    cy=0
def yp():
    global cy,xian
    cy-=0.1
    yy = [[cos(cy), 0, sin(cy)],
          [0, 1, 0],
          [-sin(cy), 0, cos(cy)]]
    for i in range(len(xian)):
        xian[i]=Phy.xianxing(xian[i],yy)
    cy=0
def zp():
    global cz,xian
    cz+=0.1
    zz = [[cos(cz), sin(cz), 0],
          [-sin(cz), cos(cz), 0],
          [0, 0, 1]]
    for i in range(len(xian)):
        xian[i]=Phy.xianxing(xian[i],zz)
    cz=0
def zn():
    global cz,xian
    cz-=0.1
    zz = [[cos(cz), sin(cz), 0],
          [-sin(cz), cos(cz), 0],
          [0, 0, 1]]
    for i in range(len(xian)):
        xian[i]=Phy.xianxing(xian[i],zz)
    cz=0

Phy.tready()
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
        turtle.goto(xian[i][0],xian[i][1])
        turtle.pu()
cx=0
cy=0
cz=0
xian=[[100,0,0],[0,100,0],[0,0,100]]
while True:

    turtle.onkeypress(yn,"a")
    turtle.onkeypress(yp,"d")
    turtle.onkeypress(xp,"s")
    turtle.onkeypress(xn,"w")
    turtle.onkeypress(zp,"q")
    turtle.onkeypress(zn,"e")
    turtle.listen()
    zuobiaoxian(xian)
    turtle.update()
    turtle.clear()
