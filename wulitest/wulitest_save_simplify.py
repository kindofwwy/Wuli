from wuli import *
name="big2.txt"

def sim_biao(biao):
    for i in range(len(biao)):
        biao[i]=round(biao[i],2)
print("loading model...")
with open(name,"r") as model:
    modelbiao=model.readlines()
print("processing...")
with open(name[0:-4]+"_sim.txt","w") as newmodel:
    for i in range(len(modelbiao)):
        if i==len(modelbiao)-1:
            newmodel.write(modelbiao[-1])
            break
        Phy.readone(eval(modelbiao[i]))
        for j in range(len(Phy.biao)):
            sim_biao(Phy.biao[j].v)
            sim_biao(Phy.biao[j].p)
            sim_biao(Phy.biao[j].axianshi)
        newmodel.write(str(Phy.saveone()))
        newmodel.write("\n")
print("done")

