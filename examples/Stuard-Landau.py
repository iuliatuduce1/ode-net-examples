import numpy as np
from scipy.integrate import odeint

# Define the parameters
alpha = 1.0
beta = 1.0
omega = 1.0
I = 0.0

# Define the function that returns the rate of change of the state variables
def stuart_landau(x, t):
    dxdt = alpha*x[0] - beta*x[0]**3 - omega*x[1] + I
    dydt = omega*x[0] + alpha*x[1] - beta*x[1]**3
    return [dxdt, dydt]

# Define the initial conditions and time vector
x0 = [1.0, 0.0]
t = np.linspace(0, 10, 1000)

# Solve the differential equations
sol = odeint(stuart_landau, x0, t)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], label='x')
plt.plot(t, sol[:, 1], label='y')
plt.xlabel('Time')
plt.ylabel('State variables')
plt.legend()
plt.show()
