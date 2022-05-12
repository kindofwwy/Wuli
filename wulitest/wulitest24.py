from wuli import *
Phy.tready()
r=100
v=1
a=Phy(1,[0,v,0],[r,0,0],r=5)
t=0.01
yuan=0
while True:
    a.force2(v**2/r,[0,0,0])
    Phy.run(t)
    Phy.tplay(fps=10)
    yuan+=(a.v[0]**2+a.v[1]**2)**0.5*t
    if [round(a.p[0],2),round(a.p[1],2)]==[-r,0]:
        break
print(yuan/r)