from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
mu = 2
x0 = 2.5
y0 = -0.75

# Define the system of differential equations
def f(t, y):
    x, y = y
    return [y, mu*(1 - x**2)*y - x]

# Define the initial conditions
ics = [x0, y0]

# Define the time range
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

# Solve the system of differential equations
sol = solve_ivp(f, t_span, ics, t_eval=t_eval)

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the direction field
x_min, x_max = -5, 5
y_min, y_max = -10, 10
X, Y = np.meshgrid(np.linspace(x_min, x_max, 20), np.linspace(y_min, y_max, 20))
U, V = f(0, [X, Y])
ax.quiver(X, Y, U, V, color='red')

# Plot the phase portrait
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Portetul fazic pentru condițiile inițiale x0={x0},y0={y0} \n și μ={mu}')
ax.plot(sol.y[0], sol.y[1], color='blue')

# Plot the flow across the plane
ax.streamplot(X, Y, U, V, color='red', linewidth=0.5, density=1.5)

plt.show()
