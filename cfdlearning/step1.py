import numpy as np
from matplotlib import pyplot as plt
import time,sys

nx = 41
dx = 2 / (nx-1)
nt = 25
dt = .025
c = 1
u = np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2

un = np.ones(nx)
un = u.copy()
print(un)
print('finish')
for n in range(nt):
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

plt.plot(np.linspace(0, 2, nx), u)
plt.show()
