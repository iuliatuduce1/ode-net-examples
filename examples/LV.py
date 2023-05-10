from scipy.integrate import odeint
import numpy as np

import numpy as np
from scipy.integrate import odeint


def lotka_volterra(y, t, a, b, c, d):
    # y din R 2
    # y[0] represents the number of prey
    # y[1] represents the number of predators

    dydt = [a * y[0] - b * y[0] * y[1], -c * y[1] + d * y[0] * y[1]]

    return dydt


def verhust(y,t,k,L):
     # y populatia
#  k rata de crestere per capita
# L const de suport relativ al mediului

    dydt=k*y(1-y/L)
    return dydt



def sl(y,t,alpha,beta,omega,I):

   dydt=[alpha * y[0] - beta * y[0] ** 3 - omega * y[1] + I, omega * y[0] + alpha * y[1] - beta * y[1] ** 3]
   return dydt
def test_lotka_volterra():
    # Initial conditions and constants
    y0 = [10, 5]
    a, b, c, d = 1.5, 0.75, 1, 0.75

    steps = 100

    t = np.linspace(0, 10, steps)

    solution = odeint(lotka_volterra, y0, t, args=(a, b, c, d))

    import matplotlib.pyplot as plt
    plt.plot(t, solution[:, 0], 'b', label='Prey')
    plt.plot(t, solution[:, 1], 'g', label='Predators')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
