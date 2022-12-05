import matplotlib.pyplot as plt
import numpy as np


np.random.seed(19680801)
Z = np.random.rand(100, 165)
x = np.arange(-0.5, 165, 1)  # len = 200
y = np.arange(-0.5, 100, 1)  # len = 300


fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
plt.show()
