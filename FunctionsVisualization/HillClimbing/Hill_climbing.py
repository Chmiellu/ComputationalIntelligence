import numpy as np
import matplotlib.pyplot as plt
import random

class Individual:
    def __init__(self, genotyp):
        self.genotyp = np.round(np.array(genotyp, dtype=float), 2)
        self.fenotyp = np.round(np.array(genotyp, dtype=float), 2)

    def Cost(self):
        return round((np.sum(self.genotyp ** 2)), 8)

    def Neighboor(self, index, step_size):
        new_genotyp = np.copy(self.genotyp)
        if index == 0:
            new_genotyp[0] += step_size
        elif index == 1:
            new_genotyp[0] -= step_size
        elif index == 2:
            new_genotyp[1] += step_size
        elif index == 3:
            new_genotyp[1] -= step_size
        return Individual(new_genotyp)

    def random_point(self, x_range=(-3, 3), y_range=(-3, 3)):
        x = round(random.uniform(*x_range), 2)
        y = round(random.uniform(*y_range), 2)
        return x, y

def hill_climbing(start_point, step_size=0.01, max_iterations=5000):
    current_point = start_point
    path = [(current_point.genotyp, current_point.Cost())]

    for _ in range(max_iterations):
        neighbors = []
        for i in range(4):
            neighbor = current_point.Neighboor(i, step_size)
            neighbors.append(neighbor)

        best_neighbor = min(neighbors, key=lambda x: x.Cost())

        if min(x.Cost() for x in neighbors) >= current_point.Cost():
            print(f"Osiągnięto globalne minimum. Zakończono na kroku {_ + 1}. Kolejny krok zwiększy funkcję kosztu.")
            break

        current_point = best_neighbor
        path.append((current_point.genotyp, current_point.Cost()))

    return path

individual = Individual([0, 0])
start_point = individual.random_point()

infos = hill_climbing(Individual(start_point))

#for idx, (point, cost_value) in enumerate(infos):
 #   print(f"Krok {idx + 1}: Punkt: {point}, Wartość funkcji kosztu: {cost_value}")
