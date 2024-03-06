import numpy as np
import matplotlib.pyplot as plt
def griewank(x, y):
    term1 = x**2 / 4000
    term2 = np.cos(x / np.sqrt(np.arange(1, len(x) + 1)))
    sum_term = np.sum(term1) - np.prod(term2)
    return 1 + sum_term

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x, y)
Z = griewank(X, Y)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Griewank Function')

plt.show()
