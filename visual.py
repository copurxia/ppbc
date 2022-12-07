import matplotlib.pyplot as plt
import numpy as np
from palettable.cartocolors.sequential import DarkMint_4  # type: ignore


np.random.seed(19680801)
Z = np.random.rand(126, 136)
x = np.arange(-0.5, 136, 1)  # len = 200
y = np.arange(-0.5, 126, 1)  # len = 300


fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, cmap=DarkMint_4.mpl_colormap)
print(type(DarkMint_4.mpl_colormap))
print(DarkMint_4.mpl_colormap)
plt.show()
