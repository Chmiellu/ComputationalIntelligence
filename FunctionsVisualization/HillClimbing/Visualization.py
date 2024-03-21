from Hill_climbing import Individual, hill_climbing
import numpy as np
import matplotlib.pyplot as plt


def sphere(*args):
    return sum(arg**2 for arg in args)


def schwefel(*args):
    return 418.9829 * len(args) - np.sum(
        arg * np.sin(np.sqrt(np.abs(arg))) for arg in args
    )


def michalewicz(*args, m=10):
    n = len(args)
    sum_term = 0
    for i in range(n):
        sum_term += np.sin(args[i]) * (np.sin((i + 1) * args[i] ** 2 / np.pi)) ** (
            2 * m
        )
    return -sum_term


# Options: sphere, schwefel, michalewicz
function = schwefel

# Options: every10, full, start_end
points = "start_end"

individual = Individual([0, 0], function)
start_point = individual.random_point()

infos = hill_climbing(Individual(start_point, function))

for idx, (point, cost_value) in enumerate(infos):
    print(f"Krok {idx + 1}: Punkt: {point}, Wartość funkcji kosztu: {cost_value}")

if function == sphere:
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
elif function == schwefel:
    x = np.linspace(-50, 50, 100)
    y = np.linspace(-50, 50, 100)
elif function == michalewicz:
    x = np.linspace(0, np.pi, 100)
    y = np.linspace(0, np.pi, 100)

X, Y = np.meshgrid(x, y)

Z = function(X, Y)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis")

for idx, (point, cost_value) in enumerate(infos):
    if points == "every10":
        if idx % 10 == 0:
            ax.scatter(point[0], point[1], cost_value, color="red", s=50)
    elif points == "full":
        ax.scatter(point[0], point[1], cost_value, color="red", s=50)
    elif points == "start_end":
        if idx == 0:
            ax.scatter(
                point[0], point[1], cost_value, color="blue", label="Start Point", s=50
            )
        elif idx == len(infos) - 1:
            ax.scatter(
                point[0], point[1], cost_value, color="red", label="End Point", s=50
            )
            ax.legend()

ax.set_xlabel("X")
ax.set_ylabel("Y")
function_title = "not defined"
if function == sphere:
    function_title = "Sphere"
elif function == schwefel:
    function_title = "Schwefel"
elif function == michalewicz:
    function_title = "Michalewicz"
plt.title(function_title)
plt.show()
