from wuli import *

name="big.txt"
model=open(name,"r")
modelbiao=model.readlines()
model.close()

Phy.tready()
jmp=1

for i in range(len(modelbiao)):
    if i%jmp==0:
        Phy.readone(eval(modelbiao[i]))

        Phy.tplay(x=[[1,0,0],[0,1,0],[0,0,0]])

print("done")

