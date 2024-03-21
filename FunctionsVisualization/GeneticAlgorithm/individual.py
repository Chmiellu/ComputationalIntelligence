import numpy as np
import random
class Individual:
    def __init__(self, genotyp):
        self.genotyp = genotyp


    def mutate(self, mutation_rate):
        genotyp_size = self.genotyp.shape[0]
        number_genes_to_change = int(np.ceil(genotyp_size * mutation_rate))
        genes_to_change = random.choices(range(genotyp_size), k=number_genes_to_change)
        self.genotyp[genes_to_change] = -self.genotyp[genes_to_change] + 1

    def evaluate(self, task):
        weight_sum = (self.genotyp * task.weights).sum()
        sizes_sum = (self.genotyp * task.sizes).sum()
        costs_sum = (self.genotyp * task.costs).sum()
        if weight_sum <= task.Weight_limit and sizes_sum <= task.Size_limit:
            return costs_sum
        else:
            return 0
