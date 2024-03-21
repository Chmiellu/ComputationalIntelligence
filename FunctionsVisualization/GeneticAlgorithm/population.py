import random
import numpy as np
from individual import Individual
class Population:
    def __init__(self, genotyp_size=None, population_size=None):
        self.population = []
        if genotyp_size != None and population_size != None:
            population_array = np.random.choice(
                [0, 1], size=(population_size, genotyp_size), p=[0.85, 0.15]
            )
        for genotyp in population_array:
            individual = Individual(genotyp)
            self.population.append(individual)
        self.size = len(self.population)

    def tournament(self, tournament_size, task):
        selected = random.choices(self.population, k=tournament_size)
        evaluation = [elem.evaluate(task) for elem in selected]
        idx_best_individual = evaluation.index(max(evaluation))
        return selected[idx_best_individual]

    def crossover(self, crossover_rate, parent_1, parent_2, task):
        if np.random.random() < crossover_rate:
            splitting_point = np.random.randint(1, len(parent_1.genotyp))
            result_genotyp = np.concatenate([
                parent_1.genotyp[:splitting_point],
                parent_2.genotyp[splitting_point:]
            ])
            result = Individual(result_genotyp)
        else:
            result = parent_1
        return result

    def add_child(self, child):
        self.population.append(child)
        self.size = len(self.population)

    def best(self, task):
        evaluation = [individual.evaluate(task) for individual in self.population]
        idx_best_individual = evaluation.index(max(evaluation))
        best = self.population[idx_best_individual]
        return best, best.evaluate(task)

    def evaluate(self, task):
        evaluation = np.array(
            [individual.evaluate(task) for individual in self.population]
        )
        return evaluation
