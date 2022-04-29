from wuli import *

Phy.tready()
dianlist = []
for i in range(100):
    dianlist.append(Phy(5, [0, 0, 0], [(i - 50) * 7, 0, 0]))
dianlist[49].force([0,-10000000,0])
dianlist[50].force([0,-10000000,0])

while True:
    for i in range(len(dianlist)):
        if i == len(dianlist) - 1:
            break
        dianlist[i].resilience(50, 100000, dianlist[i + 1])
        #dianlist[i].force([0,-10000,0])

    dianlist[0].a = [0, 0, 0]
    dianlist[-1].a = [0, 0, 0]
    Phy.run(0.001)
    Phy.tplay()
