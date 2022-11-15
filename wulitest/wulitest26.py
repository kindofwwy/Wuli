from wuli import *
import time
Phy.tready()
a=Phy(5,[0,0,0],[0,100,0],r=5)
b=Phy(5,[0,0,0],[0,-100,0],r=5,color="red")
s=[]
for i in range(10000):
    a.resilience(100,other=b)
    s.append(str(Phy.saveone()))
    Phy.run(0.01)

for i in s:
    Phy.readone(eval(i))
    Phy.tplay()
    time.sleep(0.03)

