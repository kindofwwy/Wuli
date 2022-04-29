from wuli import *
Phy.tready()
dian=[Phy(20,[0,0,0],[-75,0,0],24.5,"red"),
      Phy(20,[0,0,0],[-25,0,0],24.5,"blue"),
      Phy(20,[0,0,0],[25,0,0],24.5,"green"),
      Phy(20,[0,0,0],[75,0,0],24.5)]
gua=[Phy(1,[0,0,0],[-75,300,0]),
     Phy(1,[0,0,0],[-25,300,0]),
     Phy(1,[0,0,0],[25,300,0]),
     Phy(1,[0,0,0],[75,300,0])]
dian[0].force([-1000000,0,0])
dian[1].force([-1000000,0,0])
dian[2].force([-1000000,0,0])
while True:
    for i in range(4):
        dian[i].resilience(300,1000000,gua[i])
        gua[i].a=[0,0,0]
        dian[i].bounce(100000)
        dian[i].force([0,-10000,0])
    Phy.run(0.001)
    Phy.tplay(10)

    
