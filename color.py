import os
import datetime
import copy
import numpy as np
from haishoku.haishoku import Haishoku


def date_num(y, m, d):
    d1 = datetime.date(y, m, d)
    d2 = datetime.date(y, 1, 1)
    return (d1-d2).days


r = np.zeros((366, 2600), dtype=int)
g = np.zeros((366, 2600), dtype=int)
b = np.zeros((366, 2600), dtype=int)

plants = os.listdir("img")

for plant in plants:
    print(plant)
    pl_imgs = os.listdir("img\\"+plant)
    for pl_img in pl_imgs:
        print(plant.split(" ")[1])
        haishoku = Haishoku.loadHaishoku("img\\"+plant+"\\"+pl_img)
        print("日期：", pl_img.split(" ")[1])
        datear = pl_img.split(" ")[1].split("-")
        arindex = date_num(
            int(datear[0]), int(datear[1]), int(datear[2]))
        print("数组序号：", arindex)
        print("时间：", pl_img.split(" ")[2].split(".")[0].replace(";", ":"))
        print("主色：", haishoku.dominant)
        for i in range(0, 2600):
            if r[i][arindex] == 0 and g[i][arindex] == 0 and b[i][arindex] == 0:
                r[i][arindex] = copy.copy(haishoku.dominant[0])  # type: ignore
                g[i][arindex] = copy.copy(haishoku.dominant[1])  # type: ignore
                b[i][arindex] = copy.copy(haishoku.dominant[2])  # type: ignore
                print("i=", i)
                break
        print("")
