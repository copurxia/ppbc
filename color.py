import os
import datetime
import copy
import numpy as np
import matplotlib.pyplot as plt
from palettable.cartocolors.sequential import DarkMint_4  # type: ignore
from haishoku.haishoku import Haishoku

# 色彩拟合sec
color_arr = ["#fff5f5", "#ffe3e3", "#ffc9c9", "#ffa8a8",  # Red
             "#ff8787", "#ff6b6b", "#fa5252", "#f03e3e", "#e03131", "#c92a2a",
             "#fff0f6", "#ffdeeb", "#fcc2d7", "#faa2c1",  # Pink
             "#f783ac", "#f06595", "#e64980", "#d6336c", "#c2255c", "#a61e4d",
             "#f8f0fc", "#f3d9fa", "#eebefa", "#e599f7",  # Grape
             "#da77f2", "#cc5de8", "#be4bdb", "#ae3ec9", "#9c36b5", "#862e9c",
             "#f3f0ff", "#e5dbff", "#d0bfff", "#b197fc",  # Violet
             "#9775fa", "#845ef7", "#7950f2", "#7048e8", "#6741d9", "#5f3dc4",
             "#edf2ff", "#dbe4ff", "#bac8ff", "#91a7ff",  # Indigo
             "#748ffc", "#5c7cfa", "#4c6ef5", "#4263eb", "#3b5bdb", "#364fc7",
             "#e7f5ff", "#d0ebff", "#a5d8ff", "#74c0fc",  # Blue
             "#4dabf7", "#339af0", "#228be6", "#1c7ed6", "#1971c2", "#1864ab",
             "#e3fafc", "#c5f6fa", "#99e9f2", "#66d9e8",  # Cyan
             "#3bc9db", "#22b8cf", "#15aabf", "#1098ad", "#0c8599", "#0b7285",
             "#e6fcf5", "#c3fae8", "#96f2d7", "#63e6be",  # Teal
             "#38d9a9", "#20c997", "#12b886", "#0ca678", "#099268", "#087f5b",
             "#ebfbee", "#d3f9d8", "#b2f2bb", "#8ce99a",  # Green
             "#69db7c", "#51cf66", "#40c057", "#37b24d", "#2f9e44", "#2b8a3e",
             "#f4fce3", "#e9fac8", "#d8f5a2", "#c0eb75",  # Lime
             "#a9e34b", "#94d82d", "#82c91e", "#74b816", "#66a80f", "#5c940d",
             "#fff9db", "#fff3bf", "#ffec99", "#ffe066",  # Yellow
             "#ffd43b", "#fcc419", "#fab005", "#f59f00", "#f08c00", "#e67700",
             "#fff3bf", "#ffec99", "#ffe066", "#ffd43b",  # Orange
             "#fcc419", "#fab005", "#f59f00", "#f08c00", "#e67700", "#d9480f"]


def rgb2hsv(r, g, b):  # RGB转HSV
    r = r/255
    g = g/255
    b = b/255
    max = np.max([r, g, b])
    min = np.min([r, g, b])
    h = 0
    s = 0
    v = max
    if max != min:
        if max == r:
            h = 60*(g-b)/(max-min)
        elif max == g:
            h = 60*(b-r)/(max-min)+120
        elif max == b:
            h = 60*(r-g)/(max-min)+240
        if h < 0:
            h = h+360
        s = (max-min)/max
    return h, s, v


def cl_color(r, g, b):  # 颜色拟合
    min = 1000
    cl_color = ""
    h, s, v = rgb2hsv(r, g, b)
    for i in color_arr:
        ir = int(i[1:3], 16)
        ig = int(i[3:5], 16)
        ib = int(i[5:7], 16)
        i_h, i_s, i_v = rgb2hsv(ir, ig, ib)
        dis = pow(pow(i_h-h, 2)+pow(i_s-s, 2)+pow(i_v-v, 2), 0.5)
        if dis < min:
            min = dis
            cl_color = i
    return cl_color


def date_num(y, m, d):  # 日期转换为第几天
    d1 = datetime.date(y, m, d)
    d2 = datetime.date(y, 1, 1)
    return (d1-d2).days


