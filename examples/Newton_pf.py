from scipy.integrate import solve_ivp
from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify

# Define the variables and parameters
u, v, x, t = symbols('u v x t')
m = 1
b = 0.5 # Specify a single value for b
k = 0.9
g = 9.81
x0 = 2
u0 = 1

# Define the system of differential equations
du_dt = -b/m*u - k/m*x - g/m
dv_dt = -b/m*v - k/m*u
dx_dt = u

# Define the initial conditions
ics = [x.subs(t, 0) - x0, u.subs(t, 0) - u0, v.subs(t, 0)]

# Convert the symbolic expressions to Python functions
du_dt_func = lambdify((u, v, x), du_dt, modules='numpy')
dv_dt_func = lambdify((u, v, x), dv_dt, modules='numpy')
dx_dt_func = lambdify((u, v, x), dx_dt, modules='numpy')

# Define the function to pass to solve_ivp
def f(t, y):
    u, v, x = y
    return [du_dt_func(u, v, x), dv_dt_func(u, v, x), dx_dt_func(u, v, x)]

# Define the time range
t_span = (0, 10)
t_eval = np.linspace(*t_span, 100)

# Set up the plot
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
x_min, x_max = -5, 5
u_min, u_max = -5, 5

# Solve the system of differential equations
sol = solve_ivp(f, t_span, [u0, 0, x0], t_eval=t_eval)

# Plot the phase portrait
ax[0].set_xlim([x_min, x_max])
ax[0].set_ylim([u_min, u_max])
ax[0].set_xlabel('x')
ax[0].set_ylabel('u')
ax[0].set_title(f'Portretul fazic pentru condițiile inițiale x0={x0},u0={u0} \n și masa={m} kg')
ax[0].plot(sol.y[2], sol.y[0], color='blue')

# Plot the direction field
X, U = np.meshgrid(np.linspace(x_min, x_max, 20), np.linspace(u_min, u_max, 20))
Udot = du_dt_func(U, 0, X)
Xdot = dx_dt_func(U, 0, X)
ax[0].quiver(X, U, Xdot, Udot, color='red')

# # Plot the flow across the plane
ax[1].set_xlim([x_min, x_max])
ax[1].set_ylim([u_min, u_max])
ax[1].set_xlabel('x')
ax[1].set_ylabel('u')
ax[1].set_title('Fluxul')
ax[1].streamplot(X, U, Xdot, Udot)

plt.show()
