import numpy as np
import matplotlib.pyplot as plt

def michalewicz(x, m=10):
    n = len(x)
    sum_term = 0
    for i in range(n):
        sum_term += np.sin(x[i]) * (np.sin((i + 1) * x[i]**2 / np.pi))**(2*m)
    return -sum_term

# Create grid of points
x = np.linspace(0, np.pi, 500)
y = np.linspace(0, np.pi, 500)
X, Y = np.meshgrid(x, y)
Z = michalewicz(np.array([X, Y]))

# Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Michalewicz Function')

plt.show()
