from wuli import *
import random,turtle
Phy.tready()
biao=[Phy(5,[0,0,0],[0,-300,0],10,"red")]
l=[[3.0, 135.0, 0], [-23.0, 110.0, 0], [35.0, 111.0, 0], [-62.0, 83.0, 0], [6.0, 83.0, 0], [73.0, 80.0, 0], [-93.0, 43.0, 0], [-23.0, 39.0, 0], [29.0, 40.0, 0], [97.0, 42.0, 0]]
l2=[[-100.0, 223.0, 0], [-70.0, 221.0, 0], [-31.0, 221.0, 0], [4.0, 221.0, 0], [46.0, 223.0, 0], [86.0, 220.0, 0], [141.0, 219.0, 0], [-51.0, 253.0, 0], [-50.0, 195.0, 0], [78.0, 253.0, 0], [69.0, 182.0, 0], [-43.0, 125.0, 0], [-42.0, 88.0, 0], [-51.0, 52.0, 0], [-7.0, 127.0, 0], [23.0, 127.0, 0], [61.0, 125.0, 0], [101.0, 122.0, 0], [96.0, 102.0, 0], [91.0, 70.0, 0], [81.0, 41.0, 0], [-21.0, 40.0, 0], [11.0, 41.0, 0], [40.0, 41.0, 0], [-2.0, 86.0, 0], [32.0, 81.0, 0], [-129.0, -52.0, 0], [-85.0, -47.0, 0], [-44.0, -48.0, 0], [7.0, -46.0, 0], [82.0, -45.0, 0], [119.0, -45.0, 0], [48.0, -46.0, 0], [8.0, -4.0, 0], [0.0, -78.0, 0], [-7.0, -114.0, 0]]
l3=[[-150, -150, 0], [-150, -100, 0], [-150, -50, 0], [-150, 0, 0], [-150, 50, 0], [-150, 100, 0], [-150, 150, 0], [-100, -150, 0], [-100, -100, 0], [-100, -50, 0], [-100, 0, 0], [-100, 50, 0], [-100, 100, 0], [-100, 150, 0], [-50, -150, 0], [-50, -100, 0], [-50, -50, 0], [-50, 0, 0], [-50, 50, 0], [-50, 100, 0], [-50, 150, 0], [0, -150, 0], [0, -100, 0], [0, -50, 0], [0, 0, 0], [0, 50, 0], [0, 100, 0], [0, 150, 0], [50, -150, 0], [50, -100, 0], [50, -50, 0], [50, 0, 0], [50, 50, 0], [50, 100, 0], [50, 150, 0], [100, -150, 0], [100, -100, 0], [100, -50, 0], [100, 0, 0], [100, 50, 0], [100, 100, 0], [100, 150, 0], [150, -150, 0], [150, -100, 0], [150, -50, 0], [150, 0, 0], [150, 50, 0], [150, 100, 0], [150, 150, 0]]
def f(x,y):
    biao[0].force([x*500,y*500,0])
def s():
    biao[0].v=[0,0,0]
for i in l3:
    biao.append(Phy(10,
                    [0,0,0],
                    i,
                    r=10
                    ))
while True:
    turtle.onscreenclick(f)
    turtle.onkey(s," ")
    for i in biao:
        i.bounce(k=100000)
        i.force([-i.v[0] * 1.3, -i.v[1] * 1.3, -i.v[2] * 1.3])
    Phy.run(0.01)
    Phy.tplay(c=biao[0])
    turtle.listen()
