from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Function that defines the Lotka-Volterra equations

def f(t, y):
    x, y = y
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]


# Parameters
alpha = 1.0
beta = 0.5
gamma = 0.5
delta = 2.0
x0=0.1
y0=0.2

ics = [x0, y0]

# Define the time range
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

# Solve the system of differential equations
sol = solve_ivp(f, t_span, ics, t_eval=t_eval)
# Set up the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the direction field on the first subplot
x_min, x_max = -0.5, 5
y_min, y_max = -1, 20
X, Y = np.meshgrid(np.linspace(x_min, x_max, 20), np.linspace(y_min, y_max, 20))
U, V = f(0, [X, Y])
ax1.quiver(X, Y, U, V, color='red')

# Plot the phase portrait on the first subplot
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title(f'Portetul fazic pentru condițiile inițiale: x0={x0}, y0={y0}')
ax1.plot(sol.y[0], sol.y[1], color='blue')

# Plot the flow across the plane on the first subplot
ax1.streamplot(X, Y, U, V, color='red', linewidth=0.5, density=1.5)

# Plot the solutions on the second subplot
ax2.plot(sol.t, sol.y[0], label='Prada')
ax2.plot(sol.t, sol.y[1], label='Prădător')
ax2.set_xlabel('t')
ax2.set_ylabel('Populație')
ax2.set_title('Populație vs. Timp')
ax2.legend()

# Show the plot
plt.tight_layout()
plt.show()