import numpy as np
from matplotlib import pyplot as plt


def linearconv(nx):
    dx = 2 / (nx - 1)
    nt = 20  # nt is the number of timesteps we want to calculate
    sigma = .5
    c = 1

    dt = dx * sigma

    u = np.ones(nx)  # defining a np array which is nx elements long with every value equal to 1.
    u[int(.5 / dx):int(1 / dx + 1)] = 2  # setting u = 2 between 0.5 and 1 as per our I.C.s

    un = np.ones(nx)  # initializing our placeholder array, un, to hold the values we calculate for the n+1 timestep

    for n in range(nt):  # iterate through time
        un = u.copy()  ##copy the existing values of u into un
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])

    plt.plot(np.linspace(0, 2, nx), u)
    plt.show()

if __name__ == '__main__':
    linearconv(85)