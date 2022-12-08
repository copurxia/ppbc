import os
import datetime
import copy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from palettable.cartocolors.sequential import DarkMint_4  # type: ignore
from haishoku.haishoku import Haishoku


def date_num(y, m, d):
    d1 = datetime.date(y, m, d)
    d2 = datetime.date(y, 1, 1)
    return (d1-d2).days


r = np.zeros((2600, 366), dtype=int)
g = np.zeros((2600, 366), dtype=int)
b = np.zeros((2600, 366), dtype=int)

plants = os.listdir("img")
color_map = []

for plant in plants:
    print(plant)
    index_count = np.zeros(366, dtype=int)
    pl_imgs = os.listdir("img\\"+plant)
    pl_imgs.sort()
    for pl_img in pl_imgs:
        print(plant.split(" ")[1])
        haishoku = Haishoku.loadHaishoku("img\\"+plant+"\\"+pl_img)
        print("日期：", pl_img.split(" ")[1])
        datear = pl_img.split(" ")[1].split("-")
        orar_index = date_num(
            int(datear[0]), int(datear[1]), int(datear[2]))
        arindex = orar_index
        index_n = 1
        while index_count[arindex] > index_n:
            arindex = arindex+1
            if arindex == 366:
                arindex = orar_index
                index_n = index_n+1
        print("数组序号：", arindex)
        index_count[arindex] = index_count[arindex]+1
        print("时间：", pl_img.split(" ")[2].split(".")[0].replace(";", ":"))
        print("主色：", haishoku.dominant)
        for i in range(0, 2600):
            if r[i][arindex] == 0 and g[i][arindex] == 0 and b[i][arindex] == 0:  # type: ignore
                r[i][arindex] = copy.copy(haishoku.dominant[0])  # type: ignore
                g[i][arindex] = copy.copy(haishoku.dominant[1])  # type: ignore
                b[i][arindex] = copy.copy(haishoku.dominant[2])  # type: ignore
                color_str = "#"+'{:02X}'.format(r[i][arindex]) + \
                    '{:02X}'.format(g[i][arindex]) + \
                    '{:02X}'.format(b[i][arindex])
                print("colorstr=", color_str)
                print("i=", i)
                break
        print("")
for _c in range(0, 100):
    for i in range(0, 2599):
        for j in range(366, 1):
            if g[i][j] == 0:
                if not g[i+1][j] == 0:
                    g[i][j] = g[i+1][j]
                    g[i+1][j] = 0
                elif not g[i+1][j-1] == 0:
                    g[i][j] = g[i+1][j-1]
                    g[i+1][j-1] = 0

x = np.arange(-0.5, 366, 1)  # len = 2600
y = np.arange(-0.5, 100, 1)  # len = 366

fig, ax = plt.subplots()
# type: ignore
ax.pcolormesh(x, y, g[:100], cmap=DarkMint_4.mpl_colormap)
# plt.show()
plt.savefig('output/Figure_3.png')