# 读取图片
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
        print(plant)
        haishoku = Haishoku.loadHaishoku("img\\"+plant+"\\"+pl_img)
        print("日期：", pl_img.split(" ")[1])
        datear = pl_img.split(" ")[1].split("-")
        orar_index = date_num(
            int(datear[0]), int(datear[1]), int(datear[2]))
        arindex = orar_index
        index_n = 0
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
                print("clo_col=", cl_color(
                    r[i][arindex], g[i][arindex], b[i][arindex]))
                print("i=", i)
                break
        print("")

# 从左向右补偿
for c in range(0, 900):
    for i in range(0, 2599):
        cnt = 0
        for j in range(365, 0, -1):
            if g[i][j] == 0:
                if not g[i+1][j] == 0:
                    g[i][j] = g[i+1][j]
                    g[i+1][j] = 0
                elif not g[i][j-1] == 0:
                    g[i][j] = g[i][j-1]
                    g[i][j-1] = 0
            else:
                cnt = 1
        if cnt == 0:
            break

# 从右向左补偿
for c in range(0, 1500):
    for i in range(0, 2599):
        cnt = 0
        for j in range(0, 365):
            if g[i][j] == 0:
                if not g[i+1][j] == 0:
                    g[i][j] = g[i+1][j]
                    g[i+1][j] = 0
                elif not g[i][j+1] == 0:
                    g[i][j] = g[i][j+1]
                    g[i][j+1] = 0
            else:
                cnt = 1
        if cnt == 0:
            break

# 折叠
foldr = np.zeros((600, 122), dtype=int)
foldg = np.zeros((600, 122), dtype=int)
foldb = np.zeros((600, 122), dtype=int)
for i in range(100):
    for j in range(366):
        foldr[3*i+j % 3][int(j / 3)] = r[i][j]
        foldg[3*i+j % 3][int(j / 3)] = g[i][j]
        foldb[3*i+j % 3][int(j / 3)] = b[i][j]

# 生成图片
x = np.arange(-0.5, 122, 1)  # len = 2600
y = np.arange(-0.5, 120, 1)  # len = 366

fig, ax = plt.subplots()

ax.pcolormesh(x, y, foldg[:120], cmap=DarkMint_4.mpl_colormap)
# plt.show()
plt.savefig('output/Figure_18.svg')

# 生成SVG
magrin = 10
width = 50
height = 50
file = open('output/final.svg', 'w')
file.write('<svg version="1.1" baseProfile="full" width="8000" height="8000" xmlns="http://www.w3.org/2000/svg">')
for i in range(0, 120):
    for j in range(0, 122):
        color_str = "#"+'{:02X}'.format(foldr[i][j]) + \
                    '{:02X}'.format(foldg[i][j]) + \
                    '{:02X}'.format(foldb[i][j])
        file.write('<rect x="'+str((j+1)*magrin+j*width)+'" y="'+str((i+1)*magrin+i*height) +
                   '" width="'+str(width)+'" height="'+str(height)+'" fill="'+color_str+'" />')
file.write('</svg>')

# 生成单色SVG
file = open('output/green.svg', 'w')
file.write('<svg version="1.1" baseProfile="full" width="8000" height="8000" xmlns="http://www.w3.org/2000/svg">')
for i in range(0, 120):
    for j in range(0, 122):
        color_str = "#"+'00' + \
                    '{:02X}'.format(foldg[i][j]) + \
                    '00'
        file.write('<rect x="'+str(j*magrin+j*width)+'" y="'+str(i*magrin+i*height) +
                   '" width="'+str(width)+'" height="'+str(height)+'" fill="'+color_str+'" />')
file.write('</svg>')

# 色彩拟合
file = open('output/ownclo.svg', 'w')
file.write('<svg version="1.1" baseProfile="full" width="8000" height="8000" xmlns="http://www.w3.org/2000/svg">')
for i in range(0, 120):
    for j in range(0, 122):
        color_str = cl_color(foldr[i][j], foldg[i][j], foldb[i][j])
        file.write('<rect x="'+str(j*magrin+j*width)+'" y="'+str(i*magrin+i*height) +
                   '" width="'+str(width)+'" height="'+str(height)+'" fill="'+color_str+'" />')
file.write('</svg>')
