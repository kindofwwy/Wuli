from wuli import *
Phy.tready()

pin=Phy(1,[0,0,0],[3,1.5,15.6],r=0.5)
pin2=Phy(1,[0,0,0],[3.1,1.5,15.6],r=0.5,color="red")

a=5
b=15
c=1
cam=Phy.camera([-10,0,5],[3,-3,15.6])
zhen=0
while True:
    if zhen%60==0:
        Phy(1,[0,0,0],pin.p[:],r=0.1)
        Phy(1,[0,0,0],pin2.p[:],r=0.1,color="red")

    pin.v=[a*(pin.p[1]-pin.p[0]),
           b*pin.p[0]-pin.p[1]-pin.p[0]*pin.p[2],
           -c*pin.p[2]+pin.p[0]*pin.p[1]]
    pin2.v=[a*(pin2.p[1]-pin2.p[0]),
             b*pin2.p[0]-pin2.p[1]-pin2.p[0]*pin2.p[2],
             -c*pin2.p[2]+pin2.p[0]*pin2.p[1]]
    Phy.run(0.001)
    if zhen%20==0:
        cam.tplay()
        cam.movecam(stepsize=0.2)
    zhen+=1

