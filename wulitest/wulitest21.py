from wuli import *
Phy.tready()
l=[]
d=31
k=2000
for i in range(-d//2,d//2):
    for j in range(-d//2,d//2):
        l.append(Phy(3,[0,0,0],[j*20,i*20,0],5))
l[(d**2)//2].v=[0,0,100]
while True:
    for i in range(len(l)):
        if l[i].axianshi!=[0,0,0]:
            l[i].color="red"
        if len(l)-i>d:
            l[i].resilience(None,k,l[i+d])
        if (i+1)%d==0 or i ==len(l)-1:
            continue
        l[i].resilience(None,k,l[i+1])

    Phy.run(0.005)
    Phy.tplay()
