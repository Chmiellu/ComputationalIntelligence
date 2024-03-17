from Hill_climbing import Individual, hill_climbing
import numpy as np
import matplotlib.pyplot as plt

individual = Individual([0, 0])
start_point = individual.random_point()

infos = hill_climbing(Individual(start_point))

for idx, (point, cost_value) in enumerate(infos):
    print(f"Krok {idx + 1}: Punkt: {point}, Wartość funkcji kosztu: {cost_value}")


def sphere(x, y):
    return x**2 + y**2

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = sphere(X, Y)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

for idx, (point, cost_value) in enumerate(infos):
    if idx % 10 == 0:
        ax.scatter(point[0], point[1], cost_value, color='red', s=5)

ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.title('Sphere Function')
plt.show()


