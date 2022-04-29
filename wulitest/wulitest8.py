from wuli import *
import turtle
def stop(x,y):
    b.v=[0,0,0]
    c.v=[0,0,0]
Phy.tready()
a = Phy(1, [0, 0, 0], [0, 300, 0])
b = Phy(10, [0, 0, 0], [0, 200, 0])
c = Phy(10, [0, 0, 0], [0, 100, 0])
while True:
    a.resilience(100, 10000000, b)
    b.resilience(100, 10000000, c)
    b.force([-1000,-1000,0])
    c.force([1000,-1000,0])
    a.a=[0,0,0]
    Phy.run(0.001)
    Phy.tplay(a=True)
    turtle.onscreenclick(stop)
