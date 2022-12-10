import matplotlib.pyplot as plt
import numpy as np
from palettable.cartocolors.sequential import DarkMint_4  # type: ignore


np.random.seed(19680801)
Z = np.random.rand(126, 136)
x = np.arange(-0.5, 136, 1)  # len = 200
y = np.arange(-0.5, 126, 1)  # len = 300


# 色彩拟合
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


print(cl_color(1, 2, 3))
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, cmap=DarkMint_4.mpl_colormap)
# plt.show()
# plt.savefig('output/Figure_3.png')
