# 不好使的宇宙模拟
# 生成的模型可能会很大（200mb~2gb及以上），请注意设置zhenshu、star_num和name
from wuli import *
import random
biao=[]
zhenshu=500  # 生成多少帧
#Phy.tready()
name="big.txt"  # 文件名
try:
    model = open(name, "r")
    modelbiao = model.readlines()
    model.close()
    Phy.readone(eval(modelbiao[-1]))
except:
    xrange=(-1000,1000)
    yrange=(-1000,1000)
    zrange=(-1000,1000)
    vrange=(0,0)
    mrange=(50,50)
    star_num=500    # 生成多少颗星
    for i in range(star_num):
        biao.append(Phy(m=random.uniform(mrange[0],mrange[1]),
                        v=[random.uniform(vrange[0],vrange[1]),
                           random.uniform(vrange[0],vrange[1]),
                           random.uniform(vrange[0],vrange[1])],
                        p=[random.uniform(xrange[0],xrange[1]),
                           random.uniform(yrange[0],yrange[1]),
                           random.uniform(zrange[0],zrange[1])]
                        ))


for j in range(zhenshu):

    for i in Phy.biao:
        i.bounce(k=10000)
    Phy.gravity(10)
    Phy.run(1)
    #Phy.tplay()
    with open(name,"a") as big:
        big.write(str(Phy.saveone()))
        big.write("\n")
    Phy.rbiao=[]
    print(f"{j},it's working")
print("done")