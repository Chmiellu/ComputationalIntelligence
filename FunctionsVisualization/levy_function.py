import numpy as np
import matplotlib.pyplot as plt

def schwefel(x):
    return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))), axis=0)

# Create grid of points
x = np.linspace(-500, 500, 500)
y = np.linspace(-500, 500, 500)
X, Y = np.meshgrid(x, y)
Z = schwefel(np.array([X, Y]))

# Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Schwefel Function')

plt.show()
