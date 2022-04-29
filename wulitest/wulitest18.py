from wuli import *
import turtle,time
Phy.tready()
s=Phy(1000,[0,0,0],[0,0,0])
for i in range(51):
    for j in range(51):
        a=Phy(1,[0,0,100],[i*10-250,j*10-250,-10000])
        t1=time.perf_counter()
        while True:
            Phy.gravity(10)
            s.a=[0,0,0]
            Phy.run(1)
            t2=time.perf_counter()
            if t2-t1>0.5:
                print(a.p)
                break
            if a.p[2]>=10000:
                turtle.goto(a.p[0],a.p[1])
                turtle.dot(3)
                turtle.update()
                Phy.biao.pop()
                break


turtle.done()
